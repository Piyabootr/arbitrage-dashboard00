import streamlit as st
import pandas as pd
import plotly.express as px
import time

# ==========================================
# 0. ระบบพจนานุกรมแปลภาษา (Localization)
# ==========================================
LANG_DICT = {
    "English": {
        "title": "🔥 Daily Best Deal Aggregator Hub",
        "caption": "Your automated platform for curated discounted products, flash sales, and top affiliate earnings.",
        "sidebar_sec": "⚙️ Affiliate Configuration",
        "aff_id": "Your Affiliate ID / Tracking Code",
        "min_disc": "Minimum Discount Filter (%)",
        "search_label": "🔍 Search Deals by Name or SKU",
        "filter_cat": "Filter by Category",
        "all_cat": "All Categories",
        "filter_plat": "Filter by Platform",
        "all_plat": "All Platforms",
        "kpi_total": "Total Active Deals",
        "kpi_high": "High Discount (>30%)",
        "kpi_max": "Max Savings Available",
        "tab_grid": "🛍️ Deal Showcase",
        "tab_table": "📋 Master Table View",
        "tab_chart": "📊 Discount Analysis Chart",
        "btn_buy": "🛒 Buy Now (Earn Commission)",
        "badge_disc": "DISCOUNT",
        "footer": "💡 Tip: Share your personalized links on social media to earn automated commissions without holding stock."
    },
    "ไทย": {
        "title": "🔥 เว็บไซต์รวบรวมดีลและสินค้าลดราคารายวัน",
        "caption": "แพลตฟอร์มรวบรวมสินค้าแฟลชเซลและดีลเด็ดประจำวัน พร้อมระบบสร้างลิงก์นายหน้าอัตโนมัติ",
        "sidebar_sec": "⚙️ ตั้งค่าระบบ Affiliate",
        "aff_id": "รหัส Affiliate ID ของคุณ (เช่น my_shop_001)",
        "min_disc": "กรองส่วนลดขั้นต่ำ (%)",
        "search_label": "🔍 ค้นหาดีลสินค้า หรือรหัส SKU",
        "filter_cat": "กรองตามหมวดหมู่",
        "all_cat": "ทุกหมวดหมู่",
        "filter_plat": "กรองตามแพลตฟอร์ม",
        "all_plat": "ทุกแพลตฟอร์ม",
        "kpi_total": "ดีลทั้งหมดในระบบ",
        "kpi_high": "ดีลลดแรง (>30%)",
        "kpi_max": "ส่วนลดสูงสุดในระบบ",
        "tab_grid": "🛍️ แกลเลอรีดีลเด็ด",
        "tab_table": "📋 ตารางสรุปข้อมูลดีล",
        "tab_chart": "📊 กราฟวิเคราะห์ส่วนลด",
        "btn_buy": "🛒 สั่งซื้อสินค้า (สร้างรายได้)",
        "badge_disc": "ส่วนลด",
        "footer": "💡 คำแนะนำ: คัดลอกลิงก์ไปแชร์ลงโซเชียลเพื่อสร้างรายได้แบบ Passive Income โดยไม่ต้องสต็อกสินค้า"
    }
}

# ==========================================
# 1. ตั้งค่าหน้าเว็บ Streamlit
# ==========================================
st.set_page_config(page_title="Deal Aggregator Hub", layout="wide")

# --- Sidebar: ตั้งค่าระบบภาษาและ Affiliate ID ---
selected_lang = st.sidebar.selectbox("🌐 Language / ภาษา", ["ไทย", "English"], index=0)
lang = LANG_DICT.get(selected_lang, LANG_DICT["ไทย"])

st.sidebar.markdown("---")
st.sidebar.header(lang["sidebar_sec"])
user_aff_id = st.sidebar.text_input(lang["aff_id"], "my_affiliate_id_99")
min_discount_filter = st.sidebar.slider(lang["min_disc"], 0, 50, 20, 5)

