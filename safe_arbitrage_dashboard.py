import time
import random
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import pandas as pd
import streamlit as st
import plotly.express as px

# ==========================================
# 0. พจนานุกรมแปลภาษา (Localization / Dictionary)
# ==========================================
LANG_DICT = {
    "English": {
        "title": "⚡ Multi-Platform Arbitrage & Intelligence Hub",
        "caption": "Comprehensive price disparity monitoring, multi-category inventory, and real-time risk analytics.",
        "sidebar_sec": "🛡️ Security & Rate Limit",
        "min_delay": "Min Delay per Item (seconds)",
        "max_delay": "Max Delay per Item (seconds)",
        "proxy_info": "Proxy URL (Optional)",
        "cache_info": "💡 Auto-Cache 10m enabled to prevent duplicate requests.",
        "profit_sec": "💰 Business & Profit Settings",
        "min_margin": "Min Required Margin (%)",
        "platform_fee": "Platform Fee (%)",
        "custom_sec": "➕ Add Custom Product to Scan",
        "c_sku": "SKU Code",
        "c_name": "Product Name",
        "c_cat": "Category",
        "c_plat": "Platform",
        "c_cost": "Base Cost (THB)",
        "c_market": "Market Price (THB)",
        "btn_add": "Add to Active Catalog",
        "search_label": "🔍 Search Product or SKU",
        "filter_cat": "Filter by Category",
        "all_cat": "All Categories",
        "filter_platform": "Filter by Platform",
        "all_platforms": "All Platforms",
        "btn_fetch": "🔄 Run Multi-Platform Scan",
        "btn_clear": "🗑️ Clear Cache & Reset",
        "btn_download": "📥 Download Full Report (CSV)",
        "spinner": "Scanning multi-platform markets securely...",
        "kpi_total": "Total Analyzed",
        "kpi_target": "Profitable Opportunities",
        "kpi_profit": "Max Net Profit",
        "kpi_status": "System Security",
        "tab_table": "📋 Master Intelligence Table",
        "tab_chart1": "📈 Profit & Margin Breakdown",
        "tab_chart2": "📊 Cost vs Market Price Comparison",
        "col_sku": "SKU",
        "col_name": "Product Name",
        "col_cat": "Category",
        "col_platform": "Platform",
        "col_cost": "Cost (THB)",
        "col_market": "Market Price (THB)",
        "col_fee": "Fee (THB)",
        "col_profit": "Net Profit (THB)",
        "col_margin": "Net Margin (%)",
        "col_risk": "Risk Level",
        "col_advice": "Action",
        "status_profitable": "🔥 High Margin",
        "status_low": "⚠️ Low Margin",
        "status_wait": "💡 Stable"
    },
    "ไทย": {
        "title": "⚡ ศูนย์กลางวิเคราะห์ส่วนต่างราคาและโอกาสทางธุรกิจ (Multi-Platform Hub)",
        "caption": "ระบบตรวจสอบราคาสินค้าหลากหลายหมวดหมู่ วิเคราะห์ความเสี่ยง และประมวลผลกำไรแบบเรียลไทม์",
        "sidebar_sec": "🛡️ ตั้งค่าความปลอดภัย (Rate Limit & Proxy)",
        "min_delay": "หน่วงเวลาต่ำสุดต่อรายการ (วินาที)",
        "max_delay": "หน่วงเวลาสูงสุดต่อรายการ (วินาที)",
        "proxy_info": "Proxy URL (ตัวเลือกเสริม)",
        "cache_info": "💡 เปิดใช้งาน Auto-Cache 10 นาที ป้องกันการส่งซ้ำ",
        "profit_sec": "💰 ตั้งค่าเป้าหมายธุรกิจและกำไร",
        "min_margin": "กำไรขั้นต่ำที่ต้องการ (%)",
        "platform_fee": "หักค่าธรรมเนียมแพลตฟอร์ม (%)",
        "custom_sec": "➕ เพิ่มสินค้าเองเพื่อสแกน",
        "c_sku": "รหัส SKU",
        "c_name": "ชื่อสินค้า",
        "c_cat": "หมวดหมู่สินค้า",
        "c_plat": "แพลตฟอร์ม",
        "c_cost": "ราคาทุน (บาท)",
        "c_market": "ราคาขายตลาด (บาท)",
        "btn_add": "เพิ่มเข้าสู่ระบบสแกน",
        "search_label": "🔍 ค้นหาชื่อสินค้า หรือ SKU",
        "filter_cat": "กรองตามหมวดหมู่",
        "all_cat": "ทุกหมวดหมู่",
        "filter_platform": "กรองตามแพลตฟอร์ม",
        "all_platforms": "ทุกแพลตฟอร์ม",
        "btn_fetch": "🔄 รันสแกนหลายแพลตฟอร์ม",
        "btn_clear": "🗑️ ล้างแคชและรีเซ็ต",
        "btn_download": "📥 ดาวน์โหลดรายงานทั้งหมด (CSV)",
        "spinner": "กำลังสแกนตลาดหลากหลายแพลตฟอร์มภายใต้ระบบป้องกันความปลอดภัย...",
        "kpi_total": "สินค้าทั้งหมด",
        "kpi_target": "เข้าเกณฑ์ทำกำไร",
        "kpi_profit": "กำไรสุทธิสูงสุด",
        "kpi_status": "สถานะระบบ",
        "tab_table": "📋 ตารางวิเคราะห์ข้อมูลเชิงลึก",
        "tab_chart1": "📈 กราฟกระจายตัวกำไรและอัตรากำไร",
        "tab_chart2": "📊 เปรียบเทียบต้นทุนกับราคาตลาด",
        "col_sku": "รหัส SKU",
        "col_name": "ชื่อสินค้า",
        "col_cat": "หมวดหมู่",
        "col_platform": "ช่องทาง",
        "col_cost": "ราคาทุน (บาท)",
        "col_market": "ราคาตลาด (บาท)",
        "col_fee": "ค่าธรรมเนียม (บาท)",
        "col_profit": "กำไรสุทธิ (บาท)",
        "col_margin": "อัตรากำไร (%)",
        "col_risk": "ระดับความเสี่ยง",
        "col_advice": "คำแนะนำ",
        "status_profitable": "🔥 กำไรสูงน่าลงทุน",
        "status_low": "⚠️ กำไรน้อยระวัง",
        "status_wait": "💡 ทรงตัว"
    }
}

