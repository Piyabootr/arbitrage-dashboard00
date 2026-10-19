import streamlit as st
import pandas as pd

# ตั้งค่าหน้าเว็บให้เป็นแบบ Wide Layout
st.set_page_config(page_title="Pro Content & Stories Hub", layout="wide")

# ==========================================
# 0. พจนานุกรมแปลภาษา (Localization / Dictionary)
# ==========================================
LANG_DICT = {
    "English": {
        "title": "💡 Pro Content, Knowledge & Stories Hub",
        "caption": "Professional blogging platform featuring real knowledge articles, moral fairy tales, and automated AdSense analytics.",
        "top_banner": "🔥 Special Promotion: Boost your online earnings today with our exclusive toolkits!",
        "stat_views": "Total Views",
        "stat_likes": "Total Likes",
        "stat_earnings": "Est. AdSense Earnings",
        "stat_posts": "Total Posts",
        "sidebar_search": "🔍 Search & Filter",
        "search_label": "Search title or content",
        "cat_label": "📂 Select Category",
        "all_cat": "All Categories",
        "cat_knowledge": "Knowledge & Tech",
        "cat_stories": "Fairy Tales & Stories",
        "cat_finance": "Finance & Business",
        "write_expander": "✍️ Publish New Post",
        "w_title": "Post Title",
        "w_cat": "Category",
        "w_time": "Reading Time",
        "w_summary": "Short Summary",
        "w_content": "Full Content",
        "w_btn": "Publish Content",
        "success_msg": "Content published successfully!",
        "section_title": "📰 Recommended Articles & Stories",
        "btn_read": "📖 Read Full Story",
        "btn_like": "❤️ Like",
        "footer_banner": "Support our platform by sharing these insightful articles and stories with your friends!"
    },
    "ไทย": {
        "title": "💡 ศูนย์รวมบทความสาระน่ารู้และนิทานออนไลน์ (Pro Hub)",
        "caption": "แพลตฟอร์มบล็อกระดับมืออาชีพ รวบรวมบทความสาระความรู้จริง นิทานสอนใจ และระบบวิเคราะห์รายได้ AdSense แบบเรียลไทม์",
        "top_banner": "🔥 โปรโมชันพิเศษประจำวัน: ยกระดับรายได้ออนไลน์ของคุณด้วยแพ็กเกจเครื่องมืออัจฉริยะ!",
        "stat_views": "ยอดเข้าชมรวม",
        "stat_likes": "ยอดถูกใจรวม",
        "stat_earnings": "รายได้ AdSense ประเมิน",
        "stat_posts": "บทความและนิทานทั้งหมด",
        "sidebar_search": "🔍 ค้นหาและกรองข้อมูล",
        "search_label": "ค้นหาชื่อเรื่องหรือเนื้อหา",
        "cat_label": "📂 เลือกหมวดหมู่",
        "all_cat": "ทั้งหมด",
        "cat_knowledge": "สาระน่ารู้ & เทคโนโลยี",
        "cat_stories": "นิทาน & เรื่องเล่าสอนใจ",
        "cat_finance": "การเงิน & ธุรกิจ",
        "write_expander": "✍️ เขียนบทความหรือนิทานใหม่",
        "w_title": "หัวข้อเรื่อง",
        "w_cat": "หมวดหมู่",
        "w_time": "เวลาที่ใช้ในการอ่าน",
        "w_summary": "คำโปรยย่อ (Summary)",
        "w_content": "เนื้อหาเต็ม (Full Content)",
        "w_btn": "เผยแพร่ผลงาน",
        "success_msg": "เผยแพร่เนื้อหาสำเร็จเรียบร้อย!",
        "section_title": "📰 บทความและนิทานแนะนำล่าสุด",
        "btn_read": "📖 อ่านเนื้อหาเต็ม",
        "btn_like": "❤️ ถูกใจ",
        "footer_banner": "สนับสนุนเว็บไซต์ของเราโดยการแชร์บทความหรือนิทานดีๆ นี้ให้คนที่คุณรักอ่าน!"
    }
}

# --- Sidebar: เลือกภาษา ---
selected_lang = st.sidebar.selectbox("🌐 Language / ภาษา", ["ไทย", "English"], index=0)
lang = LANG_DICT.get(selected_lang, LANG_DICT["ไทย"])

