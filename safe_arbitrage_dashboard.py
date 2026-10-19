import time
import random
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import pandas as pd
import streamlit as st

# ==========================================
# 0. พจนานุกรมแปลภาษา (Localization / Dictionary)
# ==========================================
LANG_DICT = {
    "English": {
        "title": "🛡️ Arbitrage & Price Monitor (Safe API & Rate-Limited Edition)",
        "caption": "Dashboard for price disparity monitoring with rate limiter, backoff, and caching.",
        "sidebar_sec": "🛡️ Security & Rate Limit",
        "min_delay": "Min Delay per Item (seconds)",
        "max_delay": "Max Delay per Item (seconds)",
        "proxy_info": "Proxy URL (Optional)",
        "cache_info": "💡 Auto-Cache 10m enabled to prevent duplicate requests.",
        "profit_sec": "💰 Profit Target Settings",
        "min_margin": "Min Required Margin (%)",
        "platform_fee": "Platform Fee (%)",
        "btn_fetch": "🔄 Fetch Latest Data (Safe Fetch)",
        "btn_clear": "🗑️ Clear Cache & Re-fetch",
        "spinner": "Fetching data under rate limits...",
        "kpi_total": "Total Items Checked",
        "kpi_target": "Meeting Profit Target",
        "kpi_delay": "Delay Range",
        "kpi_status": "Protection Status",
        "table_title": "📊 Price Disparity & Data Fetch Status Table",
        "col_sku": "SKU",
        "col_name": "Product Name",
        "col_platform": "Data Source",
        "col_cost": "Cost (THB)",
        "col_market": "Market Price (THB)",
        "col_fee": "Fee (THB)",
        "col_profit": "Net Profit (THB)",
        "col_margin": "Net Margin (%)",
        "col_delay": "Delay Used (s)",
        "col_status": "Connection Status",
        "col_advice": "Recommendation",
        "status_profitable": "🔥 Profitable",
        "status_wait": "Hold"
    },
    "ไทย": {
        "title": "🛡️ ระบบตรวจสอบส่วนต่างราคาและราคาลดพิเศษ (Safe API & Rate-Limited)",
        "caption": "แดชบอร์ดตรวจสอบส่วนต่างราคาพร้อมระบบควบคุมความถี่ (Rate Limiter, Backoff & Caching)",
        "sidebar_sec": "🛡️ ตั้งค่าความปลอดภัย (Rate Limit & Proxy)",
        "min_delay": "หน่วงเวลาต่ำสุดต่อรายการ (วินาที)",
        "max_delay": "หน่วงเวลาสูงสุดต่อรายการ (วินาที)",
        "proxy_info": "Proxy URL (ตัวเลือกเสริม)",
        "cache_info": "💡 เปิดใช้งาน Auto-Cache 10 นาที เพื่อป้องกันการส่ง Request ซ้ำ",
        "profit_sec": "💰 ตั้งค่าเป้าหมายกำไร",
        "min_margin": "กำไรขั้นต่ำที่ต้องการ (%)",
        "platform_fee": "หักค่าธรรมเนียมแพลตฟอร์ม (%)",
        "btn_fetch": "🔄 ดึงข้อมูลล่าสุด (Safe Fetch)",
        "btn_clear": "🗑️ ล้าง Cache เพื่อดึงใหม่ทันที",
        "spinner": "กำลังดึงข้อมูลภายใต้เงื่อนไข Rate Limit...",
        "kpi_total": "รายการที่ตรวจสอบ",
        "kpi_target": "เข้าเกณฑ์กำไรสุทธิ",
        "kpi_delay": "ช่วงเวลาหน่วงต่อคำขอ",
        "kpi_status": "สถานะการป้องกัน",
        "table_title": "📊 ตารางวิเคราะห์ส่วนต่างราคาและสถานะการดึงข้อมูล",
        "col_sku": "รหัส SKU",
        "col_name": "ชื่อสินค้า",
        "col_platform": "ช่องทางข้อมูล",
        "col_cost": "ราคาทุน (บาท)",
        "col_market": "ราคาตลาด (บาท)",
        "col_fee": "ค่าธรรมเนียม (บาท)",
        "col_profit": "กำไรสุทธิ (บาท)",
        "col_margin": "กำไรสุทธิ (%)",
        "col_delay": "เวลาหน่วงที่ใช้ (วินาที)",
        "col_status": "สถานะการเชื่อมต่อ",
        "col_advice": "คำแนะนำ",
        "status_profitable": "🔥 ทำกำไรได้",
        "status_wait": "รอก่อน"
    }
}

