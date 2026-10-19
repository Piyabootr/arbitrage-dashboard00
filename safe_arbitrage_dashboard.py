import streamlit as st
import pandas as pd

# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="Tech & Lifestyle Blog - บทความน่ารู้", layout="wide")

# --- ส่วนจำลองการติดป้ายโฆษณา Google AdSense (Header Banner) ---
st.markdown(
    """
    <div style="background-color: #f0f2f6; padding: 10px; text-align: center; border-radius: 5px; margin-bottom: 20px;">
        <span style="color: gray; font-size: 12px;">[ พื้นที่จำลองป้ายโฆษณา Google AdSense - Display Ad ]</span>
        <h4 style="color: #333; margin: 0;">🔥 โปรโมชันพิเศษประจำวัน คลิกเพื่อดูรายละเอียดเพิ่มเติม!</h4>
    </div>
    """,
    unsafe_allow_html=True
)

# หัวข้อบล็อก
st.title("💡 บทความและสาระน่ารู้ออนไลน์")
st.caption("แหล่งรวมบทความน่าอ่าน ยิ่งมีคนเข้ามาอ่านเยอะ ยิ่งสร้างรายได้จากยอดวิวโฆษณาแบบ Passive Income")

# ฐานข้อมูลบทความตัวอย่าง
articles = [
    {
        "id": 1,
        "title": "5 วิธีประหยัดเงินในยุคดิจิทัลที่คุณก็ทำได้ทันที",
        "category": "การเงิน",
        "read_time": "3 นาที",
        "summary": "เรียนรู้เทคนิคการบริหารเงินง่าย ๆ ที่ช่วยให้คุณเหลือเงินเก็บเพิ่มขึ้นโดยไม่ต้องอด",
        "content": "เนื้อหาบทความฉบับเต็ม: การประหยัดเงินในยุคดิจิทัลเริ่มต้นจากการเช็กแอปพลิเคชันการใช้จ่าย ตัดรายจ่ายที่ไม่จำเป็นออก และตั้งค่าหักเงินเก็บอัตโนมัติทุกครั้งที่เงินเดือนออก..."
    },
    {
        "id": 2,
        "title": "เจาะลึกเทรนด์ AI มาแรงในปี 2026 มีอะไรต้องรู้บ้าง",
        "category": "เทคโนโลยี",
        "read_time": "5 นาที",
        "summary": "อัปเดตเทคโนโลยีปัญญาประดิษฐ์ที่จะเข้ามาเปลี่ยนวิถีชีวิตและการทำงานของเรา",
        "content": "เนื้อหาบทความฉบับเต็ม: เทคโนโลยี AI ในปัจจุบันก้าวไปไกลมาก ทั้งระบบอัตโนมัติ หุ่นยนต์อัจฉริยะ และเครื่องมือช่วยทำงานที่ช่วยประหยัดเวลาได้มากกว่า 50%..."
    },
    {
        "id": 3,
        "title": "ไอเดียแต่งห้องทำงานมินิมอล นั่งทำงานได้ทั้งวันไม่มีเบื่อ",
        "category": "ไลฟ์สไตล์",
        "read_time": "4 นาที",
        "summary": "แชร์ไอเดียจัดโต๊ะทำงานและแต่งห้องโทนสีสบายตา เพิ่ม Productive ให้ตัวเอง",
        "content": "เนื้อหาบทความฉบับเต็ม: การจัดแสงไฟในห้องทำงานและการเลือกใช้โทนสีไม้ธรรมชาติหรือสีขาว จะช่วยลดความเครียดและเพิ่มสมาธิในการทำงานได้เป็นอย่างดี..."
    }
]

# ระบบเลือกบทความ (Sidebar Menu)
st.sidebar.header("📚 หมวดหมู่บทความ")
selected_cat = st.sidebar.selectbox("เลือกหมวดหมู่", ["ทั้งหมด", "การเงิน", "เทคโนโลยี", "ไลฟ์สไตล์"])

# กรองบทความตามหมวดหมู่
filtered_articles = articles
if selected_cat != "ทั้งหมด":
    filtered_articles = [a for a in articles if a['category'] == selected_cat]

# แสดงผลรายการบทความ
for art in filtered_articles:
    with st.container():
        st.subheader(art['title'])
        st.write(f"🏷️ หมวดหมู่: **{art['category']}** | ⏱️ อ่าน: {art['read_time']}")
        st.write(art['summary'])
        
        # ปุ่มกดอ่านบทความแบบเต็ม
        if st.button(f"📖 อ่านบทความเต็ม (ID: {art['id']})", key=f"btn_{art['id']}"):
            st.success(art['content'])
            st.balloons()
            
        st.markdown("---")

# --- ส่วนจำลองการติดป้ายโฆษณา Google AdSense (Footer Banner) ---
st.markdown(
    """
    <div style="background-color: #f0f2f6; padding: 15px; text-align: center; border-radius: 5px; margin-top: 30px;">
        <span style="color: gray; font-size: 12px;">[ พื้นที่จำลองป้ายโฆษณา Google AdSense - In-Article Ad ]</span>
        <p style="margin: 5px 0; font-weight: bold; color: #555;">สนับสนุนเว็บไซต์ของเราโดยการแชร์บทความนี้ให้เพื่อนๆ ของคุณอ่าน!</p>
    </div>
    """,
    unsafe_allow_html=True
)
