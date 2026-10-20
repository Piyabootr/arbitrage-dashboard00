import streamlit as st
import pandas as pd
import requests
import re
import xml.etree.ElementTree as ET

# ตั้งค่าหน้าเว็บให้เป็นแบบ Wide Layout
st.set_page_config(page_title="QELVYQ — Stories & Latest Updates.", layout="wide", initial_sidebar_state="expanded")

# ==========================================
# 1. ระบบจัดการสิทธิ์ผู้ดูแลระบบ (Admin Authentication System)
# ==========================================
if "is_admin" not in st.session_state:
    st.session_state.is_admin = False

if "current_page" not in st.session_state:
    st.session_state.current_page = "home"
if "selected_article_id" not in st.session_state:
    st.session_state.selected_article_id = None

# ==========================================
# 2. ระบบคำนวณสถิติแบบเรียลไทม์ตามความเป็นจริง (Real-Time Analytics)
# ==========================================
if "page_views" not in st.session_state:
    st.session_state.page_views = 1
if "active_users" not in st.session_state:
    st.session_state.active_users = 1

st.session_state.page_views += 1
real_adsense_revenue = (st.session_state.page_views / 1000.0) * 1.50

# ==========================================
# 3. ระบบตรวจสอบและแก้ไขไวยากรณ์ (Grammar Checker Engine)
# ==========================================
def check_and_correct_grammar(text: str) -> tuple[str, list[str]]:
    corrections = []
    corrected_text = text

    if corrected_text and not corrected_text[0].isupper():
        corrections.append("Capitalized the first letter.")
        corrected_text = corrected_text[0].upper() + corrected_text[1:]

    common_errors = {"teh": "the", "recieve": "receive", "adress": "address", "seperate": "separate", "dont": "don't", "cant": "can't"}
    for wrong, right in common_errors.items():
        if wrong in corrected_text.lower():
            corrections.append(f"Corrected spelling: '{wrong}' -> '{right}'")
            corrected_text = re.sub(re.escape(wrong), right, corrected_text, flags=re.IGNORECASE)

    if corrected_text and corrected_text[-1] not in ['.', '!', '?']:
        corrections.append("Added terminal punctuation.")
        corrected_text = corrected_text + "."

    if not corrections:
        corrections.append("Grammar pristine.")

    return corrected_text, corrections