# --- Initial Session State สำหรับบทความและนิทาน (เนื้อหาจริง) ---
if "articles_db" not in st.session_state:
    st.session_state.articles_db = [
        {
            "id": 1,
            "title": "นิทานอีสป: ราชสีห์กับหนู (The Lion and the Mouse)",
            "category": "นิทาน & เรื่องเล่าสอนใจ",
            "read_time": "3 นาที",
            "views": 3420,
            "likes": 412,
            "summary": "นิทานคลาสสิกสอนใจว่า 'คนตัวเล็กก็อาจมีประโยชน์ต่อคนตัวใหญ่ได้ในยามคับขัน'",
            "content": "กาลครั้งหนึ่งนานมาแล้ว มีราชสีห์ตัวใหญ่หลับพักผ่อนอยู่ในป่า มีหนูตัวน้อยวิ่งมาไต่บนหลังของราชสีห์จนมันตื่นขึ้นมาด้วยความโกรธและใช้กรงเล็บตะปบไว้ หนูจึงร้องขอชีวิตและสัญญาว่า หากรอดไปได้จะตอบแทนบุญคุณแน่นอน ราชสีห์หัวเราะและปล่อยตัวไป ต่อมาไม่นาน ราชสีห์ติดตาข่ายนายพราน ร้องคำรามลั่นป่า หนูตัวน้อยได้ยินจึงรีบวิ่งมาแทะเชือกตาข่ายจนขาด ทำให้ราชสีห์รอดชีวิตมาได้ นิทานเรื่องนี้สอนให้รู้ว่า: เมตตาธรรมค้ำจุนโลก และไม่มีใครเล็กเกินกว่าที่จะช่วยเหลือผู้อื่น"
        },
        {
            "id": 2,
            "title": "5 สาระน่ารู้รอบตัว: ทำไมเราถึงหาวเมื่อเห็นคนอื่นหาว?",
            "category": "สาระน่ารู้ & เทคโนโลยี",
            "read_time": "4 นาที",
            "views": 5120,
            "likes": 680,
            "summary": "ไขข้อข้องใจทางวิทยาศาสตร์ว่าทำไมอาการ 'หาว' ถึงแพร่เชื้อใส่กันได้รวดเร็วนัก",
            "content": "อาการหาวติดต่อกัน (Contagious Yawning) เป็นปรากฏการณ์ทางชีววิทยาที่เกี่ยวข้องกับ 'ความเห็นอกเห็นใจ' (Empathy) และระบบเซลล์ประสาทกระจกเงา (Mirror Neurons) ในสมอง เมื่อเราเห็นคนอื่นหาว สมองส่วนที่ควบคุมความรู้สึกร่วมจะทำงานกระตุ้นให้เราหาวตามโดยอัตโนมัติ ซึ่งมักเกิดขึ้นกับคนใกล้ชิดหรือคนที่มีความผูกพันกันสูง นอกจากนี้ยังเป็นกลไกช่วยปรับอุณหภูมิในสมองให้ตื่นตัวอยู่เสมออีกด้วย"
        },
        {
            "id": 3,
            "title": "นิทานสอนใจ: เด็กเลี้ยงแกะผู้สูญเสียความน่าเชื่อถือ",
            "category": "นิทาน & เรื่องเล่าสอนใจ",
            "read_time": "4 นาที",
            "views": 2890,
            "likes": 310,
            "summary": "เรื่องราวเตือนใจเกี่ยวกับการพูดโกหกและผลกระทบที่ตามมาเมื่อไม่มีใครเชื่อใจอีก",
            "content": "เด็กชายเลี้ยงแกะคนหนึ่งนึกสนุก อยากแกล้งชาวบ้านจึงตะโกนลั่นว่า 'ช่วยด้วย! หมาป่ามากินแกะแล้ว!' ชาวบ้านรีบวิ่งถือไม้มาช่วยแต่กลับพบว่าเด็กชายหัวเราะชอบใจที่หลอกได้สำเร็จ วันต่อมาเขาทำแบบเดิมอีก ชาวบ้านก็เริ่มไม่พอใจ จนกระทั่งวันหนึ่งมีหมาป่าบุกมาจริงๆ เขาร้องตะโกนขอความช่วยเหลือสุดเสียง แต่ไม่มีชาวบ้านคนไหนออกมาช่วยเลยเพราะคิดว่าเขาโกหกอีก แกะจึงถูกหมาป่ากินจนหมดฝูง นิทานเรื่องนี้สอนให้รู้ว่า: คนโกหกย่อมไม่มีใครเชื่อถือ แม้ในเวลาที่เขาพูดความจริง"
        },
        {
            "id": 4,
            "title": "เทคนิคบริหารการเงินฉบับคนรุ่นใหม่: กฎ 50/30/20",
            "category": "การเงิน & ธุรกิจ",
            "read_time": "5 นาที",
            "views": 4150,
            "likes": 520,
            "summary": "วิธีแบ่งเงินเดือนง่ายๆ ที่ช่วยให้คุณมีเงินเก็บและอิสรภาพทางการเงินโดยไม่เครียด",
            "content": "กฎการจัดสรรเงิน 50/30/20 คิดค้นโดย Elizabeth Warren เป็นแนวทางแบ่งรายได้สุทธิออกเป็น 3 ส่วนหลัก: 1) 50% สำหรับค่าใช้จ่ายจำเป็น (ค่าเช่าบ้าน, ค่าอาหาร, ค่าเดินทาง) 2) 30% สำหรับความสุขส่วนตัว (ช้อปปิ้ง, ท่องเที่ยว, สังสรรค์) และ 3) 20% สำหรับการออมเงินและลงทุนเพื่ออนาคต การบริหารตามสัดส่วนนี้ช่วยให้ชีวิตมีความสมดุลและสร้างความมั่งคั่งได้ระยะยาว"
        }
    ]

