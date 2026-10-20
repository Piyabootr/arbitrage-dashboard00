import streamlit as st
import pandas as pd
import requests
import re
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime

# ตั้งค่าหน้าเว็บให้เป็นแบบ Wide Layout
st.set_page_config(page_title="QELVYQ — Knowledge in Real Time.", layout="wide", initial_sidebar_state="expanded")

# ==========================================
# 1. ระบบจัดการสถานะหน้าและข้อมูล
# ==========================================
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"
if "selected_article_id" not in st.session_state:
    st.session_state.selected_article_id = None
if "page_views" not in st.session_state:
    st.session_state.page_views = 12581
if "active_users" not in st.session_state:
    st.session_state.active_users = 142

st.session_state.page_views += 1
real_adsense_revenue = (st.session_state.page_views / 1000.0) * 80.00

# ==========================================
# 2. ระบบดึงข้อมูลข่าวสารและเรื่องราวแบบจัดเต็ม
# ==========================================
@st.cache_data(ttl=60)
def fetch_pro_feed_data(query: str) -> list:
    items = []
    clean_query = query.strip().lower()
    
    # รูปภาพตัวอย่างประกอบข่าวสารและเทคโนโลยีพรีเมียม
    stock_images = [
        "https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?w=600&auto=format&fit=crop&q=60",
        "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=600&auto=format&fit=crop&q=60",
        "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=60",
        "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=600&auto=format&fit=crop&q=60",
        "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&auto=format&fit=crop&q=60",
        "https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=600&auto=format&fit=crop&q=60"
    ]

    try:
        rss_url = "https://techcrunch.com/feed/"
        resp = requests.get(rss_url, timeout=4)
        if resp.status_code == 200:
            root = ET.fromstring(resp.content)
            for idx, item in enumerate(root.findall('.//item')[:10]):
                title = item.find('title').text if item.find('title') is not None else "Breaking News Update"
                desc = item.find('description').text if item.find('description') is not None else "Latest live update..."
                clean_desc = re.sub('<.*?>', '', desc)
                
                items.append({
                    "id": 30000 + idx,
                    "title": f"Live Online News: {title}",
                    "category": "Technology" if idx % 2 == 0 else "Business",
                    "read_time": f"{idx+2} mins ago",
                    "views": f"{1.2 + idx * 0.5:.1f}k views",
                    "image": stock_images[idx % len(stock_images)],
                    "summary": clean_desc[:180] + "...",
                    "content": f"""Live Global Dispatch & Comprehensive Analysis:
{clean_desc}

Industry Implications & Real-Time Telemetry:
As developments unfold regarding '{clean_query}', international markets react with heightened agility. Analysts point to robust infrastructural scaling and decentralized verification pipelines as key drivers for sustainable growth.

Key Operational Highlights:
- Real-time data synchronization across multi-region edge servers.
- Enhanced cryptographic security and compliance auditing.
- Continuous automated monitoring ensuring 99.999% uptime.

Published live via QELVYQ Global Intelligence Network."""
                })
    except:
        pass

    # เพิ่มฐานข้อมูลเรื่องเล่าและนิทานคุณภาพสูง
    pro_stories_pool = [
        ("The Chrono Weaver: A Short Story of Lost Moments", "Stories", "6 mins ago", "3.4k views", stock_images[0],
         "A short tale about a clockmaker who discovers a pocket watch capable of pausing time for five seconds.",
         """In a cobblestone alleyway sits a dusty clockmaker's shop, tended by an elderly man named Thomas. Unknown to the town, Thomas possessed a brass pocket watch that could halt time for exactly five seconds. 

For years, he used it selfishly to avoid minor embarrassments—spilled coffee, delayed trains, misplaced keys. But one rainy afternoon, as a runaway carriage hurtled toward a young child on the street, Thomas froze time. He walked over, gently moved the child to safety, and let time resume. 

In that single frozen moment, Thomas realized true purpose wasn't about erasing mistakes, but about choosing when to act with courage. From that day on, the watch remained unwound, and Thomas lived fully in every imperfect second."""),
        
        ("The Kingdom of Glass: A Long Story of Truth and Reflection", "Stories", "12 mins ago", "5.8k views", stock_images[1],
         "An epic narrative about a mountain kingdom where every citizen's mirror reflected their true intentions.",
         """High above the cloudline lay Aethelgard, a kingdom constructed entirely of translucent crystal glass. In this realm, mirrors didn't reflect physical appearance; they revealed the pure intent behind a person's words. 

For centuries, the citizens lived in radical harmony. Lies shattered instantly against the glass walls, causing minor tremors across the valley. However, a young ambitious lord named Vane sought power by discovering a rare mineral that could tint the glass, hiding deceit behind shimmering gold facades. 

As the golden haze spread, trust withered, and the kingdom plunged into suspicion. It took a humble glassblower's apprentice, armed only with a hammer of absolute honesty, to shatter the tainted panes and restore the natural light to Aethelgard.""")
    ]

    for idx, (t_title, t_cat, t_time, t_views, t_img, t_sum, t_content) in enumerate(pro_stories_pool):
        items.append({
            "id": 40000 + idx,
            "title": t_title,
            "category": t_cat,
            "read_time": t_time,
            "views": t_views,
            "image": t_img,
            "summary": t_sum,
            "content": t_content,
            "likes": 15 + idx * 5
        })

    return items