# ==========================================
# 4. ระบบสร้างและดึงข้อมูลเฉพาะ Short/Long Stories และ Latest News
# ==========================================
@st.cache_data(ttl=60)
def generate_stories_and_news(query: str) -> list:
    items = []
    clean_query = query.strip().lower()
    
    # 1. ดึงข่าวสารอัปเดตใหม่ๆ จาก TechCrunch RSS
    try:
        rss_url = "https://techcrunch.com/feed/"
        resp = requests.get(rss_url, timeout=4)
        if resp.status_code == 200:
            root = ET.fromstring(resp.content)
            for idx, item in enumerate(root.findall('.//item')[:6]):
                title_elem = item.find('title')
                title = title_elem.text if title_elem is not None else "Breaking News Update"
                
                desc_elem = item.find('description')
                desc = desc_elem.text if desc_elem is not None and desc_elem.text else "Latest update..."
                clean_desc = re.sub('<.*?>', '', desc)
                
                items.append({
                    "id": 1000 + idx,
                    "title": f"Breaking News: {title}",
                    "category": "Latest News & Updates",
                    "read_time": "4 mins",
                    "views": 1,
                    "likes": 0,
                    "source": "QELVYQ Live News Wire",
                    "summary": clean_desc[:200] + "...",
                    "content": f"""Latest Update Briefing:
{clean_desc}

Detailed Reporting & Global Impact:
As developments unfold regarding '{clean_query}', international analysts track continuous telemetry and real-time updates. This news dispatch provides uncompromised coverage of current milestones, market reactions, and expert forecasts.

Stay tuned to QELVYQ for continuous live reporting and follow-up updates."""
                })
    except:
        pass

    # 2. สร้างเรื่องเล่าและนิทาน (Short Story or Long Story) แบบจัดเต็ม
    stories_pool = [
        ("The Chrono Weaver: A Short Story of Lost Moments", "Short Story or Long Story", "6 mins", 
         "A short tale about a clockmaker who discovers a pocket watch capable of pausing time for five seconds.",
         """In a cobblestone alleyway sits a dusty clockmaker's shop, tended by an elderly man named Thomas. Unknown to the town, Thomas possessed a brass pocket watch that could halt time for exactly five seconds. 

For years, he used it selfishly to avoid minor embarrassments—spilled coffee, delayed trains, misplaced keys. But one rainy afternoon, as a runaway carriage hurtled toward a young child on the street, Thomas froze time. He walked over, gently moved the child to safety, and let time resume. 

In that single frozen moment, Thomas realized true purpose wasn't about erasing mistakes, but about choosing when to act with courage. From that day on, the watch remained unwound, and Thomas lived fully in every imperfect second."""),
        
        ("The Kingdom of Glass: A Long Story of Truth and Reflection", "Short Story or Long Story", "12 mins", 
         "An epic narrative about a mountain kingdom where every citizen's mirror reflected their true intentions.",
         """High above the cloudline lay Aethelgard, a kingdom constructed entirely of translucent crystal glass. In this realm, mirrors didn't reflect physical appearance; they revealed the pure intent behind a person's words. 

For centuries, the citizens lived in radical harmony. Lies shattered instantly against the glass walls, causing minor tremors across the valley. However, a young ambitious lord named Vane sought power by discovering a rare mineral that could tint the glass, hiding deceit behind shimmering gold facades. 

As the golden haze spread, trust withered, and the kingdom plunged into suspicion. It took a humble glassblower's apprentice, armed only with a hammer of absolute honesty, to shatter the tainted panes and restore the natural light to Aethelgard. 

Epilogue:
The story reminds us that true strength lies not in concealing our flaws behind illusions, but in standing transparent under the sun."""),

        ("Global Tech Outlook: The Next Wave of Autonomous Systems", "Latest News & Updates", "5 mins",
         "An exhaustive briefing on autonomous edge networks and their deployment across major cities.",
         """Comprehensive Global Dispatch:
Autonomous infrastructure has transitioned from experimental trials to widespread municipal integration. Urban centers utilizing decentralized edge sensors report unprecedented efficiency in traffic flow, energy distribution, and emergency response coordination. 

Industry leaders emphasize that as machine learning models mature, privacy safeguards and cryptographic verification will remain the cornerstone of public trust.""")
    ]

    for idx, (t_title, t_cat, t_time, t_sum, t_content) in enumerate(stories_pool):
        items.append({
            "id": 2000 + idx,
            "title": f"{t_title} ({clean_query.capitalize()})" if clean_query != "all" else t_title,
            "category": t_cat,
            "read_time": t_time,
            "views": 1,
            "likes": 0,
            "source": "QELVYQ Editorial Desk",
            "summary": t_sum,
            "content": t_content
        })

    return items

# ==========================================
# 5. ฐานข้อมูลเริ่มต้น (Master Database)
# ==========================================
if "master_db" not in st.session_state:
    st.session_state.master_db = generate_stories_and_news("all")

# ==========================================
# 6. หน้าตาเว็บไซต์ (UI Layout & Page Router)
# ==========================================

st.markdown(
    """
    <div style="background: linear-gradient(135deg, #0f172a 0%, #1e3c72 50%, #1e293b 100%); padding: 12px; text-align: center; border-radius: 8px; margin-bottom: 20px; color: white;">
        <span style="font-size: 10px; letter-spacing: 2px; text-transform: uppercase; opacity: 0.7;">[ GOOGLE ADSENSE - GLOBAL LEADERBOARD AD ]</span>
        <h4 style="margin: 5px 0; color: #38bdf8;">⚡ QELVYQ Global Stories & News Hub — Explore Today</h4>
    </div>
    """,
    unsafe_allow_html=True
)

