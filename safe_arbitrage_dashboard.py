import streamlit as st
import pandas as pd

# ตั้งค่าหน้าเว็บให้เป็นแบบ Wide Layout
st.set_page_config(page_title="Pro Blog & AdSense Hub", layout="wide")

# --- Initial Session State สำหรับบทความ ---
if "articles_db" not in st.session_state:
    st.session_state.articles_db = [
        {
            "id": 1,
            "title": "5 วิธีประหยัดเงินในยุคดิจิทัลที่คุณก็ทำได้ทันที",
            "category": "การเงิน",
            "read_time": "3 นาที",
            "views": 1420,
            "likes": 85,
            "summary": "เรียนรู้เทคนิคการบริหารเงินง่าย ๆ ที่ช่วยให้คุณเหลือเงินเก็บเพิ่มขึ้นโดยไม่ต้องอด",
            "content": "เนื้อหาบทความฉบับเต็ม: การประหยัดเงินในยุคดิจิทัลเริ่มต้นจากการเช็กแอปพลิเคชันการใช้จ่าย ตัดรายจ่ายที่ไม่จำเป็นออก และตั้งค่าหักเงินเก็บอัตโนมัติทุกครั้งที่เงินเดือนออก..."
        },
        {
            "id": 2,
            "title": "เจาะลึกเทรนด์ AI มาแรงในปี 2026 มีอะไรต้องรู้บ้าง",
            "category": "เทคโนโลยี",
            "read_time": "5 นาที",
            "views": 3890,
            "likes": 240,
            "summary": "อัปเดตเทคโนโลยีปัญญาประดิษฐ์ที่จะเข้ามาเปลี่ยนวิถีชีวิตและการทำงานของเรา",
            "content": "เนื้อหาบทความฉบับเต็ม: เทคโนโลยี AI ในปัจจุบันก้าวไปไกลมาก ทั้งระบบอัตโนมัติ หุ่นยนต์อัจฉริยะ และเครื่องมือช่วยทำงานที่ช่วยประหยัดเวลาได้มากกว่า 50%..."
        },
        {
            "id": 3,
            "title": "ไอเดียแต่งห้องทำงานมินิมอล นั่งทำงานได้ทั้งวันไม่มีเบื่อ",
            "category": "ไลฟ์สไตล์",
            "read_time": "4 นาที",
            "views": 2150,
            "likes": 112,
            "summary": "แชร์ไอเดียจัดโต๊ะทำงานและแต่งห้องโทนสีสบายตา เพิ่ม Productive ให้ตัวเอง",
            "content": "เนื้อหาบทความฉบับเต็ม: การจัดแสงไฟในห้องทำงานและการเลือกใช้โทนสีไม้ธรรมชาติหรือสีขาว จะช่วยลดความเครียดและเพิ่มสมาธิในการทำงานได้เป็นอย่างดี..."
        },
        {
            "id": 4,
            "title": "เคล็ดลับดูแลสุขภาพฉบับคนทำงานนั่งโต๊ะ (Office Syndrome)",
            "category": "สุขภาพ",
            "read_time": "4 นาที",
            "views": 950,
            "likes": 45,
            "summary": "ท่าบริหารร่างกายง่ายๆ คลายอาการปวดหลังและคอบ่าไหล่ระหว่างวัน",
            "content": "เนื้อหาบทความฉบับเต็ม: การนั่งทำงานหน้าจอคอมพิวเตอร์นานเกินไปทำให้เกิดอาการกล้ามเนื้ออักเสบเรื้อรัง ควรลุกขึ้นยืดเหยียดกล้ามเนื้อทุกๆ 1 ชั่วโมง..."
        }
    ]

# --- แถบจำลองป้ายโฆษณา Google AdSense (Top Banner) ---
st.markdown(
    """
    <div style="background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); padding: 12px; text-align: center; border-radius: 8px; margin-bottom: 20px; border: 1px dashed #a0aec0;">
        <span style="color: #718096; font-size: 11px; text-transform: uppercase; letter-spacing: 1px;">[ Google AdSense - Responsive Leaderboard Ad ]</span>
        <h4 style="color: #2d3748; margin: 5px 0;">🔥 แพ็กเกจเครื่องมือสร้างรายได้ออนไลน์ สมัครวันนี้รับโบนัสพิเศษฟรี!</h4>
    </div>
    """,
    unsafe_allow_html=True
)