if "master_db" not in st.session_state:
    st.session_state.master_db = fetch_pro_feed_data("all")

# ==========================================
# 3. Sidebar เมนูด้านซ้าย (Navigation & Filters)
# ==========================================
with st.sidebar:
    st.markdown("### ⚡ QELVYQ")
    st.caption("Knowledge in Real Time.")
    st.markdown("---")
    
    # เมนูหลัก
    selected_menu = st.radio(
        "Navigation", 
        ["🏠 Home", "📡 Live News", "📖 Stories", "🤖 AI Assistant", "📊 Analytics", "🔖 Bookmarks"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.markdown("### 🔍 Search")
    search_input = st.text_input("Search", placeholder="Search for news, topics...", label_visibility="collapsed")
    
    st.markdown("### 📂 Category Filter")
    selected_filter = st.selectbox(
        "Filter Categories",
        ["All Categories", "Technology", "Business", "Stories", "Science", "World"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.markdown("### ⚡ Quick Access")
    if st.button("🔥 Trending Now"):
        selected_filter = "Technology"
    if st.button("⭐ Most Viewed"):
        selected_filter = "Business"

    st.markdown("---")
    # Admin Passcode สำหรับเข้าโหมด Writer Studio
    with st.expander("🔐 Admin Portal"):
        admin_code = st.text_input("Passcode", type="password")
        if admin_code == "qelvyq2026":
            st.success("Admin Active")
            new_t = st.text_input("Title")
            new_c = st.text_area("Content")
            if st.button("Publish"):
                st.session_state.master_db.insert(0, {
                    "id": 99999, "title": new_t, "category": "Technology", 
                    "read_time": "Just now", "views": "10 views", 
                    "image": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=60",
                    "summary": new_t, "content": new_c, "likes": 1
                })
                st.success("Published!")
                st.rerun()

# ==========================================
# 4. หน้าอ่านบทความเต็มจอ (Dedicated Reader Page)
# ==========================================
if st.session_state.current_page == "reader" and st.session_state.selected_article_id is not None:
    article = next((item for item in st.session_state.master_db if item.get("id") == st.session_state.selected_article_id), None)
    if article:
        if st.button("← Back to Home"):
            st.session_state.current_page = "Home"
            st.session_state.selected_article_id = None
            st.rerun()
            
        st.image(article.get("image", ""), use_column_width=True)
        st.markdown(f"# {article['title']}")
        st.markdown(f"🏷️ **{article['category']}** | ⏱️ {article['read_time']} | 👀 {article['views']}")
        st.markdown("---")
        st.write(article['content'])
        st.markdown("---")
        if st.button("❤️ Like"):
            st.success("Liked!")
        st.stop()

# ==========================================
# 5. หน้าแรกหลัก (Home Dashboard Layout)
# ==========================================

# Hero Banner ด้านบนสุด
current_date_str = datetime.now().strftime("%a, %d %b %Y  %I:%M %p")
st.markdown(
    f"""
    <div style="background: linear-gradient(135deg, #0d1b2a 0%, #1b263b 50%, #415a77 100%); padding: 25px 30px; border-radius: 12px; color: white; margin-bottom: 25px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
            <span style="background: #1d3557; color: #48cae4; padding: 4px 12px; border-radius: 20px; font-size: 11px; font-weight: bold; text-transform: uppercase;">⭐ REAL-TIME NEWS AGGREGATOR</span>
            <span style="font-size: 13px; opacity: 0.8;">📅 {current_date_str} &nbsp;|&nbsp; <span style="color: #2ec4b6; font-weight: bold;">● Live</span></span>
        </div>
        <h1 style="margin: 0; font-size: 28px; font-weight: 700;">QELVYQ — Stories & Real-Time Updates.</h1>
        <p style="margin: 5px 0 0 0; font-size: 14px; opacity: 0.85;">Engaging, short & long stories, moral fables, and live breaking news updates powered by real-time online data.</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Analytics Metrics Header Bar
m1, m2, m3, m4 = st.columns(4)
m1.metric("🟢 Live Active Visitors", f"{st.session_state.active_users} online", "+12% vs. yesterday")
m2.metric("📊 Total Page Views", f"{st.session_state.page_views:,}", "+18% vs. yesterday")
m3.metric("💰 Est. AdSense Revenue", f"${real_adsense_revenue:,.2f} USD", "+24% vs. yesterday")
m4.metric("📚 Total Articles & Tales", f"{len(st.session_state.master_db)} active", "+3 new in the last hour")

st.markdown("---")

# Category Tabs ด้านบนฟีดข่าว
tab_all, tab_news, tab_tech, tab_biz, tab_sci, tab_world = st.tabs(["All", "News", "Tech", "Business", "Science", "World"])

# กรองข้อมูลตาม Search และ Category
filtered_feed = st.session_state.master_db
if search_input:
    filtered_feed = [x for x in filtered_feed if search_input.lower() in x['title'].lower() or search_input.lower() in x['summary'].lower()]
if selected_filter != "All Categories":
    filtered_feed = [x for x in filtered_feed if x['category'].lower() == selected_filter.lower()]

st.markdown("### 📰 Latest News & Updates")
st.caption("Real-time news, technology, business, and more — updated continuously.")

if not filtered_feed:
    st.warning("No articles found matching your criteria.")
else:
    # แสดงผลแบบ 2 คอลัมน์ (การ์ดข่าวพรีเมียมพร้อมภาพประกอบ)
    cols = st.columns(2)
    for idx, item in enumerate(filtered_feed):
        col = cols[idx % 2]
        with col:
            with st.container(border=True):
                if "image" in item:
                    st.image(item["image"], use_column_width=True, height=180)
                
                st.markdown(f"**{item['category']}**")
                st.markdown(f"#### {item['title']}")
                st.write(item['summary'])
                
                c_btn1, c_btn2 = st.columns([3, 1])
                with c_btn1:
                    if st.button(f"📖 Read Story (ID: {item['id']})", key=f"feed_read_{item['id']}_{idx}"):
                        st.session_state.current_page = "reader"
                        st.session_state.selected_article_id = item['id']
                        st.rerun()
                with c_btn2:
                    st.markdown(f"⏱️ {item['read_time']} &nbsp; 👀 {item['views']}")
                
            st.markdown("")

# Footer Banner สไตล์มืออาชีพ
st.markdown("---")
st.markdown(
    """
    <div style="background-color: #f8f9fa; padding: 20px; text-align: center; border-radius: 8px; border: 1px dashed #cbd5e0;">
        <span style="color: #718096; font-size: 11px; text-transform: uppercase; letter-spacing: 1px;">[ GOOGLE ADSENSE - NATIVE AD UNIT ]</span>
        <p style="margin: 8px 0 0 0; font-weight: bold; color: #2d3748;">QELVYQ — Knowledge in Real Time. Delivering verified global intelligence to readers worldwide.</p>
    </div>
    """,
    unsafe_allow_html=True
)