# --- แถบจำลองป้ายโฆษณา Google AdSense (Top Banner) ---
st.markdown(
    f"""
    <div style="background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); padding: 12px; text-align: center; border-radius: 8px; margin-bottom: 20px; border: 1px dashed #a0aec0;">
        <span style="color: #718096; font-size: 11px; text-transform: uppercase; letter-spacing: 1px;">[ Google AdSense - Responsive Leaderboard Ad ]</span>
        <h4 style="color: #2d3748; margin: 5px 0;">{lang['top_banner']}</h4>
    </div>
    """,
    unsafe_allow_html=True
)

# --- ส่วนหัวหลักของเว็บไซต์ ---
st.title(lang["title"])
st.caption(lang["caption"])

st.markdown("---")

# --- แถบสถิติภาพรวมเว็บไซต์ (Analytics Metric Cards) ---
total_views = sum([a["views"] for a in st.session_state.articles_db])
total_likes = sum([a.get("likes", 0) for a in st.session_state.articles_db])
estimated_earnings = total_views * 0.05  # จำลองรายได้ 0.05 บาทต่อวิว

m1, m2, m3, m4 = st.columns(4)
m1.metric(lang["stat_views"], f"{total_views:,} วิว", "+15% สัปดาห์นี้")
m2.metric(lang["stat_likes"], f"{total_likes:,} ไลฟ์", "Engagement สูง")
m3.metric(lang["stat_earnings"], f"{estimated_earnings:,.2f} THB", "Passive Income")
m4.metric(lang["stat_posts"], f"{len(st.session_state.articles_db)} เรื่อง", "Active Posts")

st.markdown("---")

# --- Sidebar: ค้นหาและหมวดหมู่ ---
st.sidebar.header(lang["sidebar_search"])
search_query = st.sidebar.text_input(lang["search_label"], "")
selected_cat = st.sidebar.selectbox(lang["cat_label"], [lang["all_cat"], lang["cat_knowledge"], lang["cat_stories"], lang["cat_finance"]])

st.sidebar.markdown("---")

# --- ฟอร์มเพิ่มบทความหรือนิทานใหม่ ---
with st.sidebar.expander(lang["write_expander"]):
    with st.form("new_post_form"):
        new_title = st.text_input(lang["w_title"], "นิทานกระต่ายกับเต่า ภาคใหม่")
        new_cat = st.selectbox(lang["w_cat"], [lang["cat_knowledge"], lang["cat_stories"], lang["cat_finance"]])
        new_time = st.text_input(lang["w_time"], "3 นาที")
        new_summary = st.text_area(lang["w_summary"], "สรุปย่อสั้นๆ...")
        new_content = st.text_area(lang["w_content"], "เนื้อหาเต็ม...")
        
        submitted = st.form_submit_button(lang["w_btn"])
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
            st.success(lang["success_msg"])
            st.rerun()

# --- กรองข้อมูลตามการค้นหาและหมวดหมู่ ---
filtered_posts = st.session_state.articles_db
if search_query:
    filtered_posts = [p for p in filtered_posts if search_query.lower() in p['title'].lower() or search_query.lower() in p['summary'].lower()]
if selected_cat != lang["all_cat"]:
    filtered_posts = [p for p in filtered_posts if p['category'] == selected_cat]

# --- แสดงผลเนื้อหาแบบ Grid (2 คอลัมน์ ทันสมัย) ---
st.subheader(lang["section_title"])

if not filtered_posts:
    st.warning("ไม่พบเนื้อหาที่ค้นหา กรุณาลองใหม่อีกครั้ง")
else:
    cols = st.columns(2)
    for idx, post in enumerate(filtered_posts):
        col = cols[idx % 2]
        with col:
            with st.container(border=True):
                st.markdown(f"### {post['title']}")
                st.markdown(f"🏷️ **{post['category']}** &nbsp;|&nbsp; ⏱️ {post['read_time']} &nbsp;|&nbsp; 👀 {post['views']:,} วิว")
                st.write(post['summary'])
                
                b1, b2 = st.columns([2, 1])
                with b1:
                    if st.button(f"{lang['btn_read']} (ID: {post['id']})", key=f"read_{post['id']}"):
                        st.info(post['content'])
                with b2:
                    if st.button(f"{lang['btn_like']} ({post['likes']})", key=f"like_{post['id']}"):
                        post['likes'] += 1
                        st.rerun()
                
            st.markdown("")

# --- แถบจำลองป้ายโฆษณา Google AdSense (Footer Banner) ---
st.markdown(
    f"""
    <div style="background-color: #f0f2f6; padding: 15px; text-align: center; border-radius: 8px; margin-top: 30px; border: 1px dashed #cbd5e0;">
        <span style="color: #718096; font-size: 11px; text-transform: uppercase; letter-spacing: 1px;">[ Google AdSense - In-Article Native Ad ]</span>
        <p style="margin: 5px 0; font-weight: bold; color: #4a5568;">{lang['footer_banner']}</p>
    </div>
    """,
    unsafe_allow_html=True
)