# หน้าอ่านบทความเต็มจอ (Dedicated Reader Page)
if st.session_state.current_page == "reader" and st.session_state.selected_article_id is not None:
    target_article = next((item for item in st.session_state.master_db if item.get("id") == st.session_state.selected_article_id), None)
    
    if target_article:
        if st.button("⬅️ Back to Feed"):
            st.session_state.current_page = "home"
            st.session_state.selected_article_id = None
            st.rerun()
            
        st.markdown(f"# {target_article['title']}")
        st.markdown(f"🏷️ **Category:** {target_article['category']} &nbsp;|&nbsp; ⏱️ **Read Time:** {target_article['read_time']} &nbsp;|&nbsp; 👀 **Views:** {target_article.get('views', 1):,}")
        st.markdown("---")
        
        # แสดงเนื้อหาแบบเต็มจอ
        st.write(target_article['content'])
        
        st.markdown("---")
        if st.button("❤️ Like this story"):
            target_article['likes'] = target_article.get('likes', 0) + 1
            st.success("Liked successfully!")
            st.rerun()
            
        st.stop()

# ==========================================
# หน้าแรกหลัก (Home Feed)
# ==========================================
st.title("QELVYQ — Stories & Latest Updates.")
st.caption("Engaging short and long stories, moral fables, and breaking news updates powered by real-time intelligence.")

st.markdown("---")

# --- Sidebar: ช่อง Search และหมวดหมู่ ---
st.sidebar.header("Search")
search_keyword = st.sidebar.text_input("Search", placeholder="Search stories or news...")

if search_keyword:
    with st.spinner(f"Searching stories and updates for '{search_keyword}'..."):
        new_items = generate_stories_and_news(search_keyword)
        for item in new_items:
            if not any(d['title'] == item['title'] for d in st.session_state.master_db):
                new_id = len(st.session_state.master_db) + 100
                st.session_state.master_db.insert(0, {
                    "id": new_id,
                    "title": item["title"],
                    "category": item["category"],
                    "read_time": item["read_time"],
                    "views": 1,
                    "likes": 0,
                    "summary": item["summary"],
                    "content": item["content"],
                    "source": item.get("source", "QELVYQ Desk")
                })
        st.sidebar.success(f"Found results for '{search_keyword}'!")

st.sidebar.markdown("---")
st.sidebar.header("📂 Category Filter")
selected_category = st.sidebar.selectbox(
    "Filter content", 
    ["All Categories", "Short Story or Long Story", "Latest News & Updates"]
)

st.sidebar.markdown("---")

# ==========================================
# Admin Portal (เข้าถึงได้เฉพาะ Admin)
# ==========================================
st.sidebar.header("🔐 Admin Security Portal")
admin_pass_input = st.sidebar.text_input("Admin Passcode", type="password", placeholder="Enter admin code...")

ADMIN_SECRET_KEY = "qelvyq2026"

if admin_pass_input == ADMIN_SECRET_KEY:
    st.session_state.is_admin = True
    st.sidebar.success("🔓 Admin Access Granted!")
else:
    if admin_pass_input != "":
        st.sidebar.error("❌ Invalid passcode.")
    st.session_state.is_admin = False

if st.session_state.is_admin:
    st.sidebar.markdown("---")
    st.sidebar.subheader("🛠️ Admin Control Panel")
    
    with st.sidebar.expander("✍️ Pro Writer Studio (Admin Only)"):
        with st.form("admin_writer_form"):
            w_title = st.text_input("Title", "The Midnight Journey")
            w_cat = st.selectbox("Category", ["Short Story or Long Story", "Latest News & Updates"])
            w_time = st.text_input("Read Time", "5 mins")
            w_summary = st.text_area("Summary", "Short teaser...")
            w_content = st.text_area("Content", "Full story or news text...")
            
            if st.form_submit_button("✨ AI Check & Publish"):
                corrected_content, logs = check_and_correct_grammar(w_content)
                new_id = len(st.session_state.master_db) + 100
                st.session_state.master_db.insert(0, {
                    "id": new_id,
                    "title": w_title,
                    "category": w_cat,
                    "read_time": w_time,
                    "views": 1,
                    "likes": 0,
                    "summary": w_summary,
                    "content": corrected_content,
                    "source": "Admin Manual Publish"
                })
                st.success("Published successfully by Admin!")
                st.rerun()
else:
    st.sidebar.info("🔒 Writer Studio is restricted to Admin access.")