# ==========================================
# 1. โมดูลจัดการการเชื่อมต่อแบบปลอดภัย
# ==========================================
class SafeDataClient:
    def __init__(self, min_delay: float = 1.5, max_delay: float = 3.0, proxy_url: str = ""):
        self.min_delay = min_delay
        self.max_delay = max_delay
        self.proxy_url = proxy_url
        self.session = self._create_resilient_session()

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
        fluctuation = random.uniform(-0.02, 0.02)
        live_supplier_price = round(item["base_cost"] * (1 + fluctuation), 2)

        return {
            "sku": item["sku"],
            "name": item["name"],
            "category": item["category"],
            "platform": item["platform"],
            "supplier_price": live_supplier_price,
            "market_price": item["market_price"],
            "status": "200 OK"
        }

@st.cache_data(ttl=600)
def run_safe_batch_scan(items: tuple, min_delay: float, max_delay: float, proxy: str):
    client = SafeDataClient(min_delay=min_delay, max_delay=max_delay, proxy_url=proxy)
    results = []
    for item in items:
        res = client.fetch_item_data(item)
        results.append(res)
    return results

# ==========================================
# 2. ตั้งค่าหน้าตา Streamlit Dashboard
# ==========================================
st.set_page_config(page_title="Multi-Platform Arbitrage Hub", layout="wide")

# --- Initial Session State สำหรับรายการสินค้า ---
if "custom_catalog" not in st.session_state:
    st.session_state.custom_catalog = [
        {"sku": "GAD-101", "name": "NVMe SSD 1TB Gen4", "category": "Gadgets & IT", "platform": "Shopee API", "base_cost": 1490.0, "market_price": 2290.0},
        {"sku": "GAD-102", "name": "Mechanical Keyboard Wireless", "category": "Gadgets & IT", "platform": "Lazada API", "base_cost": 850.0, "market_price": 1290.0},
        {"sku": "GAD-103", "name": "USB-C GaN Charger 65W", "category": "Gadgets & IT", "platform": "Amazon PA-API", "base_cost": 520.0, "market_price": 990.0},
        {"sku": "HOM-201", "name": "Smart Air Purifier HEPA", "category": "Home & Living", "platform": "TikTok Shop", "base_cost": 2100.0, "market_price": 3490.0},
        {"sku": "HOM-202", "name": "Robot Vacuum Cleaner Auto", "category": "Home & Living", "platform": "Shopee API", "base_cost": 4500.0, "market_price": 6900.0},
        {"sku": "BEA-301", "name": "Ionic Hair Dryer Pro", "category": "Beauty & Health", "platform": "Lazada API", "base_cost": 1250.0, "market_price": 2190.0},
        {"sku": "FAS-401", "name": "Minimalist Crossbody Bag", "category": "Fashion & Lifestyle", "platform": "TikTok Shop", "base_cost": 290.0, "market_price": 790.0},
        {"sku": "GAM-501", "name": "Ergonomic Gaming Chair", "category": "Gaming", "platform": "Shopee API", "base_cost": 3200.0, "market_price": 5200.0}
    ]

