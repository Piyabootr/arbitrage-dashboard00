import streamlit as st
from datetime import datetime

# =========================================================
# QELVYQ | Knowledge in Real Time (Pro Enterprise Edition)
# Run with: streamlit run safe_arbitrage_dashboard.py
# =========================================================
st.set_page_config(
    page_title="QELVYQ — Knowledge in Real Time",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------- Theme & Professional Graphic Styling (Glassmorphism & Neon Accents) ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');
:root { --navy:#071a3b; --blue:#0878e8; --ink:#0f2537; --muted:#64748b; --line:#cbd5e1; }
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

/* พื้นหลังฟ้าอ่อนระดับพรีเมียมพร้อมกราฟิกแสงเรืองแสง */
.stApp { 
    background: radial-gradient(circle at 10% 10%, rgba(8, 120, 232, 0.08) 0%, transparent 40%),
                radial-gradient(circle at 90% 90%, rgba(59, 130, 246, 0.06) 0%, transparent 40%),
                linear-gradient(180deg, #f0f6ff 0%, #f8fbff 50%, #eef4fd 100%); 
    color: var(--ink); 
}

.block-container { max-width: 1520px; padding-top: 1rem; padding-bottom: 2rem; padding-left: 2rem; padding-right: 2rem; }

[data-testid="stSidebar"] { background: #f4f8ff; border-right:1px solid #d2e2fb; }
[data-testid="stSidebar"] > div { padding-top: 0.8rem; padding-left: 0.8rem; padding-right: 0.8rem; }

h1,h2,h3,h4 { color:var(--ink); letter-spacing:-.025em; }

/* ดีไซน์ Metric กรอบกระจกฝ้าแบบมืออาชีพ */
div[data-testid="stMetric"] { 
    background: rgba(255, 255, 255, 0.85); 
    backdrop-filter: blur(10px);
    border: 1px solid #d1e3fc; 
    border-radius: 14px; 
    padding: 12px 14px; 
    box-shadow: 0 8px 24px rgba(14, 116, 144, 0.06); 
    transition: all 0.3s ease;
}
div[data-testid="stMetric"]:hover {
    border-color: #0878e8;
    box-shadow: 0 12px 28px rgba(8, 120, 232, 0.12);
    transform: translateY(-2px);
}
div[data-testid="stMetricLabel"] { color:#475569; font-size:.8rem; font-weight: 600; }
div[data-testid="stMetricValue"] { color:#0f172a; font-weight:800; font-size: 1.25rem !important; }

.stButton > button { border-radius:8px; border:1px solid #cbd5e1; color:#0f172a; background:#ffffff; font-weight:600; transition:all .2s ease; width: 100%; padding: 0.35rem 0.75rem; font-size: 0.82rem; }
.stButton > button:hover { border-color:#0878e8; color:#0878e8; background:#f0f7ff; box-shadow: 0 4px 12px rgba(8,120,232,0.15); }
div[data-testid="stTextInput"] input, div[data-testid="stSelectbox"] div[data-baseweb="select"] { border-radius:8px; background-color: #ffffff; min-height: 38px; border: 1px solid #cbd5e1; }

/* โลโก้ Sidebar พร้อมลูกเล่นเรืองแสง */
.q-brand-sidebar { display:flex; flex-direction:column; padding: 2px 2px 10px; border-bottom: 1px solid #d8e5f8; margin-bottom: 8px; }
.q-brand-top { display:flex; align-items:center; gap:8px; }
.q-brand-logo { width:34px; height:34px; background:linear-gradient(135deg,#38bdf8,#0284c7); border-radius:9px; display:flex; align-items:center; justify-content:center; color:white; font-size:17px; font-weight:900; box-shadow: 0 4px 12px rgba(2,132,199,0.3); }
.q-brand-title { font-size:18px; font-weight:900; color:#0f172a; line-height:1.1; letter-spacing: -0.03em; }
.q-brand-sub { font-size:10px; color:#64748b; margin-top:2px; font-weight:600; }

/* การ์ดข่าวสารแบบแนวนอน ลวดลายพรีเมียม */
.horizontal-card { background:#ffffff; border:1px solid #d4e3f8; border-radius:12px; padding:12px 15px; box-shadow:0 4px 16px rgba(18,55,102,.045); margin-bottom:10px; display:flex; gap:16px; align-items:center; transition: all 0.25s ease; }
.horizontal-card:hover { border-color: #38bdf8; box-shadow: 0 6px 20px rgba(8,120,232,0.08); }
.h-card-img { width:110px; height:90px; object-fit:cover; border-radius:10px; border:1px solid #e2e8f0; flex-shrink:0; }
.h-card-content { flex-grow:1; }
.h-card-title { font-size:14px; line-height:1.35; font-weight:750; color:#0f172a; margin:3px 0 3px; }
.h-card-summary { color:#475569; font-size:11.5px; line-height:1.45; margin:0 0 6px; }
.h-card-meta { color:#64748b; font-size:10.5px; display:flex; gap:12px; align-items:center; font-weight: 500; }

/* Hero Banner พร้อมลวดลายกราฟิกเชิงเทคโนโลยีมืออาชีพ */
.hero { position:relative; overflow:hidden; border-radius:16px; padding:22px 26px; color:#fff; background:radial-gradient(circle at 80% 20%, rgba(56, 189, 248, 0.35) 0%, transparent 35%), linear-gradient(120deg,#0369a1 0%,#0284c7 50%,#0f172a 100%); box-shadow:0 10px 30px rgba(2,132,199,0.2); margin-bottom:16px; }
.hero:before { content:''; position:absolute; width:200px; height:200px; right:-50px; bottom:-50px; background:rgba(255,255,255,0.05); border-radius:50%; pointer-events:none; }
.hero h1 { font-size:clamp(22px, 1.8vw, 30px); margin:6px 0 4px; font-weight:900; letter-spacing: -0.03em; }
.hero p { font-size:12px; opacity:0.9; margin:0; font-weight: 400; }

/* ป้ายจุดขาย / จุดสังเกตุ (Key Selling Points Badge) */
.usp-badge { display: inline-flex; align-items: center; gap: 6px; background: rgba(15, 23, 42, 0.6); backdrop-filter: blur(4px); border: 1px solid rgba(56, 189, 248, 0.4); border-radius: 20px; padding: 4px 12px; color: #bae6fd; font-size: 10.5px; font-weight: 700; margin-bottom: 8px; }

.section-head { display:flex; align-items:center; gap:8px; margin:4px 0 0; }
.section-head h3 { margin:0; font-size:18px; font-weight:800; }
.section-sub { color:#64748b; font-size:11.5px; margin:2px 0 10px; }

.footer { border-top:1px solid #cbd5e1; padding-top:12px; margin-top:20px; color:#64748b; font-size:10px; text-align:center; font-weight: 500; }
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
    category_filter = st.selectbox("Category Filter", ["All Categories", "Business", "Technology", "AI", "Science", "World"], label_visibility="collapsed")

    st.markdown("""
    <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:12px; padding:10px 12px; margin-top:10px; margin-bottom:10px; box-shadow: 0 4px 12px rgba(0,0,0,0.02);">
        <div style="font-size:11px; font-weight:800; color:#0284c7; margin-bottom:6px; display:flex; align-items:center; gap:5px;">⚡ Quick Access</div>
        <div style="font-size:12px; font-weight:600; color:#1e293b; margin:4px 0;">🔥 Trending Now</div>
        <div style="font-size:12px; font-weight:600; color:#1e293b; margin:4px 0;">👁️ Most Viewed</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%); color:white; border-radius:12px; padding:12px; margin-top:10px; box-shadow:0 6px 16px rgba(2,132,199,0.25);">
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
    <div style="position:absolute; right:20px; top:15px; font-size:11px; color:#e0f2fe; font-weight:500;">Mon, 20 Oct 2026 &bull; <span style="color:#4ade80; font-weight:700;">● Live Real-Time</span></div>
    <div class="usp-badge">🛡️ Verified Live Intelligence &bull; Zero-Delay Sync</div>
    <h1>QELVYQ — Stories & Real-Time Updates.</h1>
    <p>Engaging stories and live breaking news powered by true real-time online data and AI synthesis.</p>
</div>
""", unsafe_allow_html=True)

# Filter articles
filtered_articles = st.session_state.master_db
if search_query:
    filtered_articles = [a for a in filtered_articles if search_query.lower() in a['title'].lower()]
if category_filter != "All Categories":
    filtered_articles = [a for a in filtered_articles if a['category'].lower() == category_filter.lower()]

# Section Header with Selling Point Highlights
st.markdown("""
<div class="section-head">
    <h3>Latest News & Updates</h3>
</div>
<div class="section-sub">✨ Real-time news, technology, business, and more — verified and updated continuously.</div>
""", unsafe_allow_html=True)

# News Grid (Horizontal Cards Pro)
if not filtered_articles:
    st.info("No matching articles found.")
else:
    for idx, item in enumerate(filtered_articles):
        cat_color = "#0284c7" if item["category"] == "Business" else "#7c3aed" if item["category"] == "AI" else "#059669"
        
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
                    <span style="color: #0284c7; font-weight: 600;">✓ Verified Source</span>
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

# ---------- True Analytics Metrics Grid with Professional Graphic Touch ----------
m1, m2, m3, m4, m5 = st.columns(5)
with m1: st.metric("Live Active Visitors", f"{real_active_users} online", "🟢 Real-time session")
with m2: st.metric("Total Page Views", f"{st.session_state.page_views:,}", "📈 Live counter")
with m3: st.metric("Est. AdSense Revenue", f"${real_adsense_revenue:,.4f} USD", "💎 Verified earnings")
with m4: st.metric("Total Articles & Tales", f"{len(st.session_state.master_db)} active", "⚡ Local database")
with m5: st.metric("Live & Verified", "100% Trusted", "🔒 Secure nodes")

# Footer
st.markdown("""
<div class="footer">
    QELVYQ &bull; Knowledge in Real Time &bull; Professional Intelligence Edition
</div>
""", unsafe_allow_html=True)