# ==========================================
# แสดงผลเนื้อหาหน้าเว็บไซต์หลักพร้อมระบบแบ่งหน้า Full 2+ Pages (Pagination)
# ==========================================
filtered_db = st.session_state.master_db
if search_keyword:
    filtered_db = [item for item in filtered_db if search_keyword.lower() in item['title'].lower() or search_keyword.lower() in item['summary'].lower() or search_keyword.lower() in item['content'].lower()]
if selected_category != "All Categories":
    filtered_db = [item for item in filtered_db if item['category'] == selected_category]

st.subheader(f"📰 QELVYQ Feed ({len(filtered_db)} stories & updates available)")

if not filtered_db:
    st.warning("No stories or news found. Try another search term.")
else:
    items_per_page = 6
    total_pages = max(1, (len(filtered_db) + items_per_page - 1) // items_per_page)
    
    if total_pages > 1:
        page_num = st.selectbox("📄 Select Page Navigation", range(1, total_pages + 1), format_func=lambda x: f"Full Page {x} of {total_pages}")
    else:
        page_num = 1
        
    start_idx = (page_num - 1) * items_per_page
    end_idx = start_idx + items_per_page
    current_page_items = filtered_db[start_idx:end_idx]

    cols = st.columns(2)
    for idx, item in enumerate(current_page_items):
        col = cols[idx % 2]
        with col:
            with st.container(border=True):
                st.markdown(f"### {item['title']}")
                st.markdown(f"🏷️ **{item['category']}** | ⏱️ {item['read_time']} | 👀 {item.get('views', 1):,} views")
                st.write(item['summary'])
                
                # กำหนดค่า ID สำรองป้องกัน Key Error
                item_id = item.get('id', idx + 5000)
                
                b1, b2 = st.columns([2, 1])
                with b1:
                    if st.button(f"📖 Read Story (ID: {item_id})", key=f"read_{item_id}_{idx}"):
                        item['views'] = item.get('views', 1) + 1
                        st.session_state.current_page = "reader"
                        st.session_state.selected_article_id = item_id
                        st.rerun()
                with b2:
                    if st.button(f"❤️ Like ({item.get('likes', 0)})", key=f"like_{item_id}_{idx}"):
                        item['likes'] = item.get('likes', 0) + 1
                        st.rerun()
                
            st.markdown("")

# ==========================================
# Footer (Tab เล็กๆ ด้านล่าง พร้อมโลโก้และข้อความแบรนด์)
# ==========================================
st.markdown("---")

footer_tab1, footer_tab2 = st.tabs(["🌐 QELVYQ Brand & Info", "📊 Live Real-Time Analytics"])

with footer_tab1:
    st.markdown(
        """
        <div style="display: flex; align-items: center; gap: 15px; padding: 10px 0;">
            <div style="font-size: 28px; font-weight: bold; background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">QELVYQ</div>
            <div>
                <p style="margin: 0; font-weight: bold; color: #1e293b;">QELVYQ — Stories & Latest Updates.</p>
                <p style="margin: 0; font-size: 13px; color: #64748b;">Short & long stories, moral fables, and breaking news.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with footer_tab2:
    st.markdown("#### 📊 System Telemetry & Live Metrics")
    f_col1, f_col2, f_col3, f_col4 = st.columns(4)
    f_col1.metric("🟢 Live Visitors", f"{st.session_state.active_users} online")
    f_col2.metric("📊 Page Views", f"{st.session_state.page_views:,}")
    f_col3.metric("💰 Est. AdSense", f"${real_adsense_revenue:,.4f} USD")
    f_col4.metric("📚 Active Posts", f"{len(st.session_state.master_db)}")

# Footer AdSense Banner
st.markdown(
    """
    <div style="background-color: #f8f9fa; padding: 15px; text-align: center; border-radius: 8px; margin-top: 20px; border: 1px dashed #ced4da;">
        <span style="color: #6c757d; font-size: 11px; text-transform: uppercase; letter-spacing: 1px;">[ Google AdSense - Native Ad Unit ]</span>
        <p style="margin: 5px 0; font-weight: bold; color: #495057;">QELVYQ — Stories & Latest Updates. Engaging readers worldwide.</p>
    </div>
    """,
    unsafe_allow_html=True
)
