import streamlit as st
from datetime import datetime

# =========================================================
# QELVYQ | Knowledge in Real Time
# Run with: streamlit run qelvyq_dashboard.py
# =========================================================
st.set_page_config(
    page_title="QELVYQ — Knowledge in Real Time",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------- Theme / layout styling ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
:root { --navy:#082b63; --blue:#0878e8; --ink:#12315b; --muted:#7185a4; --line:#e3ebf7; }
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
.stApp { background: linear-gradient(180deg,#f5f9ff 0%,#ffffff 46%,#f8fbff 100%); color:var(--ink); }
.block-container { max-width: 1600px; padding-top: 1.2rem; padding-bottom: 2.5rem; }
[data-testid="stSidebar"] { background: #eef5ff; border-right:1px solid #dce8f8; }
[data-testid="stSidebar"] > div { padding-top: 1.2rem; }
h1,h2,h3,h4 { color:var(--ink); letter-spacing:-.025em; }
div[data-testid="stMetric"] { background:#fff; border:1px solid var(--line); border-radius:16px; padding:15px 16px; box-shadow:0 4px 16px rgba(20,63,120,.045); }
div[data-testid="stMetricLabel"] { color:#6b82a3; font-size:.82rem; }
div[data-testid="stMetricValue"] { color:#0a3979; font-weight:750; }
.stButton > button { border-radius:10px; border:1px solid #d8e5f6; color:#16477f; background:#fff; font-weight:600; transition:all .15s ease; }
.stButton > button:hover { border-color:#1683ef; color:#0878e8; background:#f1f8ff; }
div[data-testid="stTextInput"] input, div[data-testid="stSelectbox"] div[data-baseweb="select"] { border-radius:10px; }
.q-brand { display:flex; align-items:center; gap:10px; padding:4px 2px 18px; }
.q-brand-mark { display:flex; align-items:center; justify-content:center; width:42px; height:42px; border-radius:13px; color:#fff; font-size:25px; background:linear-gradient(135deg,#1598ff,#0747a6); box-shadow:0 7px 18px rgba(8,120,232,.22); }
.q-brand-name { font-size:23px; line-height:1.05; font-weight:800; letter-spacing:.02em; color:#0a3979; }
.q-brand-tag { color:#7185a4; font-size:10px; margin-top:4px; }
.hero { position:relative; overflow:hidden; border-radius:18px; padding:28px 30px 27px; color:#fff; background:radial-gradient(circle at 76% 25%,rgba(0,153,255,.4),transparent 26%),linear-gradient(115deg,#071a3b 0%,#073d86 56%,#05275d 100%); box-shadow:0 10px 28px rgba(5,39,93,.16); margin-bottom:18px; }
.hero:after { content:""; position:absolute; width:320px;height:320px; right:7%;top:-180px;border:1px solid rgba(100,190,255,.24);border-radius:50%;box-shadow:0 0 0 20px rgba(100,190,255,.035),0 0 0 45px rgba(100,190,255,.035),0 0 0 72px rgba(100,190,255,.025); }
.hero-tag { display:inline-block; background:rgba(31,143,255,.22); border:1px solid rgba(124,198,255,.3); border-radius:20px; padding:5px 10px; color:#d8efff; font-size:10px; font-weight:700; letter-spacing:.08em; }
.hero h1 { color:#fff; font-size:clamp(25px,2.2vw,36px); margin:10px 0 7px; line-height:1.2; font-weight:800; }
.hero p { color:#d0e3ff; margin:0; font-size:13px; max-width:760px; }
.hero-status { position:absolute; right:25px; top:22px; z-index:1; color:#d5e9ff; font-size:11px; }
.section-head { display:flex; align-items:center; gap:10px; margin:4px 0 2px; }
.section-head h3 { margin:0; font-size:20px; font-weight:750; }
.section-sub { color:#7589a7; font-size:12px; margin:3px 0 13px; }
.news-card { background:#fff; border:1px solid #e0eafa; border-radius:15px; padding:11px; box-shadow:0 4px 16px rgba(18,55,102,.045); min-height:164px; margin-bottom:4px; }
.news-image { width:100%; height:128px; object-fit:cover; border-radius:10px; border:1px solid #e8eef8; }
.news-category { display:inline-block; font-size:10px; font-weight:700; color:#fff; padding:4px 8px; border-radius:20px; margin-bottom:5px; }
.news-title { font-size:14px; line-height:1.4; font-weight:750; color:#113767; margin:0 0 5px; }
.news-summary { color:#6b7f9e; font-size:11px; line-height:1.55; margin:0 0 8px; }
.news-meta { color:#8092ad; font-size:10px; }
.small-pill { display:inline-block; border:1px solid #e1ebf8; border-radius:20px; padding:4px 8px; color:#607da3; background:#f8fbff; font-size:10px; }
.ai-panel { background:linear-gradient(145deg,#073b82,#061e49); color:white; border-radius:15px; padding:17px; margin-top:16px; box-shadow:0 8px 20px rgba(5,39,93,.14); }
.ai-panel h4 { color:white; margin:5px 0 6px; font-size:15px; }
.ai-panel p { color:#d4e6ff; font-size:11px; line-height:1.55; }
.footer { border-top:1px solid #e4ecf7; padding-top:15px; margin-top:25px; color:#8a9bb4; font-size:10px; text-align:center; }
div[data-testid="stHorizontalBlock"] { gap: 1rem; }
@media (max-width: 900px) { .hero-status { position:static; margin-top:12px; } .hero { padding:22px; } }
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

# Image URLs are illustrative thumbnails; replace with your own approved image sources if needed.
if "master_db" not in st.session_state:
    st.session_state.master_db = [
        {
            "id": 30001,
            "title": "Walmart’s Flipkart is quietly building a food delivery challenger in India",
            "category": "Business", "time_ago": "4 mins ago", "views": "26 views", "likes": 5,
            "summary": "Flipkart has expanded access to its food-delivery service to thousands of employees ahead of its public launch.",
            "content": "Walmart-backed Flipkart is positioning itself for a major thrust into India’s quick-commerce and food-delivery ecosystem. The early rollout may help the company test logistics, demand, and customer experience before a wider launch.",
            "image": "https://images.unsplash.com/photo-1563013544-824ae1b704d3?auto=format&fit=crop&w=700&q=80",
        },
        {
            "id": 30011,
            "title": "Mamdani says feds have abdicated on AI, urges New Yorkers to push back",
            "category": "Technology", "time_ago": "27 mins ago", "views": "4.2k views", "likes": 4,
            "summary": "New York leaders are debating how communities should respond to rapid AI adoption and the need for public safeguards.",
            "content": "The debate over artificial intelligence governance continues, with local leaders emphasizing transparent oversight, workforce protections, and community involvement in decisions about automated systems.",
            "image": "https://images.unsplash.com/photo-1480714378408-67cf0d13bc1b?auto=format&fit=crop&w=700&q=80",
        },
        {
            "id": 30021,
            "title": "Nscale and Anthropic are reportedly in talks for another $45B compute deal",