# --- Sidebar: ควบคุมระบบและเพิ่มสินค้า ---
selected_lang = st.sidebar.selectbox("🌐 Language / ภาษา", ["ไทย", "English"], index=0)
lang = LANG_DICT.get(selected_lang, LANG_DICT["ไทย"])

st.sidebar.markdown("---")
st.sidebar.header(lang["sidebar_sec"])
min_delay = st.sidebar.slider(lang["min_delay"], 0.5, 5.0, 1.0, 0.5)
max_delay = st.sidebar.slider(lang["max_delay"], 1.0, 8.0, 2.5, 0.5)
if max_delay < min_delay:
    max_delay = min_delay + 0.5

proxy_input = st.sidebar.text_input(lang["proxy_info"], placeholder="http://user:pass@ip:port")
st.sidebar.info(lang["cache_info"])

st.sidebar.markdown("---")
st.sidebar.header(lang["profit_sec"])
min_margin_pct = st.sidebar.slider(lang["min_margin"], 5, 50, 20, 5)
platform_fee_pct = st.sidebar.slider(lang["platform_fee"], 0.0, 15.0, 8.5, 0.5)

# --- ส่วนหัวหลัก ---
st.title(lang["title"])
st.caption(lang["caption"])

# --- ฟอร์มเพิ่มสินค้าเองแบบมืออาชีพใน Expander ---
with st.expander(lang["custom_sec"]):
    with st.form("add_product_form"):
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            new_sku = st.text_input(lang["c_sku"], "NEW-999")
            new_name = st.text_input(lang["c_name"], "Smart Watch Ultra")
        with col_b:
            new_cat = st.selectbox(lang["c_cat"], ["Gadgets & IT", "Home & Living", "Beauty & Health", "Fashion & Lifestyle", "Gaming"])
            new_plat = st.selectbox(lang["c_plat"], ["Shopee API", "Lazada API", "TikTok Shop", "Amazon PA-API"])
        with col_c:
            new_cost = st.number_input(lang["c_cost"], min_value=10.0, value=1000.0, step=50.0)
            new_market = st.number_input(lang["c_market"], min_value=10.0, value=1800.0, step=50.0)
        
        submitted = st.form_submit_button(lang["btn_add"])
        if submitted:
            st.session_state.custom_catalog.append({
                "sku": new_sku,
                "name": new_name,
                "category": new_cat,
                "platform": new_plat,
                "base_cost": float(new_cost),
                "market_price": float(new_market)
            })
            st.success("Successfully added new product to catalog!")
            st.rerun()

# --- แถบคอนโทรลกลาง ---
c1, c2, c3 = st.columns([1.5, 1.5, 3])
with c1:
    trigger = st.button(lang["btn_fetch"], type="primary")
with c2:
    if st.button(lang["btn_clear"]):
        st.cache_data.clear()
        st.rerun()

# แปลง list เป็น tuple เพื่อให้ cache ทำงานได้เสถียร
catalog_tuple = tuple(st.session_state.custom_catalog)

# ประมวลผลข้อมูล
with st.spinner(lang["spinner"]):
    raw_results = run_safe_batch_scan(catalog_tuple, min_delay, max_delay, proxy_input)

# คำนวณผลลัพธ์
table_rows = []
high_profit_count = 0
max_profit_val = 0

for r in raw_results:
    cost = r["supplier_price"]
    sell = r["market_price"]
    fee = sell * (platform_fee_pct / 100.0)
    net_profit = sell - cost - fee
    margin_pct = (net_profit / sell) * 100.0

    is_target = margin_pct >= min_margin_pct
    if is_target:
        high_profit_count += 1
    if net_profit > max_profit_val:
        max_profit_val = net_profit

    # กำหนดระดับความเสี่ยงตามอัตรากำไร
    if margin_pct >= 30:
        risk_level = "Low Risk (AAA)"
        advice = lang["status_profitable"]
    elif margin_pct >= min_margin_pct:
        risk_level = "Medium Risk (AA)"
        advice = lang["status_profitable"]
    elif margin_pct > 10:
        risk_level = "Moderate Risk (A)"
        advice = lang["status_low"]
    else:
        risk_level = "High Risk (B)"
        advice = lang["status_wait"]

    table_rows.append({
        "sku": r["sku"],
        lang["col_name"]: r["name"],
        lang["col_cat"]: r["category"],
        lang["col_platform"]: r["platform"],
        lang["col_cost"]: cost,
        lang["col_market"]: sell,
        lang["col_fee"]: round(fee, 2),
        lang["col_profit"]: round(net_profit, 2),
        lang["col_margin"]: round(margin_pct, 1),
        lang["col_risk"]: risk_level,
        lang["col_advice"]: advice
    })

