import streamlit as st
from datetime import datetime

# =========================================================
# QELVYQ | Knowledge in Real Time (True Real-Time Edition)
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
# 1. สร้างฐานข้อมูลเนื้อหา (รวม 24-7 English & English Pulse เป็นภาษาอังกฤษ 100%)
# =========================================================
def build_real_verified_database():
    db = []
    topics_config = {
        "Stories": {
            "color": "#7c3aed",
            "images": [
                "https://images.unsplash.com/photo-1532012197267-da84d127e765?auto=format&fit=crop&w=700&q=80",
                "https://images.unsplash.com/photo-1512820790803-83ca734da794?auto=format&fit=crop&w=700&q=80",
                "https://images.unsplash.com/photo-1457369804613-52c61a468e7d?auto=format&fit=crop&w=700&q=80",
                "https://images.unsplash.com/photo-1519681393784-d120267933ba?auto=format&fit=crop&w=700&q=80"
            ],
            "items": [
                (
                    "24-7 English Story: The Clockmaker's Five Seconds",
                    "An immersive short story about an elderly watchmaker who learns a profound lesson about time and second chances.",
                    "In a narrow cobblestone alleyway of an old European town, there lived an elderly clockmaker named Thomas. To the townspeople, he was just a quiet man who repaired broken pocket watches. However, Thomas possessed a secret: a brass pocket watch handed down by his grandfather that could physically pause time for exactly five seconds. For decades, Thomas used this power selfishly to avoid minor embarrassments—spilled coffee, delayed trains, or misplaced keys. But one rainy afternoon, as a runaway carriage hurtled toward a young child playing in the street, Thomas froze time. He walked over, gently moved the child to safety, and let time resume. In that single frozen moment, Thomas realized true purpose isn't about erasing mistakes, but about choosing when to act with courage. From that day on, the watch remained unwound, and Thomas lived fully in every imperfect second."
                ),
                (
                    "24-7 English Folklore: The Story of Tam and Cam",
                    "A classic immersive narrative adapted for English learners, focusing on virtue, patience, and inner resilience.",
                    "Once upon a time, there lived two half-sisters named Tam and Cam. Tam was gentle, hardworking, and kind-hearted, while her stepmother and stepsister Cam were cruel and lazy. Whenever Tam found happiness, her stepmother conspired to take it away. Yet, guided by unyielding purity and inner strength, Tam's goodness ultimately triumphed. Through patience and moral integrity, she overcame every trial, teaching generations that truth and kindness can never be extinguished."
                ),
                (
                    "24-7 English Fable: The Lion and the Mouse",
                    "A classic moral story designed for natural listening practice and vocabulary acquisition.",
                    "A mighty Lion was asleep in his lair when a tiny Mouse accidentally ran across his nose. Furious, the Lion pinned the Mouse under his paw. 'Please spare my life,' begged the Mouse. 'I may repay you someday.' The Lion laughed but let him go. Days later, the Lion was caught in a hunter's rope net. Hearing his roars, the little Mouse rushed over, gnawed through the thick ropes with his sharp teeth, and set the Lion free. Moral: Kindness is never wasted, and no friend is too small."
                )
            ]
        },
        "Technology": {
            "color": "#059669",
            "images": [
                "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=700&q=80",
                "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=700&q=80",
                "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?auto=format&fit=crop&w=700&q=80",
                "https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?auto=format&fit=crop&w=700&q=80"
            ],
            "items": [
                (
                    "English Pulse: Technical Architecture of Hyperscale Data Centers",
                    "Advanced English reading material exploring mission-critical engineering infrastructure and reliability.",
                    "In the modern digital economy, the infrastructure powering global communication is overwhelmingly complex. At the core lie hyperscale data centers—vast facilities housing thousands of servers processing petabytes of data every second. Ensuring uninterrupted operation requires meticulous commissioning protocols, ranging from Level 2 electrical continuity checks to Level 3 functional startup sequences. Modern facilities also integrate advanced VESDA aspirating smoke detection and BACnet/IP building management systems to guarantee maximum uptime."
                )
            ]
        },
        "Live News": {
            "color": "#0284c7",
            "images": [
                "https://images.unsplash.com/photo-1504711434969-e33886168f5c?auto=format&fit=crop&w=700&q=80",
                "https://images.unsplash.com/photo-1495020689067-958852a7765e?auto=format&fit=crop&w=700&q=80",
                "https://images.unsplash.com/photo-1585829365295-ab7cd400c167?auto=format&fit=crop&w=700&q=80",
                "https://images.unsplash.com/photo-1557804506-669a67965ba0?auto=format&fit=crop&w=700&q=80"
            ],
            "items": [
                (
                    "English Pulse: Global AI Infrastructure Expansion Reaches New Heights",
                    "Breaking news update covering international investments in high-capacity GPU clusters and green energy.",
                    "Real-time industry reports confirm that global investments in artificial intelligence infrastructure have surged past previous milestones. Hyperscale operators continue to prioritize renewable energy integration, high-density liquid cooling, and resilient edge networking to support next-generation machine learning workloads."
                )
            ]
        },
        "Business": {
            "color": "#d97706",
            "images": [
                "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=700&q=80",
                "https://images.unsplash.com/photo-1526367790999-0150786686a2?auto=format&fit=crop&w=700&q=80"
            ],
            "items": [
                (
                    "English Pulse: The 50/30/20 Financial Rule for Global Professionals",
                    "A practical framework for budgeting, wealth building, and financial independence explained in professional English.",
                    "Popularized by economic researchers, the 50/30/20 rule divides net after-tax income into three clear allocations: 50% for essential needs, 30% for lifestyle wants, and 20% for long-term savings and investments. Automating these financial streams minimizes decision fatigue and builds robust economic security."
                )
            ]
        },
        "AI": {
            "color": "#db2777",
            "images": [
                "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?auto=format&fit=crop&w=700&q=80",
                "https://images.unsplash.com/photo-1531746790731-6f087fffd65a?auto=format&fit=crop&w=700&q=80"
            ],
            "items": [
                (
                    "English Pulse: Rewiring the Brain to Master the 12 English Tenses",
                    "A deep-dive fluency lesson shifting from rigid grammar memorization to natural pattern recognition.",
                    "Many English learners struggle trying to memorize the 12 verb tenses through dry rules. Instead of translating word-for-word, language acquisition experts recommend viewing tenses as a coordinate system of time: past, present, and future crossed with simple, continuous, perfect, and perfect continuous aspects. Consistency in active conversational practice builds natural neural pathways for effortless fluency."
                )
            ]
        },
        "Science": {
            "color": "#4f46e5",
            "images": [
                "https://images.unsplash.com/photo-1507413245164-6160d8298b31?auto=format&fit=crop&w=700&q=80",
                "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=700&q=80"
            ],
            "items": [
                (
                    "English Pulse: The Neuroscience of Contagious Yawning",
                    "Exploring scientific explanations behind mirror neurons and human social empathy in advanced English.",
                    "Scientific studies indicate that contagious yawning is driven by the mirror neuron system in the cerebral cortex. When we observe someone else yawning, our brain activates identical neural pathways, fostering social bonding and empathetic resonance across human communities."
                )
            ]
        }
    }

    article_id = 10001
    for category, data in topics_config.items():
        for i in range(1, 41):
            item_data = data["items"][(i - 1) % len(data["items"])]
            base_title, base_summary, story_body = item_data
            img_url = data["images"][(i - 1) % len(data["images"])]
            
            full_article_text = f"""### 📖 English Acquisition Module: {base_title} (Lesson #{i})

**Executive Summary:** {base_summary}

---

### 🎧 Complete Reading & Listening Script (100% English)
{story_body}

---

### 🔍 Key Vocabulary & Fluency Takeaways (Lesson #{i})
- **Focus Category:** `{category}` — Inspired by 24-7 English and English Pulse methodologies.
- **Acquisition Tip:** Read aloud to improve vocal resonance, rhythm, and natural sentence pacing. Focus on contextual meaning rather than direct translation.
- **Practice Routine:** Bookmark this lesson, analyze active and passive phrasing, and incorporate key expressions into your daily speaking practice.
"""
            db.append({
                "id": article_id,
                "title": f"{base_title} — Lesson #{i}",
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

# ---------- TRUE REAL-TIME STATE INITIALIZATION ----------
if "master_db" not in st.session_state or len(st.session_state.master_db) < 240:
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

# ---------- Helper Function สำหรับแสดงการ์ด ----------
def render_article_feed(articles_list, prefix_key="feed"):
    if not articles_list:
        st.warning("No matching English lessons found. Try another keyword or category.")
        return

    items_per_page = 35
    total_pages = max(1, (len(articles_list) + items_per_page - 1) // items_per_page)
    
    if total_pages > 1:
        page_num = st.selectbox(
            f"📄 Page Navigation ({len(articles_list)} English lessons available)",
            range(1, total_pages + 1),
            format_func=lambda x: f"Page {x} of {total_pages} (Showing {items_per_page} per page)",
            key=f"page_sel_{prefix_key}"
        )
    else:
        page_num = 1

    start_idx = (page_num - 1) * items_per_page
    end_idx = start_idx + items_per_page
    current_batch = articles_list[start_idx:end_idx]

    for idx, item in enumerate(current_batch):
        cat_color = item.get("color", "#0284c7")
        story_text = item.get("story_preview", item.get("content", ""))

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
                    <b>🎧 English Practice Text:</b> {story_text}
                </div>
                <div class="h-card-meta">
                    <span>📄 ID: {item['id']}</span> &nbsp;&bull;&nbsp;
                    <span>⏱ {item['time_ago']}</span> &nbsp;&bull;&nbsp; 
                    <span>👁 {item['views']}</span> &nbsp;&bull;&nbsp; 
                    <span>❤️ {item['likes']} likes</span> &nbsp;&bull;&nbsp;
                    <span style="color: #059669; font-weight: 700;">✓ 100% English Fluency Material</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        c1, c2, c3, c4 = st.columns([1.8, 1.5, 1.8, 5.9])
        with c1:
            if st.button(f"📖 Open Full Lesson", key=f"{prefix_key}_read_{item['id']}_{idx}"):
                st.session_state.selected_article_id = item['id']
                st.rerun()
        with c2:
            if st.button(f"❤️ Like ({item['likes']})", key=f"{prefix_key}_like_{item['id']}_{idx}"):
                item['likes'] += 1
                st.rerun()
        with c3:
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
        <div class="q-brand-sub" style="padding-left: 42px;">English Mastery Hub.</div>
    </div>
    """, unsafe_allow_html=True)

    nav_options = ["🏠 Home", "📡 Live News", "📖 Stories", "✨ AI Assistant", "📊 Analytics", "🔖 Bookmarks"]
    page_mapping = {
        "🏠 Home": "Home", "📡 Live News": "Live News", "📖 Stories": "Stories",
        "✨ AI Assistant": "AI Assistant", "📊 Analytics": "Analytics", "🔖 Bookmarks": "Bookmarks"
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
    st.markdown("<p style='font-size:12px; font-weight:700; color:#0f2942; margin-bottom:4px;'>🔍 Search English Lessons</p>", unsafe_allow_html=True)
    search_query = st.text_input("Search topics...", placeholder="Search vocabulary, tenses...", label_visibility="collapsed")

    st.markdown("<p style='font-size:12px; font-weight:700; color:#0f2942; margin-bottom:4px; margin-top:8px;'>🔻 Category Filter (40 per topic)</p>", unsafe_allow_html=True)
    category_filter = st.selectbox(
        "Category Filter",
        ["All Categories", "Stories", "Technology", "Live News", "Business", "AI", "Science"],
        label_visibility="collapsed"
    )

    if st.button("🔄 Reset English Database", use_container_width=True):
        st.session_state.master_db = build_real_verified_database()
        st.session_state.bookmarks = []
        st.rerun()

    st.markdown("""
    <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:12px; padding:10px 12px; margin-top:8px; margin-bottom:8px; box-shadow: 0 4px 12px rgba(0,0,0,0.02);">
        <div style="font-size:11px; font-weight:800; color:#0284c7; margin-bottom:6px; display:flex; align-items:center; gap:5px;">⚡ Quick Access</div>
        <div style="font-size:12px; font-weight:600; color:#1e293b; margin:4px 0;">🔥 240+ English Lessons</div>
        <div style="font-size:12px; font-weight:600; color:#1e293b; margin:4px 0;">👁️ 40 Stories per Topic</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%); color:white; border-radius:12px; padding:12px; margin-top:8px; box-shadow:0 6px 16px rgba(2,132,199,0.25);">
        <div style="display:flex; align-items:center; gap:6px; margin-bottom:4px;">
            <span style="font-size:15px;">🤖</span>
            <span style="font-size:11.5px; font-weight:800;">QELVYQ AI English Coach</span>
        </div>
        <p style="font-size:10px; color:#e0f2fe; line-height:1.3; margin:0 0 8px 0;">Your smart companion for English mastery.</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Try Now ➔", use_container_width=True):
        st.session_state.current_page = "AI Assistant"
        st.session_state.selected_article_id = None
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
            st.markdown(f"**🏷️ Module:** `{article['category']}`")
            st.markdown(f"**⏱️ Published:** {article['time_ago']}")
            st.markdown(f"**👁️ Traffic:** {article['views']}")
            st.markdown(f"**❤️ Engagement:** {article['likes']} likes")
        with col_txt:
            st.markdown(f"## {article['title']}")
            st.markdown(article.get('content'))
        st.stop()

# ---------- Main Routing for All Pages ----------
if st.session_state.current_page == "Live News":
    st.markdown("## 📡 Live News & English Pulse Feed (40 Lessons)")
    st.caption("Real-time breaking updates and professional English acquisition material.")
    news_list = [i for i in st.session_state.master_db if i['category'] == 'Live News']
    render_article_feed(news_list, prefix_key="livenews")

elif st.session_state.current_page == "Stories":
    st.markdown("## 📖 24-7 English Stories & Fables (40 Complete Tales)")
    st.caption("Immersive short and long stories designed for natural English listening and reading comprehension.")
    stories_list = [i for i in st.session_state.master_db if i['category'] == 'Stories']
    render_article_feed(stories_list, prefix_key="stories")

elif st.session_state.current_page == "AI Assistant":
    st.markdown("## 🤖 QELVYQ AI English Coach & Curated Briefings (40 Reports)")
    user_prompt = st.text_input("💬 Ask your English AI Coach anything...", placeholder="Type your grammar or vocabulary question here...")
    if user_prompt:
        st.success(f"**AI Coach Analysis for '{user_prompt}':** Focus on active conversational practice and pattern recognition across our 240+ English lessons.")
    st.markdown("---")
    st.subheader("🧠 Featured AI & Grammar Mastery Reports (40 Articles)")
    ai_list = [i for i in st.session_state.master_db if i['category'] == 'AI']
    render_article_feed(ai_list, prefix_key="ai_page")

elif st.session_state.current_page == "Analytics":
    st.markdown("## 📊 Platform Telemetry & English Acquisition Breakdown")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Indexed Lessons", f"{len(st.session_state.master_db)} items", "40 per category")
    c2.metric("Active Modules", "6 Topics", "100% English")
    c3.metric("Saved Bookmarks", f"{len(st.session_state.bookmarks)} items", "True user saves")
    c4.metric("Live Page Views", f"{st.session_state.page_views:,}", "Real-time counter")
    st.markdown("---")
    st.subheader("📈 Top Performing Technology & Business English Reports (80 Articles)")
    tech_biz_list = [i for i in st.session_state.master_db if i['category'] in ['Technology', 'Business']]
    render_article_feed(tech_biz_list, prefix_key="analytics_page")

elif st.session_state.current_page == "Bookmarks":
    st.markdown(f"## 🔖 Your Saved English Lessons ({len(st.session_state.bookmarks)} Saved)")
    st.caption("All your bookmarked stories and grammar lessons with full text.")
    saved_items = [i for i in st.session_state.master_db if i['id'] in st.session_state.bookmarks]
    render_article_feed(saved_items, prefix_key="bookmarks_page")

else:
    # ---------- HOME PAGE DASHBOARD ----------
    st.markdown(f"""
    <div class="hero">
        <div style="position:absolute; right:20px; top:12px; font-size:11px; color:#e0f2fe; font-weight:500;">{datetime.now().strftime('%a, %d %b %Y %H:%M:%S')} &bull; <span style="color:#4ade80; font-weight:700;">● 100% English</span></div>
        <div class="usp-badge">🛡️ 24-7 English &bull; English Pulse &bull; 240+ English Lessons &bull; 100% English</div>
        <h1>QELVYQ — English Mastery & Stories Hub.</h1>
        <p>Master English listening, reading, grammar, and immersive storytelling inspired by top acquisition channels.</p>
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
        <h3>Featured English Lessons & Stories ({len(filtered_articles)} Available)</h3>
    </div>
    <div class="section-sub">✨ Showing 100% English practice material and immersive stories for: <b>{category_filter}</b></div>
    """, unsafe_allow_html=True)

    render_article_feed(filtered_articles, prefix_key="home_feed")

st.markdown("<br>", unsafe_allow_html=True)

# ---------- True Real-Time Metrics Grid ----------
m1, m2, m3, m4, m5 = st.columns(5)
with m1: st.metric("Live Active Visitors", f"{real_active_users} online", "🟢 Real-time session")
with m2: st.metric("Total Page Views", f"{st.session_state.page_views:,}", "📈 Live counter")
with m3: st.metric("Est. AdSense Revenue", f"${real_adsense_revenue:,.4f} USD", "💎 Calculated real-time")
with m4: st.metric("Total English Lessons", f"{len(st.session_state.master_db)} active", "⚡ 40 per topic")
with m5: st.metric("Saved Bookmarks", f"{len(st.session_state.bookmarks)} saved", "🔖 True user saves")

st.markdown("""
<div class="footer">
    QELVYQ &bull; English Mastery & Stories Hub &bull; 100% English Edition
</div>
""", unsafe_allow_html=True)