# --- ส่วนหัวหลักของเว็บไซต์ ---
st.title("💡 Pro Blog & Content Intelligence Hub")
st.caption("แพลตฟอร์มบทความคุณภาพสูง ระบบวิเคราะห์ยอดวิว และพื้นที่สร้างรายได้จาก Google AdSense แบบ Passive Income")

st.markdown("---")

# --- แถบสถิติภาพรวมเว็บไซต์ (Analytics Metric Cards) ---
total_views = sum([a["views"] for a in st.session_state.articles_db])
total_likes = sum([a["likes"] = = a.get("likes", 0) for a in st.session_state.articles_db]) # safety sum
estimated_earnings = total_views * 0.05  # จำลองรายได้เฉลี่ย 0.05 บาทต่อวิว

m1, m2, m3, m4 = st.columns(4)
m1.metric("📊 ยอดเข้าชมรวม (Total Views)", f"{total_views:,} วิว", "+12% สัปดาห์นี้")
m2.metric("❤️ ยอดถูกใจรวม (Total Likes)", f"{total_likes:,} ไลฟ์", "Engagement สูง")
m3.metric("💰 รายได้ AdSense ประเมิน", f"{estimated_earnings:,.2f} THB", "Passive Income")
m4.metric("📚 บทความทั้งหมด", f"{len(st.session_state.articles_db)} เรื่อง", "Active Posts")

st.markdown("---")

# --- Sidebar: ค้นหาและหมวดหมู่ ---
st.sidebar.header("🔍 ค้นหาและกรองข้อมูล")
search_query = st.sidebar.text_input("ค้นหาชื่อบทความ", "")
selected_cat = st.sidebar.selectbox("📂 เลือกหมวดหมู่บทความ", ["ทั้งหมด", "การเงิน", "เทคโนโลยี", "ไลฟ์สไตล์", "สุขภาพ"])

st.sidebar.markdown("---")
# --- ฟอร์มเพิ่มบทความใหม่ (เขียนบล็อกเองได้สดๆ) ---
with st.sidebar.expander("✍️ เขียนบทความใหม่"):
    with st.form("new_article_form"):
        new_title = st.text_input("หัวข้อบทความ", "เทคนิคลงทุนฉบับมือใหม่")
        new_cat = st.selectbox("หมวดหมู่", ["การเงิน", "เทคโนโลยี", "ไลฟ์สไตล์", "สุขภาพ"])
        new_time = st.text_input("เวลาที่ใช้, อ่าน", "3 นาที")
        new_summary = st.text_area("คำโปรยย่อ", "สรุปสาระสำคัญสั้นๆ...")
        new_content = st.text_area("เนื้อหาบทความเต็ม", "รายละเอียดเนื้อหา...")
        
        submitted = st.form_submit_button("เผยแพร่บทความ")
        if submitted:
            new_id = len(st.session_state.articles_db) + 1
            st.session_state.articles_db.insert(0, {
                "id": new_id,
                "title": new_title,
                "category": new_cat,
                "read_time": new_time,
                "views": 1,
                "likes": 0,
                "summary": new_summary,
                "content": new_content
            })
            st.success("เผยแพร่บทความสำเร็จ!")
            st.rerun()

# --- กรองข้อมูลบทความตามการค้นหาและหมวดหมู่ ---
filtered_articles = st.session_state.articles_db
if search_query:
    filtered_articles = [a for a in filtered_articles if search_query.lower() in a['title'].lower() or search_query.lower() in a['summary'].lower()]
if selected_cat != "ทั้งหมด":
    filtered_articles = [a for a in filtered_articles if a['category'] == selected_cat]

# --- แสดงผลบทความแบบ Grid (2 คอลัมน์ ดูทันสมัย) ---
st.subheader("📰 บทความแนะนำล่าสุด")

if not filtered_articles:
    st.warning("ไม่พบบทความที่ค้นหา กรุณาลองใหม่อีกครั้ง")
else:
    cols = st.columns(2)
    for idx, art in enumerate(filtered_articles):
        col = cols[idx % 2]
        with col:
            # ใช้ container สร้างการ์ดบทความที่ดูสะอาดตา
            with st.container(border=True):
                st.markdown(f"### {art['title']}")
                st.markdown(f"🏷️ **{art['category']}** &nbsp;|&nbsp; ⏱️ อ่าน: {art['read_time']} &nbsp;|&nbsp; 👀 {art['views']:,} วิว")
                st.write(art['summary'])
                
                # ปุ่มกดอ่านและปุ่มกดไลก์
                b1, b2 = st.columns([2, 1])
                with b1:
                    if st.button(f"📖 อ่านต่อ (ID: {art['id']})", key=f"read_{art['id']}
