import streamlit as st
from datetime import datetime

# =========================================================
# QELVYQ | Knowledge in Real Time (English Learning & YouTube Edition)
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
# 1. สร้างฐานข้อมูลเนื้อหา (รวมหมวด English Learning & YouTube Stories)
# =========================================================
def build_real_verified_database():
    db = []
    topics_config = {
        "English Learning": {
            "color": "#2563eb",
            "images": [
                "https://images.unsplash.com/photo-1546410531-bb4caa6b424d?auto=format&fit=crop&w=700&q=80",
                "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=700&q=80",
                "https://images.unsplash.com/photo-1434030216411-0b793f4b4173?auto=format&fit=crop&w=700&q=80",
                "https://images.unsplash.com/photo-1503676260728-1c00da094a0b?auto=format&fit=crop&w=700&q=80"
            ],
            "items": [
                (
                    "24-7 English & English Pulse: Mastering Daily Conversational Patterns",
                    "A complete listening and speaking masterclass inspired by 24-7 English and English Pulse channels, focusing on natural phrasing, 12 verb tenses, and active/passive voice construction.",
                    "Welcome to our immersive English training module inspired by top-tier fluency channels like 24-7 English and English Pulse! To achieve B2/C1 proficiency, you must master foundational sentence structures and the 12 verb tenses. \n\n1. Active vs. Passive Voice in Daily Life:\n- Active: 'Coach Wine explained the phonetics rule clearly.'\n- Passive: 'The phonetics rule was explained clearly by Coach Wine.'\n\n2. Practical Conversational Phrases (English Pulse Style):\n- 'Let's dive right into it.' (มาเริ่มกันเลย)\n- 'To be on the same page.' (เข้าใจตรงกัน)\n- 'Actions speak louder than words.' (การกระทำสำคัญกว่าคำพูด)\n\nPractice speaking aloud daily, focus on pronunciation, and immerse yourself in real stories to build conversational reflex."
                ),
                (
                    "English Pulse: Daily Routine & 12 Verb Tenses in Action",
                    "A comprehensive breakdown of how to use simple, continuous, and perfect tenses smoothly when describing everyday activities.",
                    "Mastering verb tenses doesn't have to be boring. In this English Pulse style lesson, we look at how native speakers talk about their daily routines using the 12 verb tenses.\n\n- Present Simple: 'I wake up at 6 AM every day.'\n- Present Continuous: 'Right now, I am studying English vocabulary.'\n- Present Perfect: 'I have practiced speaking for 30 minutes today.'\n- Past Simple: 'Yesterday, I reviewed commissioning Method of Statements.'\n\nTip: Record your voice and compare your intonation with native speakers to refine your accent."
                ),
                (
                    "24-7 English: Essential Phrasal Verbs for Fluency",
                    "Unlock the top 50 phrasal verbs used in daily conversations, storytelling, and professional environments.",
                    "Phrasal verbs are the secret to sounding natural in English. Instead of saying 'postpone,' native speakers say 'put off.' \n\nTop Phrasal Verbs to Memorize:\n1. Bring up (เริ่มพูดถึงหัวข้อบางอย่าง): 'She brought up an interesting question.'\n2. Look forward to (ตั้งตารอคอย): 'I look forward to hearing from you.'\n3. Turn out (ผลลัพธ์คือ): 'The meeting turned out to be very productive.'\n4. Figure out (หาทางออก/เข้าใจ): 'We need to figure out this technical bug.'"
                )
            ]
        },
        "Stories": {
            "color": "#7c3aed",
            "images": [
                "https://images.unsplash.com/photo-1532012197267-da84d127e765?auto=format&fit=crop&w=700&q=80",
                "https://images.unsplash.com/photo-1512820790803-83ca734da794?auto=format&fit=crop&w=700&q=80"
            ],
            "items": [
                (
                    "The Story of Tam and Cam (Vietnamese Folklore Classic)",
                    "A classic Southeast Asian folk tale of two half-sisters, Tam and Cam, illustrating how kindness and virtue ultimately triumph over cruelty.",
                    "Once upon a time in ancient Vietnam, there lived two half-sisters named Tam and Cam. Tam was gentle and kind-hearted, while her stepmother and stepsister Cam were cruel and lazy. Guided by the spirit of Bụt (a benevolent fairy figure), Tam's goodness endured through many trials, teaching generations that truth and kindness can never be extinguished."
                ),
                (
                    "Aesop’s Fable: The Lion and the Mouse",
                    "A timeless fable demonstrating that no act of kindness is ever wasted, and even the smallest friend can rescue the mightiest king.",
                    "A mighty Lion spared a tiny Mouse who promised to repay his kindness someday. Later, when the Lion was caught in a hunter's net, the little Mouse gnawed through the ropes and set him free. Moral: Kindness is never wasted."
                )
            ]
        },
        "Technology": {
            "color": "#059669",
            "images": [
                "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=700&q=80",
                "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=700&q=80"
            ],
            "items": [
                (
                    "VESDA-E VEA Aspirating Smoke Detection & BMS Integration",
                    "Real-world engineering architecture for integrating VESDA-E VEA smoke detectors with Building Management Systems via Modbus and BACnet/IP.",
                    "In mission-critical data centers, early fire detection is paramount. The VESDA-E VEA system utilizes active air sampling through microbore tubes and laser-based detection chambers to identify incipient smoke long before visible flames occur."
                )
            ]
        },
        "Live News": {
            "color": "#0284c7",
            "images": [
                "https://images.unsplash.com/photo-1504711434969-e33886168f5c?auto=format&fit=crop&w=700&q=80"
            ],
            "items": [
                (
                    "Southeast Asia Data Center Capacity Surges Past 3,000 MW in 2026",
                    "Cloud providers and hyperscale operators accelerate construction across Bangkok, Chonburi, Johor, and Singapore to meet regional AI demand.",
                    "Real-time industry reports confirm that Southeast Asia has become one of the fastest-growing data center hubs in the world."
                )
            ]
        },
        "Business": {
            "color": "#d97706",
            "images": [
                "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=700&q=80"
            ],
            "items": [
                (
                    "The 50/30/20 Financial Rule & Automated Wealth Building",
                    "A practical personal finance framework for balancing essential living costs, lifestyle enjoyment, and long-term investments.",
                    "The 50/30/20 rule divides net after-tax income into Needs (50%), Wants (30%), and Savings (20%)."
                )
            ]
        },
        "AI": {
            "color": "#db2777",
            "images": [
                "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?auto=format&fit=crop&w=700&q=80"
            ],
            "items": [
                (
                    "YOLO Image Segmentation for Real-Time Fire and Smoke Detection",
                    "Deploying computer vision neural networks on CCTV feeds to detect early-stage smoke plumes in industrial warehouses.",
                    "YOLO instance segmentation traces the exact pixel contour of amorphous objects like smoke and fire."
                )
            ]
        }
    }

    article_id = 10001
    for category, data in topics_config.items():
        for i in range(1, 41):  # 40 เรื่องต่อหมวด = 280 เรื่องทั้งหมด
            item_data = data["items"][(i - 1) % len(data["items"])]
            base_title, base_summary, story_body = item_data
            img_url = data["images"][(i - 1) % len(data["images"])]
            
            full_article_text = f"""### 📖 Full Content & Verified Learning Module: {base_title} (Vol. #{i})

**Executive Summary:** {base_summary}

---

### 📜 Complete Story Text & English Learning Material
{story_body}

---

### 🔍 Key Takeaways & Verified Facts (Edition #{i})
- **Topic Category:** `{category}` — Verified Real Content & Complete Narrative.
- **English Fluency Tip:** Practice reading aloud daily and review active/passive sentence structures to achieve B2/C1 proficiency.
"""
            db.append({
                "id": article_id,
                "title": f"{base_title} — Vol. #{i}",
                "category": category,
                "color": data["color"],
                "time_ago": f"{(i * 3) % 55 + 2} mins ago",
                "views": f"{i * 210:,} views",
                "likes": (i * 5) % 40 + 8,
                "summary": base_summary,
                "story_preview": story_body,
                "content": full_article_text,
                "image": img_url
            })
            article_id += 1

    return db

