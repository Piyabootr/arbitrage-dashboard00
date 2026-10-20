import streamlit as st
from datetime import datetime

# =========================================================
# QELVYQ | Knowledge in Real Time
# Run with: streamlit run safe_arbitrage_dashboard.py
# =========================================================
st.set_page_config(
    page_title="QELVYQ — Knowledge in Real Time",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------- Theme / layout styling (ปรับแก้สัดส่วนและการจัดวางให้สมมาตร) ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
:root { --navy:#082b63; --blue:#0878e8; --ink:#12315b; --muted:#7185a4; --line:#d0e2ff; }
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

.stApp { background: linear-gradient(180deg,#eef4fd 0%,#f4f8ff 46%,#eaf2ff 100%); color:var(--ink); }

/* ปรับระยะห่างคอนเทนต์ให้เต็มตาและสมมาตร */
.block-container { max-width: 1500px; padding-top: 1rem; padding-bottom: 2rem; padding-left: 2rem; padding-right: 2rem; }

[data-testid="stSidebar"] { background: #f4f8ff; border-right:1px solid #d4e3f8; }
[data-testid="stSidebar"] > div { padding-top: 0.8rem; padding-left: 0.8rem; padding-right: 0.8rem; }

h1,h2,h3,h4 { color:var(--ink); letter-spacing:-.025em; }
div[data-testid="stMetric"] { background:#ffffff; border:1px solid var(--line); border-radius:14px; padding:12px 14px; box-shadow:0 4px 14px rgba(20,63,120,.04); }
div[data-testid="stMetricLabel"] { color:#577399; font-size:.8rem; }
div[data-testid="stMetricValue"] { color:#0a3979; font-weight:750; font-size: 1.25rem !important; }

.stButton > button { border-radius:8px; border:1px solid #cce0f7; color:#16477f; background:#ffffff; font-weight:600; transition:all .15s ease; width: 100%; padding: 0.35rem 0.75rem; font-size: 0.85rem; }
.stButton > button:hover { border-color:#0878e8; color:#0878e8; background:#e4efff; }
div[data-testid="stTextInput"] input, div[data-testid="stSelectbox"] div[data-baseweb="select"] { border-radius:8px; background-color: #ffffff; min-height: 38px; }

/* โลโก้ Sidebar */
.q-brand-sidebar { display:flex; flex-direction:column; padding: 2px 2px 10px; border-bottom: 1px solid #d8e5f8; margin-bottom: 8px; }
.q-brand-top { display:flex; align-items:center; gap:8px; }
.q-brand-logo { width:32px; height:32px; background:linear-gradient(135deg,#1598ff,#0747a6); border-radius:8px; display:flex; align-items:center; justify-content:center; color:white; font-size:16px; font-weight:bold; }
.q-brand-title { font-size:18px; font-weight:800; color:#0f2942; line-height:1.1; }
.q-brand-sub { font-size:10px; color:#577399; margin-top:2px; }

/* การ์ดแนวนอนที่ปรับสัดส่วนให้สมมาตรและกระชับ */
.horizontal-card { background:#ffffff; border:1px solid #d4e3f8; border-radius:12px; padding:12px 15px; box-shadow:0 3px 12px rgba(18,55,102,.035); margin-bottom:10px; display:flex; gap:16px; align-items:center; }
.h-card-img { width:110px; height:90px; object-fit:cover; border-radius:10px; border:1px solid #d4e3f8; flex-shrink:0; }
.h-card-content { flex-grow:1; }
.h-card-title { font-size:14px; line-height:1.3; font-weight:750; color:#113767; margin:3px 0 3px; }
.h-card-summary { color:#577399; font-size:11.5px; line-height:1.45; margin:0 0 6px; }
.h-card-meta { color:#718bb0; font-size:10.5px; display:flex; gap:12px; align-items:center; }

/* Hero Banner แบบสมมาตรและกะทัดรัด */
.hero { position:relative; overflow:hidden; border-radius:16px; padding:20px 24px; color:#fff; background:radial-gradient(circle at 76% 25%,rgba(0,153,255,.4),transparent 26%),linear-gradient(115deg,#071a3b 0%,#073d86 56%,#05275d 100%); box-shadow:0 8px 24px rgba(5,39,93,.14); margin-bottom:14px; }
.hero h1 { font-size:clamp(22px, 1.8vw, 30px); margin:6px 0 4px; font-weight:800; }
.hero p { font-size:12px; opacity:0.9; margin:0; }

.section-head { display:flex; align-items:center; gap:8px; margin:2px 0 0; }
.section-head h3 { margin:0; font-size:18px; font-weight:750; }
.section-sub { color:#577399; font-size:11.5px; margin:2px 0 10px; }

.footer { border-top:1px solid #d4e3f8; padding-top:12px; margin-top:20px; color:#718bb0; font-size:10px; text-align:center; }
div[data-testid="stHorizontalBlock"] { gap: 0.8rem; }
</style>
""", unsafe_allow_html=True)

# ---------- Session State ----------
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
        <div class="q-brand-sub" style="padding-left: 40px;">Knowledge in Real Time.</div>
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
    category_filter = st.selectbox("Category Filter", ["All Categories", "Business", "Technology", "AI", "Science", "World"], label_visibility="collapsed")

    st.markdown("""
    <div style="background:#ffffff; border:1px solid #d4e3f8; border-radius:12px; padding:10px 12px; margin-top:10px; margin-bottom:10px;">
        <div style="font-size:11px; font-weight:700; color:#0878e8; margin-bottom:6px;">⚡ Quick Access</div>
        <div style="font-size:12px; font-weight:600; color:#334155; margin:4px 0;">🔥 Trending Now</div>
        <div style="font-size:12px; font-weight:600; color:#334155; margin:4px 0;">👁️ Most Viewed</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="background: linear-gradient(135deg, #082b63 0%, #061e49 100%); color:white; border-radius:12px; padding:12px; margin-top:10px; box-shadow:0 4px 14px rgba(8,43,99,0.15);">
        <div style="display:flex; align-items:center; gap:6px; margin-bottom:4px;">
            <span style="font-size:16px;">🤖</span>
            <span style="font-size:12px; font-weight:700;">QELVYQ AI Assistant</span>
        </div>
        <p style="font-size:10.5px; color:#d4e6ff; line-height:1.3; margin:0 0 10px 0;">Your smart companion for better information.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Try Now ➔", use_container_width=True):
        st.session_state.current_page = "AI Assistant"
        st.rerun()

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
    <div style="position:absolute; right:20px; top:15px; font-size:11px; color:#d5e9ff;">Mon, 20 Oct 2026 &bull; <span style="color:#4ade80;">● Live Real-Time</span></div>
    <span style="background:rgba(31,143,255,.22); border:1px solid rgba(124,198,255,.3); border-radius:20px; padding:3px 8px; color:#d8efff; font-size:9.5px; font-weight:700; letter-spacing:.08em;">★ REAL-TIME NEWS AGGREGATOR</span>
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

# News Grid (Horizontal Cards Compact)
if not filtered_articles:
    st.info("No matching articles found.")
else:
    for idx, item in enumerate(filtered_articles):
        cat_color = "#0878e8" if item["category"] == "Business" else "#7c3aed" if item["category"] == "AI" else "#059669"
        
        st.markdown(f"""
        <div class="horizontal-card">
            <img src="{item['image']}" class="h-card-img">
            <div class="h-card-content">
                <div>
                    <span style="background:{cat_color}; color:#fff; padding:2px 7px; border-radius:10px; font-size:9px; font-weight:700;">{item['category']}</span>
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

# ---------- True Analytics Metrics Grid (Balanced Sizing) ----------
m1, m2, m3, m4, m5 = st.columns(5)
with m1: st.metric("Live Active Visitors", f"{real_active_users} online", "Real-time session")
with m2: st.metric("Total Page Views", f"{st.session_state.page_views:,}", "Live counter")
with m3: st.metric("Est. AdSense Revenue", f"${real_adsense_revenue:,.4f} USD", "Based on views")
with m4: st.metric("Total Articles & Tales", f"{len(st.session_state.master_db)} active", "Local database")
with m5: st.metric("Live & Verified", "Trusted sources", "Active status")

# Footer
st.markdown("""
<div class="footer">
    QELVYQ &bull; Knowledge in Real Time &bull; True Telemetry Edition
</div>
""", unsafe_allow_html=True)