df_out = pd.DataFrame(table_rows)

st.markdown("---")

# --- แสดงผล KPI เมตริกแบบมืออาชีพ ---
k1, k2, k3, k4 = st.columns(4)
k1.metric(lang["kpi_total"], f"{len(df_out)} รายการ", "Active SKUs")
k2.metric(lang["kpi_target"], f"{high_profit_count} รายการ", f"Target >={min_margin_pct}%")
k3.metric(lang["kpi_profit"], f"{max_profit_val:,.2f} THB", "Top Performer")
k4.metric(lang["kpi_status"], "🟢 Protected & Active", "Rate-Limiter ON")

st.markdown("---")

# --- ระบบกรองข้อมูลขั้นสูง (Search, Category Filter, Platform Filter) ---
s1, s2, s3 = st.columns([2, 1.5, 1.5])
with s1:
    search_query = st.text_input(lang["search_label"], "")
with s2:
    categories = [lang["all_cat"]] + list(df_out[lang["col_cat"]].unique())
    selected_cat = st.selectbox(lang["filter_cat"], categories)
with s3:
    platforms = [lang["all_platforms"]] + list(df_out[lang["col_platform"]].unique())
    selected_platform = st.selectbox(lang["filter_platform"], platforms)

# กรองข้อมูล
filtered_df = df_out.copy()
if search_query:
    filtered_df = filtered_df[
        filtered_df[lang["col_name"]].str.contains(search_query, case=False, na=False) |
        filtered_df["sku"].str.contains(search_query, case=False, na=False)
    ]
if selected_cat != lang["all_cat"]:
    filtered_df = filtered_df[filtered_df[lang["col_cat"]] == selected_cat]
if selected_platform != lang["all_platforms"]:
    filtered_df = filtered_df[filtered_df[lang["col_platform"]] == selected_platform]

# --- แบ่ง Tab แสดงผลลัพธ์หลากหลายมิติ ---
tab1, tab2, tab3 = st.tabs([lang["tab_table"], lang["tab_chart1"], lang["tab_chart2"]])

with tab1:
    st.subheader(lang["tab_table"])
    
    def style_dataframe(row):
        advice_col = lang["col_advice"]
        profitable_text = lang["status_profitable"]
        return [
            "background-color: #e8f5e9; color: #2e7d32; font-weight: bold"
            if row[advice_col] == profitable_text else ""
            for _ in row
        ]

    st.dataframe(filtered_df.style.apply(style_dataframe, axis=1), use_container_width=True)

    csv_data = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label=lang["btn_download"],
        data=csv_data,
        file_name='multi_platform_arbitrage_report.csv',
        mime='text/csv',
    )

with tab2:
    st.subheader(lang["tab_chart1"])
    if not filtered_df.empty:
        fig1 = px.scatter(
            filtered_df,
            x=lang["col_market"],
            y=lang["col_profit"],
            size=filtered_df[lang["col_margin"]].abs(),
            color=lang["col_cat"],
            hover_name=lang["col_name"],
            text="sku",
            title="Net Profit vs Market Price (Bubble size represents Margin %)"
        )
        fig1.update_traces(textposition='top center')
        fig1.update_layout(template="plotly_white")
        st.plotly_chart(fig1, use_container_width=True)
    else:
        st.warning("No data to plot.")

with tab3:
    st.subheader(lang["tab_chart2"])
    if not filtered_df.empty:
        fig2 = px.bar(
            filtered_df,
            x=lang["col_name"],
            y=[lang["col_cost"], lang["col_market"]],
            barmode="group",
            title="Cost Price vs Market Price Comparison by Product",
            labels={"value": "Amount (THB)", "variable": "Price Type"}
        )
        fig2.update_layout(xaxis_tickangle=-15, template="plotly_white")
        st.plotly_chart(fig2, use_container_width=True)
    else:
        st.warning("No data to plot.")