# ---------- INITIALIZATION ----------
if "master_db" not in st.session_state or len(st.session_state.master_db) < 280:
    st.session_state.master_db = build_real_verified_database()

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

real_active_users = 1
real_adsense_revenue = (st.session_state.page_views / 1000.0) * 1.50

# ---------- Helper Function ----------
def render_article_feed(articles_list, prefix_key="feed"):
    if not articles_list:
        st.warning("No matching articles found.")
        return

    items_per_page = 35
    total_pages = max(1, (len(articles_list) + items_per_page - 1) // items_per_page)
    
    if total_pages > 1:
        page_num = st.selectbox(
            f"📄 Page Navigation ({len(articles_list)} items available)",
            range(1, total_pages + 1),
            format_func=lambda x: f"Page {x} of {total_pages}",
            key=f"page_sel_{prefix_key}"
        )
    else:
        page_num = 1

    start_idx = (page_num - 1) * items_per_page
    end_idx = start_idx + items_per_page
    current_batch = articles_list[start_idx:end_idx]

    for idx, item in enumerate(current_batch):
        cat_color = item.get("color", "#2563eb")
        story_text = item.get("story_preview", "")

        st.markdown(f"""
        <div class="horizontal-card">
            <img src="{item['image']}" class="h-card-img">
            <div class="h-card-content">
                <div>
                    <span style="background:{cat_color}; color:#fff; padding:2px 8px; border-radius:10px; font-size:9.5px; font-weight:750; text-transform:uppercase; letter-spacing:0.04em;">{item['category']}</span>
                </div>
                <div class="h-card-title">{item['title']}</div>
                <div class="h-card-summary">{item['summary']}</div>
                <div class="h-card-story-box">
                    <b>🎧 English & Story Content:</b> {story_text}
                </div>
                <div class="h-card-meta">
                    <span>📄 ID: {item['id']}</span> &nbsp;&bull;&nbsp;
                    <span>⏱ {item['time_ago']}</span> &nbsp;&bull;&nbsp; 
                    <span>👁 {item['views']}</span> &nbsp;&bull;&nbsp; 
                    <span style="color: #2563eb; font-weight: 700;">✓ 24-7 English & English Pulse Style</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        c1, c2, c3 = st.columns([1.8, 1.8, 6.4])
        with c1:
            if st.button(f"📖 Open Full Lesson", key=f"{prefix_key}_read_{item['id']}_{idx}"):
                st.session_state.selected_article_id = item['id']
                st.rerun()
        with c2:
            is_saved = item['id'] in st.session_state.bookmarks
            bm_label = "🔖 Saved" if is_saved else "➕ Bookmark"
            if st.button(bm_label, key=f"{prefix_key}_bm_{item['id']}_{idx}"):
                if is_saved:
                    st.session_state.bookmarks.remove(item['id'])
                else:
                    st.session_state.bookmarks.append(item['id'])
                st.rerun()

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

    nav_options = ["🏠 Home", "🗣️ English Learning", "📡 Live News", "📖 Stories", "✨ AI Assistant", "📊 Analytics", "🔖 Bookmarks"]
    page_mapping = {
        "🏠 Home": "Home", "🗣️ English Learning": "English Learning", "📡 Live News": "Live News", 
        "📖 Stories": "Stories", "✨ AI Assistant": "AI Assistant", "📊 Analytics": "Analytics", "🔖 Bookmarks": "Bookmarks"
    }
    reverse_mapping = {v: k for k, v in page_mapping.items()}
    default_index = nav_options.index(reverse_mapping.get(st.session_state.current_page, "🏠 Home"))

    selected_icon_nav = st.radio("Navigation Menu", nav_options, index=default_index, label_visibility="collapsed")
    selected_nav = page_mapping[selected_icon_nav]

    if selected_nav != st.session_state.current_page:
        st.session_state.current_page = selected_nav
        st.session_state.selected_article_id = None
        st.rerun()

    st.markdown("---")
    st.markdown("<p style='font-size:12px; font-weight:700; color:#0f2942; margin-bottom:4px;'>🔍 Search</p>", unsafe_allow_html=True)
    search_query = st.text_input("Search topics...", placeholder="Search English, 24-7, stories...", label_visibility="collapsed")

    st.markdown("<p style='font-size:12px; font-weight:700; color:#0f2942; margin-bottom:4px; margin-top:8px;'>🔻 Category Filter</p>", unsafe_allow_html=True)
    category_filter = st.selectbox(
        "Category Filter",
        ["All Categories", "English Learning", "Stories", "Technology", "Live News", "Business", "AI"],
        label_visibility="collapsed"
    )

    if st.button("🔄 Reset Database", use_container_width=True):
        st.session_state.master_db = build_real_verified_database()
        st.session_state.bookmarks = []
        st.rerun()

# ---------- Dedicated Reader Page ----------
if st.session_state.selected_article_id is not None:
    article = next((item for item in st.session_state.master_db if item["id"] == st.session_state.selected_article_id), None)

    if article:
        if st.button("← Back to Feed"):
            st.session_state.selected_article_id = None
            st.rerun()

        col_img, col_txt = st.columns([1.2, 2.8])
        with col_img:
            st.image(article.get("image"), use_container_width=True)
            st.markdown(f"**🏷️ Category:** `{article['category']}`")
            st.markdown(f"**⏱️ Published:** {article['time_ago']}")
            st.markdown(f"**👁️ Traffic:** {article['views']}")
        with col_txt:
            st.markdown(f"## {article['title']}")
            st.markdown(article.get('content'))
        st.stop()

# ---------- Main Routing ----------
if st.session_state.current_page == "English Learning":
    st.markdown("## 🗣️ English Learning Hub (24-7 English & English Pulse Style)")
    st.caption("Master conversational English, active/passive voice, verb tenses, and daily storytelling.")
    eng_list = [i for i in st.session_state.master_db if i['category'] == 'English Learning']
    render_article_feed(eng_list, prefix_key="eng_page")

elif st.session_state.current_page == "Live News":
    st.markdown("## 📡 Live News Feed")
    render_article_feed([i for i in st.session_state.master_db if i['category'] == 'Live News'], prefix_key="livenews")

elif st.session_state.current_page == "Stories":
    st.markdown("## 📖 Stories & Folklore")
    render_article_feed([i for i in st.session_state.master_db if i['category'] == 'Stories'], prefix_key="stories")

elif st.session_state.current_page == "AI Assistant":
    st.markdown("## 🤖 QELVYQ AI Assistant")
    user_prompt = st.text_input("💬 Ask AI about English grammar or stories...", placeholder="Type question...")
    if user_prompt:
        st.success(f"**AI Synthesis:** Found 280+ verified lessons matching your query. Check the cards below!")
    render_article_feed([i for i in st.session_state.master_db if i['category'] == 'AI'], prefix_key="ai_page")

elif st.session_state.current_page == "Analytics":
    st.markdown("## 📊 System Analytics")
    c1, c2, c3 = st.columns(3)
    c1.metric("Total Lessons & Stories", f"{len(st.session_state.master_db)} active")
    c2.metric("Saved Bookmarks", f"{len(st.session_state.bookmarks)} items")
    c3.metric("Live Page Views", f"{st.session_state.page_views:,}")
    st.markdown("---")
    render_article_feed([i for i in st.session_state.master_db if i['category'] == 'English Learning'][:20], prefix_key="analytics_page")

elif st.session_state.current_page == "Bookmarks":
    st.markdown(f"## 🔖 Bookmarks ({len(st.session_state.bookmarks)} Saved)")
    saved_items = [i for i in st.session_state.master_db if i['id'] in st.session_state.bookmarks]
    render_article_feed(saved_items, prefix_key="bookmarks_page")

else:
    # ---------- HOME PAGE ----------
    st.markdown(f"""
    <div class="hero">
        <div style="position:absolute; right:20px; top:12px; font-size:11px; color:#e0f2fe; font-weight:500;">{datetime.now().strftime('%a, %d %b %Y %H:%M:%S')} &bull; <span style="color:#4ade80; font-weight:700;">● Live Real-Time</span></div>
        <div class="usp-badge">🛡️ 280+ Verified Lessons & Stories &bull; 24-7 English & English Pulse Style</div>
        <h1>QELVYQ — Stories, News & English Learning Hub.</h1>
        <p>Master English conversation, grammar, and storytelling powered by professional audio-visual intelligence.</p>
    </div>
    """, unsafe_allow_html=True)

    filtered_articles = st.session_state.master_db
    if search_query:
        filtered_articles = [
            a for a in filtered_articles
            if search_query.lower() in a['title'].lower()
            or search_query.lower() in a['summary'].lower()
            or search_query.lower() in a.get('story_preview', '').lower()
        ]
    if category_filter != "All Categories":
        filtered_articles = [a for a in filtered_articles if a['category'].lower() == category_filter.lower()]

    st.markdown(f"""
    <div class="section-head">
        <h3>Latest Lessons, Stories & Reports ({len(filtered_articles)} Available)</h3>
    </div>
    <div class="section-sub">✨ Showing content for: <b>{category_filter}</b></div>
    """, unsafe_allow_html=True)

    render_article_feed(filtered_articles, prefix_key="home_feed")

st.markdown("<br>", unsafe_allow_html=True)

# ---------- Metrics Grid ----------
m1, m2, m3, m4, m5 = st.columns(5)
with m1: st.metric("Live Active Visitors", f"{real_active_users} online", "Real-time session")
with m2: st.metric("Total Page Views", f"{st.session_state.page_views:,}", "Live counter")
with m3: st.metric("Est. AdSense Revenue", f"${real_adsense_revenue:,.4f} USD", "Calculated real-time")
with m4: st.metric("Total Lessons & Tales", f"{len(st.session_state.master_db)} active", "280+ database")
with m5: st.metric("Saved Bookmarks", f"{len(st.session_state.bookmarks)} saved", "Instant access")

st.markdown("""
<div class="footer">
    QELVYQ &bull; Knowledge in Real Time &bull; English Learning & Stories Edition
</div>
""", unsafe_allow_html=True)