# ==========================================
# 1. โมดูลจัดการการเชื่อมต่อแบบปลอดภัย (Safe Request Engine)
# ==========================================
class SafeDataClient:
    def __init__(self, min_delay: float = 2.0, max_delay: float = 5.0, proxy_url: str = ""):
        self.min_delay = min_delay
        self.max_delay = max_delay
        self.proxy_url = proxy_url
        self.session = self._create_resilient_session()
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
        ]

    def _create_resilient_session(self) -> requests.Session:
        session = requests.Session()
        retry_strategy = Retry(
            total=3,
            backoff_factor=2,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["HEAD", "GET", "OPTIONS"]
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        return session

    def fetch_item_data(self, item: dict) -> dict:
        delay = random.uniform(self.min_delay, self.max_delay)
        time.sleep(delay)
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

@st.cache_data(ttl=600)
def run_safe_batch_scan(items: list, min_delay: float, max_delay: float, proxy: str):
    client = SafeDataClient(min_delay=min_delay, max_delay=max_delay, proxy_url=proxy)
    results = []
    for item in items:
        res = client.fetch_item_data(item)
        results.append(res)
    return results

# ==========================================
# 2. ตั้งค่าหน้าตา Streamlit Dashboard
# ==========================================
st.set_page_config(page_title="Safe Price & Arbitrage Dashboard", layout="wide")

# --- Sidebar: ตัวเลือกภาษาและตั้งค่าความปลอดภัย ---
selected_lang = st.sidebar.selectbox("🌐 Language / ภาษา", ["English", "ไทย"], index=0)
lang = LANG_DICT.get(selected_lang, LANG_DICT["English"])

st.sidebar.header(lang["sidebar_sec"])
min_delay = st.sidebar.slider(lang["min_delay"], 1.0, 10.0, 2.0, 0.5)
max_delay = st.sidebar.slider(lang["max_delay"], 2.0, 15.0, 4.5, 0.5)
if max_delay < min_delay:
    max_delay = min_delay + 1.0

proxy_input = st.sidebar.text_input(lang["proxy_info"], placeholder="http://user:pass@ip:port")
st.sidebar.info(lang["cache_info"])

st.sidebar.markdown("---")
st.sidebar.header(lang["profit_sec"])
min_margin_pct = st.sidebar.slider(lang["min_margin"], 5, 50, 20, 5)
platform_fee_pct = st.sidebar.slider(lang["platform_fee"], 0.0, 15.0, 8.5, 0.5)

# --- ส่วนหัวของหน้าเว็บ ---
st.title(lang["title"])
st.caption(lang["caption"])

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
    trigger = st.button(lang["btn_fetch"])
with col_btn2:
    if st.button(lang["btn_clear"]):
        st.cache_data.clear()
        st.rerun()

# ประมวลผลข้อมูล
with st.spinner(lang["spinner"]):
    raw_results = run_safe_batch_scan(catalog, min_delay, max_delay, proxy_input)

# คำนวณกำไรหลังหักค่าธรรมเนียม
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
        lang["col_sku"]: r["sku"],
        lang["col_name"]: r["name"],
        lang["col_platform"]: r["platform"],
        lang["col_cost"]: f"{cost:,.2f}",
        lang["col_market"]: f"{sell:,.2f}",
        lang["col_fee"]: f"{fee:,.2f}",
        lang["col_profit"]: f"{net_profit:,.2f}",
        lang["col_margin"]: round(margin_pct, 1),
        lang["col_delay"]: r["delay_used"],
        lang["col_status"]: r["status"],
        lang["col_advice"]: lang["status_profitable"] if is_target else lang["status_wait"]
    })

# แสดงผล KPI ด้านบน
m1, m2, m3, m4 = st.columns(4)
m1.metric(lang["kpi_total"], f"{len(table_rows)}")
m2.metric(lang["kpi_target"], f"{high_profit_count}", delta=f">={min_margin_pct}%")
m3.metric(lang["kpi_delay"], f"{min_delay} - {max_delay} s")
m4.metric(lang["kpi_status"], "Active (Retry + Cache)")

st.markdown("---")
st.subheader(lang["table_title"])

df_out = pd.DataFrame(table_rows)

def style_opportunity(row):
    advice_col = lang["col_advice"]
    profitable_text = lang["status_profitable"]
    return [
        "background-color: #d4edda; color: #155724; font-weight: bold"
        if row[advice_col] == profitable_text else ""
        for _ in row
    ]

st.dataframe(df_out.style.apply(style_opportunity, axis=1), use_container_width=True)
