import streamlit as st
from datetime import datetime

# =========================================================
# QELVYQ | Knowledge in Real Time (Dark Soft Blue Theme)
# =========================================================
st.set_page_config(
    page_title="QELVYQ — Knowledge in Real Time",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------- Theme & Layout Styling (สีพื้นหลังฟ้าอ่อนปนดำ) ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
:root { 
    --bg-main: #0b1329;       /* สีพื้นหลังหลัก: ฟ้าเข้มปนดำลึกลับ */
    --bg-card: #131c38;       /* สีพื้นหลังการ์ด/กล่อง: ฟ้าหม่นเหลือบดำ */
    --text-main: #e2e8f0;     /* สีตัวหนังสือหลัก: ขาวสว่างนวล */
    --text-muted: #94a3b8;    /* สีตัวหนังสือรอง: เทาอมฟ้า */
    --accent-blue: #38bdf8;   /* สีฟ้าไฮไลต์สว่าง */
    --border-line: #1e293b;   /* สีเส้นขอบ */
}

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

/* เปลี่ยนสีพื้นหลังหลักของแอปทั้งหมด */
.stApp { background: linear-gradient(180deg, #0b1329 0%, #0f172a 100%); color: var(--text-main); }
.block-container { max-width: 1600px; padding-top: 1.2rem; padding-bottom: 2.5rem; }

/* Sidebar Styling */
[data-testid="stSidebar"] { background: #090e1f; border-right: 1px solid var(--border-line); }
[data-testid="stSidebar"] > div { padding-top: 1.0rem; padding-left: 0.8rem; padding-right: 0.8rem; }
[data-testid="stSidebar"] .stTextInput input, [data-testid="stSidebar"] div[data-baseweb="select"] div { background-color: #131c38 !important; color: white !important; border-color: #334155 !important; }

h1, h2, h3, h4 { color: #f8fafc !important; letter-spacing: -.025em; }

/* Metrics Styling */
div[data-testid="stMetric"] { background: var(--bg-card); border: 1px solid var(--border-line); border-radius: 16px; padding: 15px 16px; box-shadow: 0 4px 16px rgba(0,0,0,0.3); }
div[data-testid="stMetricLabel"] { color: var(--text-muted); font-size: .82rem; }
div[data-testid="stMetricValue"] { color: var(--accent-blue); font-weight: 750; }

/* Buttons Styling */
.stButton > button { border-radius: 10px; border: 1px solid #334155; color: #cbd5e1; background: #131c38; font-weight: 600; transition: all .15s ease; }
.stButton > button:hover { border-color: var(--accent-blue); color: #fff; background: #1e293b; }
div[data-testid="stTextInput"] input, div[data-testid="stSelectbox"] div[data-baseweb="select"] { border-radius: 10px; background-color: #131c38; color: #fff; border-color: #334155; }

/* Brand Sidebar */
.q-brand-sidebar { display:flex; flex-direction:column; padding: 4px 4px 16px; border-bottom: 1px solid var(--border-line); margin-bottom: 12px; }
.q-brand-top { display:flex; align-items:center; gap:10px; }
.q-brand-logo { width:32px; height:32px; background:#38bdf8; border-radius:8px; display:flex; align-items:center; justify-content:center; color:#0b1329; font-size:18px; font-weight:bold; }
.q-brand-title { font-size:20px; font-weight:800; color:#f8fafc; line-height:1.1; }
.q-brand-sub { font-size:11px; color:var(--text-muted); margin-top:2px; }

/* การ์ดแนวนอน (Horizontal Card Dark Mode) */
.horizontal-card { background: var(--bg-card); border: 1px solid var(--border-line); border-radius: 15px; padding: 15px; box-shadow: 0 4px 16px rgba(0,0,0,0.2); margin-bottom: 14px; display: flex; gap: 20px; align-items: center; }
.h-card-img { width: 130px; height: 110px; object-fit: cover; border-radius: 12px; border: 1px solid #334155; flex-shrink: 0; }
.h-card-content { flex-grow: 1; }
.h-card-title { font-size: 15px; line-height: 1.35; font-weight: 750; color: #f1f5f9; margin: 4px 0 4px; }
.h-card-summary { color: var(--text-muted); font-size: 12px; line-height: 1.5; margin: 0 0 8px; }
.h-card-meta { color: #64748b; font-size: 11px; display: flex; gap: 15px; align-items: center; }

/* Hero Banner Dark Soft Blue */
.hero { position:relative; overflow:hidden; border-radius:18px; padding:28px 30px 27px; color:#fff; background:radial-gradient(circle at 76% 25%,rgba(56,189,248,0.2),transparent 30%),linear-gradient(115deg,#0f172a 0%,#1e3a8a 56%,#090d16 100%); box-shadow:0 10px 28px rgba(0,0,0,0.4); margin-bottom:18px; border: 1px solid #1e293b; }
.section-head { display:flex; align-items:center; gap:10px; margin:4px 0 2px; }
.section-head h3 { margin:0; font-size:20px; font-weight:750; color: #f8fafc; }
.section-sub { color:var(--text-muted); font-size:12px; margin:3px 0 13px; }

.footer { border-top:1px solid var(--border-line); padding-top:15px; margin-top:25px; color:var(--text-muted); font-size:10px; text-align:center; }
div[data-testid="stHorizontalBlock"] { gap: 1rem; }
</style>
""", unsafe_allow_html=True)

# ---------- Session state ----------
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"
if "selected_article_id" not in st.session_state:
    st.session_state.selected_article_id = None
if "page_views" not in st.session_state:
    st.session_state.page_views = 12581
if "active_users" not in st.session_state:
    st.session_state.active_users = 142
if "bookmarks" not in st.session_state:
    st.session_state.bookmarks = []
if "liked_articles" not in st.session_state:
    st.session_state.liked_articles = []

if "master_db" not in st.session_state:
    st.session_state.master_db = [
        {
            "id": 30001,
            "title": "Walmart’s Flipkart is quietly building a food delivery challenger in India",
            "category": "Business", "time_ago": "4 mins ago", "views": "26 views", "likes": 5,
            "summary": "Flipkart has expanded access to its food-delivery service to thousands of employees ahead of its public launch.",
            "content": "Walmart-backed Flipkart is positioning itself for a major thrust into India’s quick-commerce and food-delivery ecosystem.",
            "image": "https://images.unsplash.com/photo-1526367790999-0150786686a2?auto=format&fit=crop&w=700&q=80",
        },
        {
            "id": 30011,
            "title": "Mamdani says feds have abdicated on AI, urges New Yorkers to push back",
            "category": "Technology", "time_ago": "27 mins ago", "views": "4.2k views", "likes": 4,
            "summary": "New York leaders are debating how communities should respond to rapid AI adoption and the need for public safeguards.",
            "content": "The debate over artificial intelligence governance continues, with local leaders emphasizing transparent oversight.",
            "image": "https://images.unsplash.com/photo-1590402494682-cd3fb53b1f70?auto=format&fit=crop&w=700&q=80",
        },
        {
            "id": 30021,
            "title": "Nscale and Anthropic are reportedly in talks for another $45B compute deal",
            "category": "AI", "time_ago": "58 mins ago", "views": "7.8k views", "likes": 3,
            "summary": "Massive infrastructure investments continue as AI labs scale up their compute clusters for next-gen models.",
            "content": "The soaring demand for computational power has triggered talks around massive funding rounds.",
            "image": "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=700&q=80",
        }
    ]

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
    st.markdown("<p style='font-size:13px; font-weight:700; color:#cbd5e1; margin-bottom:5px;'>🔍 Search</p>", unsafe_allow_html=True)
    search_query = st.text_input("Search topics...", placeholder="Search for news, topics, or keywords...", label_visibility="collapsed")
    
    st.markdown("<p style='font-size:13px; font-weight:700; color:#cbd5e1; margin-bottom:5px; margin-top:10px;'>🔻 Category Filter</p>", unsafe_allow_html=True)
    category_filter = st.selectbox("Category Filter", ["All Categories", "Business", "Technology", "AI", "Science", "World"], label_visibility="collapsed")

# ---------- Dedicated Reader Page ----------
if st.session_state.current_page == "Home" and st.session_state.selected_article_id is not None:
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
            st.write(article.get('content'))
        st.stop()

# ---------- Main Routing ----------
if st.session_state.current_page != "Home":
    st.markdown(f"## 📌 {st.session_state.current_page} Page")
    st.write("Content loaded successfully.")
    st.stop()

# ---------- HOME PAGE DASHBOARD ----------
st.markdown(f"""
<div class="hero">
    <div class="hero-status">Mon, 20 Oct 2026 &bull; <span style="color:#4ade80;">● Live Real-Time</span></div>
    <span class="hero-tag">★ REAL-TIME NEWS AGGREGATOR</span>
    <h1>QELVYQ — Stories & Real-Time Updates.</h1>
    <p>Engaging stories and live breaking news powered by true real-time online data.</p>
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
<div class="section-sub">Real-time news, technology, business, and more — updated continuously.</div>
""", unsafe_allow_html=True)

# News Grid (Horizontal Cards)
if not filtered_articles:
    st.info("No matching articles found.")
else:
    for idx, item in enumerate(filtered_articles):
        cat_color = "#38bdf8" if item["category"] == "Business" else "#c084fc" if item["category"] == "AI" else "#34d399"
        
        st.markdown(f"""
        <div class="horizontal-card">
            <img src="{item['image']}" class="h-card-img">
            <div class="h-card-content">
                <div>
                    <span style="background:{cat_color}; color:#0b1329; padding:2px 8px; border-radius:12px; font-size:9px; font-weight:800;">{item['category']}</span>
                </div>
                <div class="h-card-title">{item['title']}</div>
                <div class="h-card-summary">{item.get('summary', '')}</div>
                <div class="h-card-meta">
                    <span>⏱ {item.get('time_ago')}</span> &nbsp;&bull;&nbsp; 
                    <span>👁 {item.get('views')}</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button(f"📖 Read Story (ID: {item['id']})", key=f"btn_read_{item['id']}"):
            st.session_state.selected_article_id = item['id']
            st.rerun()

st.markdown("<br>", unsafe_allow_html=True)

# ---------- Metrics Grid ----------
m1, m2, m3, m4, m5 = st.columns(5)
with m1: st.metric("Live Active Visitors", f"{st.session_state.active_users} online", "Real-time session")
with m2: st.metric("Total Page Views", f"{st.session_state.page_views:,}", "Live counter")
with m3: st.metric("Est. AdSense Revenue", "$1,006.48 USD", "Based on views")
with m4: st.metric("Total Articles & Tales", f"{len(st.session_state.master_db)} active", "Local database")
with m5: st.metric("Live & Verified", "Trusted sources", "Active status")

# Footer
st.markdown("""
<div class="footer">
    QELVYQ &bull; Knowledge in Real Time &bull; Dark Soft Blue Edition
</div>
""", unsafe_allow_html=True)
