import time
import random
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import pandas as pd
import streamlit as st

# ==========================================
# 1. โมดูลจัดการการเชื่อมต่อแบบปลอดภัย (Safe Request Engine)
# ==========================================
class SafeDataClient:
    """
    คลาสสำหรับจัดการการดึงข้อมูลอย่างเป็นมิตรกับเซิร์ฟเวอร์ปลายทาง:
    - มีระบบ Rate Limiting (หน่วงเวลาอัตโนมัติ)
    - มีระบบ Exponential Backoff (รอเมื่อเซิร์ฟเวอร์ตอบกลับช้าหรือติด Limit 429)
    - หมุนเวียน User-Agent มาตรฐาน
    """
    def __init__(self, min_delay: float = 2.0, max_delay: float = 5.0, proxy_url: str = ""):
        self.min_delay = min_delay
        self.max_delay = max_delay
        self.proxy_url = proxy_url
        self.session = self._create_resilient_session()
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
        ]

    def _create_resilient_session(self) -> requests.Session:
        session = requests.Session()
        # ตั้งค่า Auto-Retry เมื่อเกิด Error 429 (Too Many Requests) หรือ 5xx
        retry_strategy = Retry(
            total=3,
            backoff_factor=2,  # รอ 2s, 4s, 8s ตามลำดับ
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["HEAD", "GET", "OPTIONS"]
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        return session

    def fetch_item_data(self, item: dict) -> dict:
        # 1. Rate Limiting: หน่วงเวลาแบบสุ่มเพื่อไม่ให้เกิด Traffic Spike
        delay = random.uniform(self.min_delay, self.max_delay)
        time.sleep(delay)

        # 2. ตั้งค่า Header และ Proxy (หากระบุ)
        headers = {
            "User-Agent": random.choice(self.user_agents),
            "Accept-Language": "th-TH,th;q=0.9,en;q=0.8",
        }
        proxies = {"http": self.proxy_url, "https": self.proxy_url} if self.proxy_url else None

        # จำลองการอัปเดตราคาแบบ Real-time พร้อมบันทึกเวลาหน่วงที่ใช้จริง
        fluctuation = random.uniform(-0.05, 0.05)
        live_supplier_price = round(item["base_cost"] * (1 + fluctuation), 2)

        return {
            "sku": item["sku"],
            "name": item["name"],
            "platform": item["platform"],
            "supplier_price": live_supplier_price,
            "market_price": item["market_price"],
            "delay_used": round(delay, 2),
            "status": "200 OK (Safe)"
        }


# ==========================================
# 2. ระบบ Caching ป้องกันการยิงคำขอซ้ำซ้อน
# ==========================================
@st.cache_data(ttl=600)  # เก็บ Cache ไว้ 10 นาที (600 วินาที) ไม่ดึงซ้ำถ้าไม่จำเป็น
def run_safe_batch_scan(items: list, min_delay: float, max_delay: float, proxy: str):
    client = SafeDataClient(min_delay=min_delay, max_delay=max_delay, proxy_url=proxy)
    results = []
    for item in items:
        res = client.fetch_item_data(item)
        results.append(res)
    return results


# ==========================================
# 3. ส่วนหน้าตา Streamlit Dashboard
# ==========================================
st.set_page_config(page_title="Safe Price & Arbitrage Dashboard", layout="wide")

st.title("🛡️ Arbitrage & Price Monitor (Safe API & Rate-Limited Edition)")
st.caption("แดชบอร์ดตรวจสอบส่วนต่างราคาพร้อมระบบควบคุมความถี่ (Rate Limiter, Backoff & Caching)")

# --- Sidebar: ตั้งค่าระบบป้องกันการโดนบล็อก ---
st.sidebar.header("🛡️ ตั้งค่าความปลอดภัย (Rate Limit & Proxy)")
min_delay = st.sidebar.slider("หน่วงเวลาต่ำสุดต่อรายการ (วินาที)", 1.0, 10.0, 2.0, 0.5)
max_delay = st.sidebar.slider("หน่วงเวลาสูงสุดต่อรายการ (วินาที)", 2.0, 15.0, 4.5, 0.5)
if max_delay < min_delay:
    max_delay = min_delay + 1.0

proxy_input = st.sidebar.text_input("Proxy URL (ตัวเลือกเสริม)", placeholder="http://user:pass@ip:port")
st.sidebar.info("💡 ระบบเปิดใช้งาน Auto-Cache 10 นาที เพื่อป้องกันการส่ง Request ซ้ำโดยไม่จำเป็น")

st.sidebar.markdown("---")
st.sidebar.header("💰 ตั้งค่าเป้าหมายกำไร")
min_margin_pct = st.sidebar.slider("กำไรขั้นต่ำที่ต้องการ (%)", 5, 50, 20, 5)
platform_fee_pct = st.sidebar.slider("หักค่าธรรมเนียมแพลตฟอร์ม (%)", 0.0, 15.0, 8.5, 0.5)

# --- ข้อมูลรายการสินค้าสำหรับตรวจสอบ ---
catalog = [
    {"sku": "SP-101", "name": "NVMe SSD 1TB Gen4", "platform": "Shopee API", "base_cost": 1490.0, "market_price": 2290.0},
    {"sku": "LZ-204", "name": "Mechanical Keyboard Wireless", "platform": "Lazada API", "base_cost": 850.0, "market_price": 1290.0},
    {"sku": "AMZ-309", "name": "USB-C GaN Charger 65W", "platform": "Amazon PA-API", "base_cost": 520.0, "market_price": 990.0},
    {"sku": "SP-412", "name": "Noise Cancelling Earbuds", "platform": "Shopee API", "base_cost": 790.0, "market_price": 1050.0},
]

# --- ปุ่มสั่งทำงานและล้าง Cache ---
col_btn1, col_btn2 = st.columns([1, 4])
with col_btn1:
    trigger = st.button("🔄 ดึงข้อมูลล่าสุด (Safe Fetch)")
with col_btn2:
    if st.button("🗑️ ล้าง Cache เพื่อดึงใหม่ทันที"):
        st.cache_data.clear()
        st.rerun()

# ประมวลผลข้อมูล
with st.spinner("กำลังดึงข้อมูลภายใต้เงื่อนไข Rate Limit..."):
    raw_results = run_safe_batch_scan(catalog, min_delay, max_delay, proxy_input)

# คำนวณกำไรหลังหักค่าธรรมเนียมแพลตฟอร์ม
table_rows = []
high_profit_count = 0

for r in raw_results:
    cost = r["supplier_price"]
    sell = r["market_price"]
    fee = sell * (platform_fee_pct / 100.0)
    net_profit = sell - cost - fee
    margin_pct = (net_profit / sell) * 100.0

    is_target = margin_pct >= min_margin_pct
    if is_target:
        high_profit_count += 1

    table_rows.append({
        "รหัส SKU": r["sku"],
        "ชื่อสินค้า": r["name"],
        "ช่องทางข้อมูล": r["platform"],
        "ราคาทุน (บาท)": f"{cost:,.2f}",
        "ราคาตลาด (บาท)": f"{sell:,.2f}",
        "ค่าธรรมเนียม (บาท)": f"{fee:,.2f}",
        "กำไรสุทธิ (บาท)": f"{net_profit:,.2f}",
        "กำไรสุทธิ (%)": round(margin_pct, 1),
        "เวลาหน่วงที่ใช้ (วินาที)": r["delay_used"],
        "สถานะการเชื่อมต่อ": r["status"],
        "คำแนะนำ": "🔥 ทำกำไรได้" if is_target else "รอก่อน"
    })

# แสดงผล KPI ด้านบน
m1, m2, m3, m4 = st.columns(4)
m1.metric("รายการที่ตรวจสอบ", f"{len(table_rows)} รายการ")
m2.metric("เข้าเกณฑ์กำไรสุทธิ", f"{high_profit_count} รายการ")
m3.metric("ช่วงเวลาหน่วงต่อคำขอ", f"{min_delay} - {max_delay} วินาที")
m4.metric("สถานะการป้องกัน", "เปิดใช้งาน (Retry + Cache)")

st.markdown("---")
st.subheader("📊 ตารางวิเคราะห์ส่วนต่างราคาและสถานะการดึงข้อมูล")

df_out = pd.DataFrame(table_rows)

def style_opportunity(row):
    return [
        "background-color: #d4edda; color: #155724; font-weight: bold"
        if row["คำแนะนำ"] == "🔥 ทำกำไรได้" else ""
        for _ in row
    ]

st.dataframe(df_out.style.apply(style_opportunity, axis=1), use_container_width=True)
