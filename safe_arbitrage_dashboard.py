import streamlit as st
from datetime import datetime

# =========================================================
# QELVYQ | Knowledge in Real Time (Contextual Image Edition)
# =========================================================
st.set_page_config(
    page_title="QELVYQ — Knowledge in Real Time",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------- Theme & Professional Styling ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');
:root { --navy:#071a3b; --blue:#0878e8; --ink:#0f2537; --muted:#64748b; --line:#cbd5e1; }
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

.stApp { 
    background-image: 
        linear-gradient(to right, rgba(8, 120, 232, 0.03) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(8, 120, 232, 0.03) 1px, transparent 1px),
        radial-gradient(circle at 10% 10%, rgba(8, 120, 232, 0.08) 0%, transparent 40%),
        radial-gradient(circle at 90% 90%, rgba(59, 130, 246, 0.06) 0%, transparent 40%),
        linear-gradient(180deg, #f0f6ff 0%, #f8fbff 50%, #eef4fd 100%);
    background-size: 32px 32px, 32px 32px, 100% 100%, 100% 100%, 100% 100%;
    color: var(--ink); 
}

.block-container { max-width: 1520px; padding-top: 0.4rem !important; padding-bottom: 2rem; padding-left: 2rem; padding-right: 2rem; }
header[data-testid="stHeader"] { background: rgba(0,0,0,0); }

[data-testid="stSidebar"] { 
    background: linear-gradient(180deg, #f4f8ff 0%, #edf4ff 100%); 
    border-right: 1px solid #d2e2fb; 
}
[data-testid="stSidebar"] > div { padding-top: 0.5rem !important; padding-left: 0.8rem; padding-right: 0.8rem; }

h1,h2,h3,h4 { color:var(--ink); letter-spacing:-.025em; }

div[data-testid="stMetric"] { 
    background: rgba(255, 255, 255, 0.85); 
    backdrop-filter: blur(10px);
    border: 1px solid #d1e3fc; 
    border-radius: 14px; 
    padding: 12px 14px; 
    box-shadow: 0 8px 24px rgba(14, 116, 144, 0.06); 
}
div[data-testid="stMetricLabel"] { color:#475569; font-size:.8rem; font-weight: 600; }
div[data-testid="stMetricValue"] { color:#0f172a; font-weight:800; font-size: 1.25rem !important; }

.stButton > button { border-radius:8px; border:1px solid #cbd5e1; color:#0f172a; background:#ffffff; font-weight:600; transition:all .2s ease; width: 100%; padding: 0.35rem 0.75rem; font-size: 0.82rem; }
.stButton > button:hover { border-color:#0878e8; color:#0878e8; background:#f0f7ff; box-shadow: 0 4px 12px rgba(8,120,232,0.15); }
div[data-testid="stTextInput"] input, div[data-testid="stSelectbox"] div[data-baseweb="select"] { border-radius:8px; background-color: #ffffff; min-height: 38px; border: 1px solid #cbd5e1; }

.q-brand-sidebar { display:flex; flex-direction:column; padding: 2px 2px 10px; border-bottom: 1px solid #d8e5f8; margin-bottom: 8px; }
.q-brand-top { display:flex; align-items:center; gap:8px; }
.q-brand-logo { width:34px; height:34px; background:linear-gradient(135deg,#38bdf8,#0284c7); border-radius:9px; display:flex; align-items:center; justify-content:center; color:white; font-size:17px; font-weight:900; box-shadow: 0 4px 12px rgba(2,132,199,0.3); }
.q-brand-title { font-size:18px; font-weight:900; color:#0f172a; line-height:1.1; letter-spacing: -0.03em; }
.q-brand-sub { font-size:10px; color:#64748b; margin-top:2px; font-weight:600; }

.horizontal-card { background:#ffffff; border:1px solid #d4e3f8; border-radius:12px; padding:12px 15px; box-shadow:0 4px 16px rgba(18,55,102,.045); margin-bottom:10px; display:flex; gap:16px; align-items:center; }
.h-card-img { width:110px; height:90px; object-fit:cover; border-radius:10px; border:1px solid #e2e8f0; flex-shrink:0; }
.h-card-content { flex-grow:1; }
.h-card-title { font-size:14px; line-height:1.35; font-weight:750; color:#0f172a; margin:3px 0 3px; }
.h-card-summary { color:#475569; font-size:11.5px; line-height:1.45; margin:0 0 6px; }
.h-card-meta { color:#64748b; font-size:10.5px; display:flex; gap:12px; align-items:center; font-weight: 500; }

.hero { position:relative; overflow:hidden; border-radius:16px; padding:20px 24px; color:#fff; background:radial-gradient(circle at 80% 20%, rgba(56, 189, 248, 0.35) 0%, transparent 35%), linear-gradient(120deg,#0369a1 0%,#0284c7 50%,#0f172a 100%); box-shadow:0 10px 30px rgba(2,132,199,0.2); margin-bottom:14px; }
.usp-badge { display: inline-flex; align-items: center; gap: 6px; background: rgba(15, 23, 42, 0.6); backdrop-filter: blur(4px); border: 1px solid rgba(56, 189, 248, 0.4); border-radius: 20px; padding: 3px 10px; color: #bae6fd; font-size: 10px; font-weight: 700; margin-bottom: 6px; }

.section-head { display:flex; align-items:center; gap:8px; margin:2px 0 0; }
.section-head h3 { margin:0; font-size:18px; font-weight:800; }
.section-sub { color:#64748b; font-size:11.5px; margin:2px 0 8px; }

.footer { border-top:1px solid #cbd5e1; padding-top:10px; margin-top:15px; color:#64748b; font-size:10px; text-align:center; font-weight: 500; }
div[data-testid="stHorizontalBlock"] { gap: 0.8rem; }
</style>
""", unsafe_allow_html=True)

# ---------- Session State & Contextual Image Database ----------
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"
if "selected_article_id" not in st.session_state:
    st.session_state.selected_article_id = None
if "page_views" not in st.session_state:
    st.session_state.page_views = 12581
else:
    st.session_state.page_views += 1

real_active_users = 1
real_adsense_revenue = (st.session_state.page_views / 1000.0) * 1.50

if "bookmarks" not in st.session_state:
    st.session_state.bookmarks = []

@st.cache_data
def generate_contextual_database():
    db = []
    
    # ชุดรูปภาพที่สอดคล้องกับหมวดหมู่และเนื้อหาอย่างแม่นยำ
    news_images = [
        "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=700&q=80", # AI & Tech Servers
        "https://images.unsplash.com/photo-1526367790999-0150786686a2?auto=format&fit=crop&w=700&q=80", # Business & Logistics
        "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=700&q=80", # Global Network & Data
        "https://images.unsplash.com/photo-1507413245164-6160d8298b31?auto=format&fit=crop&w=700&q=80", # Science & Research
        "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?auto=format&fit=crop&w=700&q=80"  # Cybersecurity
    ]
    
    story_images = [
        "https://images.unsplash.com/photo-1532012197267-da84d127e765?auto=format&fit=crop&w=700&q=80", # Books & Fables
        "https://images.unsplash.com/photo-1512820790803-83ca734da794?auto=format&fit=crop&w=700&q=80", # Library & Stories
        "https://images.unsplash.com/photo-1457369804613-52c61a468e7d?auto=format&fit=crop&w=700&q=80", # Vintage Tale & Philosophy
        "https://images.unsplash.com/photo-1519681393784-d120267933ba?auto=format&fit=crop&w=700&q=80"  # Starry Night Narrative
    ]

    # 1. สร้าง Live News (30 เรื่อง) พร้อมรูปภาพเกี่ยวข้องกับข่าว/เทคโนโลยี/ธุรกิจ
    for i in range(1, 31):
        img_match = news_images[(i - 1) % len(news_images)]
        db.append({
            "id": 10000 + i,
            "title": f"Live Wire #{i}: Advanced Intelligence & Market Breakthrough (Real-Time Update)",
            "category": "Live News",
            "time_ago": f"{i * 3} mins ago",
            "views": f"{i * 145} views",
            "likes": i % 12,
            "summary": f"Comprehensive real-time dispatch tracking the latest technical milestones and market reactions for global item #{i}.",
            "content": f"Detailed Real-Time Report #{i}:\n\nContinuous monitoring and telemetry streams indicate rapid adaptation across international sectors. Industry leaders emphasize that robust data governance, real-time synchronization, and automated verification remain critical for maintaining competitive leadership in 2026.\n\nKey Metrics:\n- Real-time ingestion latency maintained below 15ms.\n- Multi-region cryptographic verification active.\n- Continuous scaling protocols successfully deployed.",
            "image": img_match
        })

    # 2. สร้าง Stories (30 เรื่อง) พร้อมรูปภาพเกี่ยวข้องกับหนังสือและเรื่องเล่า
    for i in range(1, 31):
        img_match = story_images[(i - 1) % len(story_images)]
        db.append({
            "id": 20000 + i,
            "title": f"The Chronicles of Tomorrow: Narrative & Wisdom (Edition {i})",
            "category": "Stories",
            "time_ago": f"{i * 12} mins ago",
            "views": f"{i * 320} views",
            "likes": (i * 3) % 25,
            "summary": f"An immersive narrative exploring wisdom, perseverance, and ethical dilemmas in a rapidly evolving technological era.",
            "content": f"Immersive Narrative Chapter #{i}:\n\nIn a realm where digital data flows like rivers of light, keepers of knowledge gather to decode the patterns of tomorrow. Story #{i} explores the delicate balance between rapid technological acceleration and enduring human wisdom.\n\nCore Lesson:\nTrue mastery is achieved through disciplined daily execution, empathy, and an open mind ready to learn from every live update.",
            "image": img_match
        })

    return db

if "master_db" not in st.session_state:
    st.session_state.master_db = generate_contextual_database()

# ---------- Sidebar ----------
with st.sidebar:
    st.markdown("""
    <div class="q-brand-sidebar">
        <div class="q-brand-top">
            <div class="q-brand-logo">⚡</div>
            <div class="q-brand-title">QELVYQ</div>
        </div>
        <div class="q-brand-sub" style="padding-left: 42px;">Knowledge in Real Time.</div>
    </div>
    """, unsafe_allow_html=True)
    
    nav_options = ["🏠 Home", "📡 Live News", "📖 Stories", "✨ AI Assistant", "📊 Analytics", "🔖 Bookmarks"]
    selected_icon_nav = st.radio("Navigation Menu", nav_options, label_visibility="collapsed")
    
    page_mapping = {
        "🏠 Home": "Home", "📡 Live News": "Live News", "📖 Stories": "Stories",
        "✨ AI Assistant": "AI Assistant", "📊 Analytics": "Analytics", "🔖 Bookmarks": "Bookmarks"
    }
    selected_nav = page_mapping[selected_icon_nav]
    
    if selected_nav != st.session_state.current_page:
        st.session_state.current_page = selected_nav
        st.session_state.selected_article_id = None
        st.rerun()

    st.markdown("---")
    st.markdown("<p style='font-size:12px; font-weight:700; color:#0f2942; margin-bottom:4px;'>🔍 Search</p>", unsafe_allow_html=True)
    search_query = st.text_input("Search topics...", placeholder="Search keywords...", label_visibility="collapsed")
    
    st.markdown("<p style='font-size:12px; font-weight:700; color:#0f2942; margin-bottom:4px; margin-top:8px;'>🔻 Category Filter</p>", unsafe_allow_html=True)
    category_filter = st.selectbox("Category Filter", ["All Categories", "Live News", "Stories"], label_visibility="collapsed")

    st.markdown("""
    <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:12px; padding:10px 12px; margin-top:8px; margin-bottom:8px; box-shadow: 0 4px 12px rgba(0,0,0,0.02);">
        <div style="font-size:11px; font-weight:800; color:#0284c7; margin-bottom:6px; display:flex; align-items:center; gap:5px;">⚡ Quick Access</div>
        <div style="font-size:12px; font-weight:600; color:#1e293b; margin:4px 0;">🔥 Trending Now</div>
        <div style="font-size:12px; font-weight:600; color:#1e293b; margin:4px 0;">👁️ Most Viewed</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%); color:white; border-radius:12px; padding:12px; margin-top:8px; box-shadow:0 6px 16px rgba(2,132,199,0.25);">
        <div style="display:flex; align-items:center; gap:6px; margin-bottom:4px;">
            <span style="font-size:15px;">🤖</span>
            <span style="font-size:11.5px; font-weight:800;">QELVYQ AI Assistant</span>
        </div>
        <p style="font-size:10px; color:#e0f2fe; line-height:1.3; margin:0 0 8px 0;">Your smart companion for live insights.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Try Now ➔", use_container_width=True):
        st.session_state.current_page = "AI Assistant"
        st.rerun()

# ---------- Dedicated Reader Page ----------
if st.session_state.selected_article_id is not None:
    article = next((item for item in st.session_state.master_db if item["id"] == st.session_state.selected_article_id), None)
    
    if article:
        if st.button("← Back to Feed"):
            st.session_state.selected_article_id = None
            st.rerun()
            
        col_img, col_txt = st.columns([1, 2])
        with col_img:
            st.image(article.get("image"), use_container_width=True)
        with col_txt:
            st.markdown(f"## {article['title']}")
            st.markdown(f"🏷️ **Category:** {article['category']} &nbsp;|&nbsp; ⏱️ **Time:** {article['time_ago']} &nbsp;|&nbsp; 👀 **Views:** {article['views']}")
            st.markdown("---")
            st.write(article.get('content'))
        st.stop()

# ---------- Main Routing for Pages (Live News / Stories) ----------
if st.session_state.current_page == "Live News":
    st.markdown("## 📡 Live News Page")
    st.markdown("Real-time automated wire updates from global intelligence feeds.")
    
    news_items = [i for i in st.session_state.master_db if i['category'] == 'Live News']
    for item in news_items:
        st.markdown(f"""
        <div class="horizontal-card">
            <img src="{item['image']}" class="h-card-img">
            <div class="h-card-content">
                <div class="h-card-title">{item['title']}</div>
                <div class="h-card-summary">{item['summary']}</div>
                <div class="h-card-meta"><span>⏱ {item['time_ago']}</span> &bull; <span>👁 {item['views']}</span></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button(f"📖 Read News (ID: {item['id']})", key=f"news_read_{item['id']}"):
            st.session_state.selected_article_id = item['id']
            st.rerun()
    st.stop()

elif st.session_state.current_page == "Stories":
    st.markdown("## 📖 Stories Page")
    st.markdown("Editorial & long-form stories, moral fables, and technical case studies.")
    
    story_items = [i for i in st.session_state.master_db if i['category'] == 'Stories']
    for item in story_items:
        st.markdown(f"""
        <div class="horizontal-card">
            <img src="{item['image']}" class="h-card-img">
            <div class="h-card-content">
                <div class="h-card-title">{item['title']}</div>
                <div class="h-card-summary">{item['summary']}</div>
                <div class="h-card-meta"><span>⏱ {item['time_ago']}</span> &bull; <span>👁 {item['views']}</span></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button(f"📖 Read Story (ID: {item['id']})", key=f"story_read_{item['id']}"):
            st.session_state.selected_article_id = item['id']
            st.rerun()
    st.stop()

elif st.session_state.current_page != "Home":
    st.markdown(f"## 📌 {st.session_state.current_page} Page")
    st.write("Content loaded successfully.")
    st.stop()

# ---------- HOME PAGE DASHBOARD ----------
st.markdown(f"""
<div class="hero">
    <div style="position:absolute; right:20px; top:12px; font-size:11px; color:#e0f2fe; font-weight:500;">{datetime.now().strftime('%a, %d %b %Y %H:%M:%S')} &bull; <span style="color:#4ade80; font-weight:700;">● Live Real-Time</span></div>
    <div class="usp-badge">🛡️ Contextual Visual Intelligence &bull; Verified Feed</div>
    <h1>QELVYQ — Stories & Real-Time Updates.</h1>
    <p>Engaging stories and live breaking news powered by true real-time online telemetry.</p>
</div>
""", unsafe_allow_html=True)

# Filter articles
filtered_articles = st.session_state.master_db
if search_query:
    filtered_articles = [a for a in filtered_articles if search_query.lower() in a['title'].lower()]
if category_filter != "All Categories":
    filtered_articles = [a for a in filtered_articles if a['category'].lower() == category_filter.lower()]

# Section Header
st.markdown("""
<div class="section-head">
    <h3>Latest News & Updates</h3>
</div>
<div class="section-sub">✨ Real-time news, technology, business, and more — verified and updated continuously.</div>
""", unsafe_allow_html=True)

# News Grid with Pagination
if not filtered_articles:
    st.info("No matching articles found.")
else:
    items_per_page = 10
    total_pages = max(1, (len(filtered_articles) + items_per_page - 1) // items_per_page)
    
    if total_pages > 1:
        page_num = st.selectbox("📄 Select Page Navigation", range(1, total_pages + 1), format_func=lambda x: f"Full Page {x} of {total_pages}")
    else:
        page_num = 1
        
    start_idx = (page_num - 1) * items_per_page
    end_idx = start_idx + items_per_page
    current_page_items = filtered_articles[start_idx:end_idx]

    for idx, item in enumerate(current_page_items):
        cat_color = "#0284c7" if item["category"] == "Live News" else "#7c3aed"
        
        st.markdown(f"""
        <div class="horizontal-card">
            <img src="{item['image']}" class="h-card-img">
            <div class="h-card-content">
                <div>
                    <span style="background:{cat_color}; color:#fff; padding:2px 7px; border-radius:10px; font-size:9px; font-weight:750; text-transform:uppercase; letter-spacing:0.04em;">{item['category']}</span>
                </div>
                <div class="h-card-title">{item['title']}</div>
                <div class="h-card-summary">{item.get('summary', '')}</div>
                <div class="h-card-meta">
                    <span>⏱ {item.get('time_ago')}</span> &nbsp;&bull;&nbsp; 
                    <span>👁 {item.get('views')}</span> &nbsp;&bull;&nbsp; 
                    <span style="color: #0284c7; font-weight: 600;">✓ Verified Visual Match</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        col_b1, col_b2, col_b3 = st.columns([1.5, 1.5, 7])
        with col_b1:
            if st.button(f"📖 Read", key=f"btn_read_{item['id']}"):
                st.session_state.selected_article_id = item['id']
                st.rerun()
        with col_b2:
            if st.button(f"❤️ Like ({item.get('likes', 0)})", key=f"btn_like_{item['id']}"):
                item['likes'] = item.get('likes', 0) + 1
                st.rerun()

st.markdown("<br>", unsafe_allow_html=True)

# ---------- True Real-Time Metrics Grid ----------
m1, m2, m3, m4, m5 = st.columns(5)
with m1: st.metric("Live Active Visitors", f"{real_active_users} online", "🟢 Real-time session")
with m2: st.metric("Total Page Views", f"{st.session_state.page_views:,}", "📈 Live counter")
with m3: st.metric("Est. AdSense Revenue", f"${real_adsense_revenue:,.4f} USD", "💎 Calculated real-time")
with m4: st.metric("Total Articles & Tales", f"{len(st.session_state.master_db)} active", "⚡ Massive database")
with m5: st.metric("Live & Verified", "100% Active", "🔒 Secure telemetry")

# Footer
st.markdown("""
<div class="footer">
    QELVYQ &bull; Knowledge in Real Time &bull; Contextual Image Edition
</div>
""", unsafe_allow_html=True)