# --- ฐานข้อมูลดีลสินค้าตัวอย่าง (สามารถเพิ่มเองได้ตลอด) ---
if "deals_catalog" not in st.session_state:
    st.session_state.deals_catalog = [
        {"sku": "DEAL-001", "name": "Wireless Noise Cancelling Earbuds Pro", "category": "Gadgets & IT", "platform": "Shopee", "original_price": 1590.0, "sale_price": 990.0, "image_url": "https://images.unsplash.com/photo-1590658268037-6bf12165a8df?w=500"},
        {"sku": "DEAL-002", "name": "Smart Watch Fitness & Heart Rate", "category": "Gadgets & IT", "platform": "Lazada", "original_price": 2490.0, "sale_price": 1490.0, "image_url": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=500"},
        {"sku": "DEAL-003", "name": "Minimalist Crossbody Canvas Bag", "category": "Fashion", "platform": "TikTok Shop", "original_price": 690.0, "sale_price": 350.0, "image_url": "https://images.unsplash.com/photo-1544816155-12df9643f363?w=500"},
        {"sku": "DEAL-004", "name": "Automatic Robotic Vacuum Cleaner", "category": "Home & Living", "platform": "Shopee", "original_price": 4900.0, "sale_price": 2990.0, "image_url": "https://images.unsplash.com/photo-1589939705384-5185137a7f0f?w=500"},
        {"sku": "DEAL-005", "name": "Ergonomic Office Chair Mesh", "category": "Home & Living", "platform": "Lazada", "original_price": 3500.0, "sale_price": 2190.0, "image_url": "https://images.unsplash.com/photo-1580481077494-e3299ac25e94?w=500"},
        {"sku": "DEAL-006", "name": "Collagen Peptide Premium Formula", "category": "Beauty & Health", "platform": "TikTok Shop", "original_price": 1200.0, "sale_price": 690.0, "image_url": "https://images.unsplash.com/photo-1584308666744-24d5c474f2ae?w=500"}
    ]

# --- ส่วนหัวหลักของเว็บไซต์ ---
st.title(lang["title"])
st.caption(lang["caption"])
st.markdown("---")

# --- คำนวณส่วนลดและอัตราประหยัดของแต่ละดีล ---
processed_deals = []
for d in st.session_state.deals_catalog:
    orig = d["original_price"]
    sale = d["sale_price"]
    discount_pct = round(((orig - sale) / orig) * 100, 1)
    savings = orig - sale
    
    # สร้างลิงก์พ่วง Affiliate ID อัตโนมัติ
    aff_link = f"https://marketplace-sample.com/product/{d['sku']}?aff_id={user_aff_id}"

    processed_deals.append({
        "sku": d["sku"],
        "name": d["name"],
        "category": d["category"],
        "platform": d["platform"],
        "original_price": orig,
        "sale_price": sale,
        "discount_pct": discount_pct,
        "savings": savings,
        "image_url": d["image_url"],
        "aff_link": aff_link
    })

df_deals = pd.DataFrame(processed_deals)

# --- แผงควบคุมการค้นหาและกรองข้อมูล ---
col_s1, col_s2, col_s3 = st.columns([2, 1.5, 1.5])
with col_s1:
    search_text = st.text_input(lang["search_label"], "")
with col_s2:
    cats = [lang["all_cat"]] + list(df_deals["category"].unique())
    selected_cat = st.selectbox(lang["filter_cat"], cats)
with col_s3:
    plats = [lang["all_plat"]] + list(df_deals["platform"].unique())
    selected_plat = st.selectbox(lang["filter_plat"], plats)

# กรองข้อมูลตามเงื่อนไข
filtered_df = df_deals[df_deals["discount_pct"] >= min_discount_filter]
if search_text:
    filtered_df = filtered_df[
        filtered_df["name"].str.contains(search_text, case=False, na=False) |
        filtered_df["sku"].str.contains(search_text, case=False, na=False)
    ]
if selected_cat != lang["all_cat"]:
    filtered_df = filtered_df[filtered_df["category"] == selected_cat]
if selected_plat != lang["all_plat"]:
    filtered_df = filtered_df[filtered_df["platform"] == selected_plat]

# --- แสดงผล KPI เมตริกด้านบน ---
k1, k2, k3 = st.columns(3)
k1.metric(lang["kpi_total"], f"{len(filtered_df)} ดีล", "Active Deals")
high_disc_count = len(filtered_df[filtered_df["discount_pct"] >= 30])
k2.metric(lang["kpi_high"], f"{high_disc_count} ดีล", "Discount >= 30%")
max_saving = filtered_df["savings"].max() if not filtered_df.empty else 0
k3.metric(lang["kpi_max"], f"{max_saving:,.0f} THB", "Best Saving")

st.markdown("---")

# --- แบ่งหน้าเว็บไซต์เป็น แท็บ (Tabs) ---
tab_grid, tab_table, tab_chart = st.tabs([lang["tab_grid"], lang["tab_table"], lang["tab_chart"]])

# 1. แท็บแกลเลอรีดีลเด็ด (Product Grid Cards)
with tab_grid:
    if not filtered_df.empty:
        # แสดงผลแบบ 3 คอลัมน์สวยงามเหมือนเว็บช้อปปิ้ง
        cols = st.columns(3)
        for idx, row in filtered_df.reset_index(drop=True).iterrows():
            col_target = cols[idx % 3]
            with col_target:
                st.image(row["image_url"], use_container_width=True)
                st.markdown(f"**{row['name']}**")
                st.caption(f"📁 {row['category']} | 🛒 {row['platform']}")
                st.markdown(f"🔥 <span style='color:red; font-size:18px;'><b>฿{row['sale_price']:,.0f}</b></span> &nbsp; <del style='color:gray;'>฿{row['original_price']:,.0f}</del>", unsafe_allow_html=True)
                st.markdown(f"⚡ ประหยัดทันที **฿{row['savings']:,.0f}** ({row['discount_pct']}%)")
                st.link_button(lang["btn_buy"], row["aff_link"], use_container_width=True)
                st.markdown("---")
    else:
        st.warning("ไม่พบสินค้าที่ตรงกับเงื่อนไขการค้นหา")

# 2. แท็บตารางสรุปข้อมูล
with tab_table:
    st.subheader(lang["tab_table"])
    display_table = filtered_df[["sku", "name", "category", "platform", "original_price", "sale_price", "discount_pct", "aff_link"]]
    st.dataframe(display_table, use_container_width=True)

# 3. แท็บกราฟวิเคราะห์ส่วนลด
with tab_chart:
    st.subheader(lang["tab_chart"])
    if not filtered_df.empty:
        fig = px.bar(
            filtered_df,
            x="name",
            y="discount_pct",
            color="platform",
            text="discount_pct",
            title="Discount Percentage (%) Distribution by Product",
            labels={"discount_pct": "Discount (%)", "name": "Product"}
        )
        fig.update_traces(texttemplate='%{text}%', textposition='outside')
        fig.update_layout(xaxis_tickangle=-15, template="plotly_white")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("ไม่มีข้อมูลสำหรับสร้างกราฟ")

st.markdown("---")
st.caption(lang["footer"])
