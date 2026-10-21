import streamlit as st
from datetime import datetime

# =========================================================
# QELVYQ | Knowledge in Real Time (Clean Production Edition)
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
    background: rgba(255, 255, 255, 0.9); 
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

.horizontal-card { background:#ffffff; border:1px solid #d4e3f8; border-radius:14px; padding:16px 18px; box-shadow:0 4px 16px rgba(18,55,102,.05); margin-bottom:10px; display:flex; gap:18px; align-items:flex-start; }
.h-card-img { width:145px; height:125px; object-fit:cover; border-radius:10px; border:1px solid #e2e8f0; flex-shrink:0; }
.h-card-content { flex-grow:1; }
.h-card-title { font-size:15.5px; line-height:1.35; font-weight:800; color:#0f172a; margin:4px 0 6px; }
.h-card-summary { color:#1e293b; font-size:12.5px; line-height:1.55; margin:0 0 8px; font-weight: 500; }
.h-card-story-box { background:#f8fafc; border-left:3px solid #0284c7; padding:8px 12px; border-radius:6px; color:#334155; font-size:12px; line-height:1.6; margin-bottom:8px; }
.h-card-meta { color:#64748b; font-size:11px; display:flex; gap:12px; align-items:center; font-weight: 600; }

.hero { position:relative; overflow:hidden; border-radius:16px; padding:20px 24px; color:#fff; background:radial-gradient(circle at 80% 20%, rgba(56, 189, 248, 0.35) 0%, transparent 35%), linear-gradient(120deg,#0369a1 0%,#0284c7 50%,#0f172a 100%); box-shadow:0 10px 30px rgba(2,132,199,0.2); margin-bottom:14px; }
.usp-badge { display: inline-flex; align-items: center; gap: 6px; background: rgba(15, 23, 42, 0.6); backdrop-filter: blur(4px); border: 1px solid rgba(56, 189, 248, 0.4); border-radius: 20px; padding: 3px 10px; color: #bae6fd; font-size: 10px; font-weight: 700; margin-bottom: 6px; }

.section-head { display:flex; align-items:center; gap:8px; margin:2px 0 0; }
.section-head h3 { margin:0; font-size:18px; font-weight:800; }
.section-sub { color:#64748b; font-size:11.5px; margin:2px 0 8px; }

.footer { border-top:1px solid #cbd5e1; padding-top:10px; margin-top:15px; color:#64748b; font-size:10px; text-align:center; font-weight: 500; }
div[data-testid="stHorizontalBlock"] { gap: 0.8rem; }
</style>
""", unsafe_allow_html=True)

# =========================================================
# 1. สร้างฐานข้อมูลเนื้อหา (หมวดละ 40 เรื่อง = 240 เรื่อง)
# =========================================================
@st.cache_data
def build_clean_database():
    db = []
    topics_config = {
        "Stories": {
            "color": "#7c3aed",
            "images": ["https://images.unsplash.com/photo-1532012197267-da84d127e765?auto=format&fit=crop&w=700&q=80"],
            "items": [
                ("The Story of Tam and Cam", "Classic Vietnamese folklore about kindness and virtue.", "Tam and Cam were half-sisters...")
            ]
        },
        "Technology": {
            "color": "#059669",
            "images": ["https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=700&q=80"],
            "items": [
                ("VESDA-E VEA Smoke Detection", "Aspirating smoke detection architecture.", "In mission-critical data centers...")
            ]
        },
        "Live News": {
            "color": "#0284c7",
            "images": ["https://images.unsplash.com/photo-1504711434969-e33886168f5c?auto=format&fit=crop&w=700&q=80"],
            "items": [
                ("Southeast Asia Data Center Capacity", "Cloud providers accelerate construction.", "Real-time industry reports confirm...")
            ]
        },
        "Business": {
            "color": "#d97706",
            "images": ["https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=700&q=80"],
            "items": [
                ("The 50/30/20 Financial Rule", "Personal finance framework for wealth building.", "The 50/30/20 rule divides net income...")
            ]
        },
        "AI": {
            "color": "#db2777",
            "images": ["https://images.unsplash.com/photo-1620712943543-bcc4688e7485?auto=format&fit=crop&w=700&q=80"],
            "items": [
                ("YOLO Image Segmentation", "Computer vision for fire and smoke detection.", "YOLO instance segmentation traces...")
            ]
        },
        "Science": {
            "color": "#4f46e5",
            "images": ["https://images.unsplash.com/photo-1507413245164-6160d8298b31?auto=format&fit=crop&w=700&q=80"],
            "items": [
                ("Neuroscience of Contagious Yawning", "Mirror neurons and human empathy.", "Contagious yawning is driven by mirror neurons...")
            ]
        }
    }

    article_id = 10001
    for category, data in topics_config.items():
        for i in range(1, 41):
            base_title, base_summary, story_body = data["items"][0]
            db.append({
                "id": article_id,
                "title": f"{base_title} — Vol. #{i}",
                "category": category,
                "color": data["color"],
                "time_ago": f"{i} mins ago",
                "views": f"{i * 100} views",
                "likes": i % 10,
                "summary": base_summary,
                "story_preview": story_body,
                "content": f"### {base_title}\n\n{story_body}",
                "image": data["images"][0]
            })
            article_id += 1
    return db

if "master_db" not in st.session_state:
    st.session_state.master_db = build_clean_database()

if "bookmarks" not in st.session_state:
    st.session_state.bookmarks = []
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"
if "selected_article_id" not in st.session_state:
    st.session_state.selected_article_id = None
if "page_views" not in st.session_state:
    st.session_state.page_views = 1
else:
    st.session_state.page_views += 1

# ---------- Helper Function ----------
def render_article_feed(articles_list, prefix_key="feed"):
    if not articles_list:
        st.warning("No matching articles found.")
        return

    for idx, item in enumerate(articles_list[:15]):
        st.markdown(f"""
        <div class="horizontal-card">
            <img src="{item['image']}" class="h-card-img">
            <div class="h-card-content">
                <div><span style="background:{item['color']}; color:#fff; padding:2px 8px; border-radius:10px; font-size:9.5px; font-weight:750;">{item['category']}</span></div>
                <div class="h-card-title">{item['title']}</div>
                <div class="h-card-summary">{item['summary']}</div>
                <div class="h-card-meta"><span>⏱ {item['time_ago']}</span> &bull; <span>👁 {item['views']}</span></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button(f"📖 Read ID: {item['id']}", key=f"{prefix_key}_read_{item['id']}_{idx}"):
            st.session_state.selected_article_id = item['id']
            st.rerun()

# ---------- Sidebar ----------
with st.sidebar:
    st.markdown("### ⚡ QELVYQ Navigation")
    nav_options = ["Home", "Live News", "Stories", "AI Assistant", "Analytics", "Bookmarks"]
    selected_nav = st.radio("Menu", nav_options, label_visibility="collapsed")
    
    if selected_nav != st.session_state.current_page:
        st.session_state.current_page = selected_nav
        st.session_state.selected_article_id = None
        st.rerun()

    search_query = st.text_input("Search", placeholder="Search keywords...")

# ---------- Reader Page ----------
if st.session_state.selected_article_id is not None:
    article = next((item for item in st.session_state.master_db if item["id"] == st.session_state.selected_article_id), None)
    if article:
        if st.button("← Back to Feed"):
            st.session_state.selected_article_id = None
            st.rerun()
        st.markdown(f"## {article['title']}")
        st.write(article['content'])
        st.stop()

# ---------- Main Routing ----------
if st.session_state.current_page == "Live News":
    st.markdown("## 📡 Live News Feed")
    render_article_feed([i for i in st.session_state.master_db if i['category'] == 'Live News'], "livenews")
elif st.session_state.current_page == "Stories":
    st.markdown("## 📖 Stories Page")
    render_article_feed([i for i in st.session_state.master_db if i['category'] == 'Stories'], "stories")
elif st.session_state.current_page != "Home":
    st.markdown(f"## 📌 {st.session_state.current_page}")
    st.write("Section active.")
    st.stop()

# ---------- Home Dashboard ----------
st.markdown("<h1>QELVYQ — Stories & Real-Time Updates.</h1>", unsafe_allow_html=True)

filtered_articles = st.session_state.master_db
if search_query:
    filtered_articles = [a for a in filtered_articles if search_query.lower() in a['title'].lower()]

render_article_feed(filtered_articles, "home_feed")

# Footer Metrics
m1, m2, m3 = st.columns(3)
with m1: st.metric("Active Visitors", "1 online")
with m2: st.metric("Page Views", f"{st.session_state.page_views:,}")
with m3: st.metric("Active Articles", f"{len(st.session_state.master_db)}")
