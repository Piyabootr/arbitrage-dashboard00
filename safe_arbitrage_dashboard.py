import streamlit as st
from datetime import datetime

# =========================================================
# QELVYQ | English Mastery & Stories Hub (100% English Edition)
# =========================================================
st.set_page_config(
    page_title="QELVYQ — English Mastery & Stories Hub",
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
# 1. ฐานข้อมูลภาษาอังกฤษ (24-7 English & English Pulse Inspiration)
# =========================================================
def build_english_learning_database():
    db = []
    topics_config = {
        "24-7 English Stories": {
            "color": "#7c3aed",
            "images": [
                "https://images.unsplash.com/photo-1532012197267-da84d127e765?auto=format&fit=crop&w=700&q=80",
                "https://images.unsplash.com/photo-1512820790803-83ca734da794?auto=format&fit=crop&w=700&q=80",
                "https://images.unsplash.com/photo-1457369804613-52c61a468e7d?auto=format&fit=crop&w=700&q=80",
                "https://images.unsplash.com/photo-1519681393784-d120267933ba?auto=format&fit=crop&w=700&q=80"
            ],
            "items": [
                (
                    "The Clockmaker's Five Seconds (Listening & Reading Practice)",
                    "An intermediate moral story about an elderly watchmaker who learns that time cannot be paused.",
                    "In a narrow cobblestone alleyway of an old European town, there lived an elderly clockmaker named Thomas. To the townspeople, he was just a quiet man who repaired broken pocket watches. However, Thomas possessed a secret: a brass pocket watch handed down by his grandfather that could physically pause time for exactly five seconds. For decades, Thomas used this power selfishly. Whenever he spilled coffee, bumped into someone, or misplaced his keys, he would click the watch and undo his clumsiness. One rainy afternoon, as Thomas walked home from the market, he noticed a runaway carriage hurtling toward a young child playing in the street. Without hesitation, Thomas clicked his brass watch. The rushing horses froze mid-air; the splashing raindrops hung suspended like glass beads. Thomas walked calmly across the wet pavement, gently picked up the child, and carried him safely to the sidewalk. As he walked back, he realized that a second chance at life is precious, but trying to erase every minor mistake robs us of our growth. That evening, Thomas wound the watch one last time and placed it deep inside a wooden box. From that day forward, he lived fully in every imperfect second, accepting both his flaws and the unpredictable flow of time."
                ),
                (
                    "The Architecture of Resilience: Hyperscale Data Centers",
                    "Advanced English reading material exploring technical infrastructure and engineering reliability.",
                    "In the modern digital economy, the infrastructure powering global communication is often invisible yet overwhelmingly complex. At the core of this infrastructure lie hyperscale data centers—vast facilities housing thousands of servers that process petabytes of data every second. However, building a data center is only half the battle; ensuring its uninterrupted operation requires a meticulous engineering process known as commissioning. Commissioning is divided into distinct phases, commonly designated from Level 1 (design review) to Level 5 (integrated systems testing). During Level 2 and Level 3 commissioning, engineering teams verify everything from the continuity of point-to-point electrical wiring to the cause-and-effect matrices of fire alarm systems. Furthermore, safety integration has evolved significantly. Modern facilities rely heavily on advanced aspirating smoke detection systems, such as VESDA-E VEA, which utilize active air sampling through microbore tubes to detect microscopic combustion particles long before visible smoke appears. Ultimately, the reliability of a data center serves as a metaphor for human systems: true resilience is never accidental."
                )
            ]
        },
        "English Pulse Fluency": {
            "color": "#0284c7",
            "images": [
                "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=700&q=80",
                "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?auto=format&fit=crop&w=700&q=80",
                "https://images.unsplash.com/photo-1507413245164-6160d8298b31?auto=format&fit=crop&w=700&q=80",
                "https://images.unsplash.com/photo-1557804506-669a67965ba0?auto=format&fit=crop&w=700&q=80"
            ],
            "items": [
                (
                    "Rewiring the Brain: Mastering the 12 English Tenses",
                    "A professional guide to shifting from memorization to pattern recognition in English grammar.",
                    "Many English learners struggle for years trying to memorize the 12 verb tenses through dry textbook rules. They get trapped in a cycle of translation—thinking in their native language and trying to map it onto English structures. To break free from this pattern, language acquisition experts suggest shifting from memorization to pattern recognition. Instead of treating the 12 tenses as separate rules, view them as a coordinate system of time: past, present, and future crossed with simple, continuous, perfect, and perfect continuous aspects. For example, the Present Perfect tense often causes confusion because learners look for a direct translation. Instead, understand its core concept: a bridge connecting a past action to a present result. When you say, 'I have lost my keys,' the focus is not on when you lost them, but on the fact that you don't have them now. Consistency beats intensity. Spending just fifteen minutes a day engaging in active conversational practice, analyzing active and passive voice constructions, and immersing yourself in native audio content will rewire your neural pathways faster than hours of passive studying."
                ),
                (
                    "Mastering Phrasal Verbs in Natural English Conversations",
                    "Unlock natural fluency by learning how to use common phrasal verbs in daily professional contexts.",
                    "Phrasal verbs are the heartbeat of natural English communication. While textbooks often teach formal vocabulary, native speakers constantly rely on phrasal verbs like 'break down', 'bring up', 'carry out', and 'set up'. The secret to mastering them is learning them in chunks rather than memorizing isolated lists. For instance, instead of studying the verb 'to resolve' in isolation, practice saying 'we need to sort this out'. When you listen to conversational English podcasts or watch native dialogues, pay close attention to prepositional shifts that alter the meaning entirely. Consistent listening and shadowing practice will naturally integrate these expressions into your active vocabulary."
                )
            ]
        }
    }

    article_id = 10001
    for category, data in topics_config.items():
        for i in range(1, 41):  # 40 items per category
            item_data = data["items"][(i - 1) % len(data["items"])]
            base_title, base_summary, story_body = item_data
            img_url = data["images"][(i - 1) % len(data["images"])]
            
            full_article_text = f"""### 📖 English Learning Module: {base_title} (Part #{i})

**Overview & Objective:** {base_summary}

---

### 🎧 Listening & Reading Practice Text (100% English)
{story_body}

---

### 📝 Key Vocabulary & Grammar Takeaways (Edition #{i})
- **Category:** `{category}` — Designed for English acquisition, listening practice, and reading fluency.
- **Practice Tip:** Read the text aloud to improve pronunciation and intonation. Pay close attention to verb tenses, sentence structures, and natural phrasing.
- **Skill Builder:** Bookmark this lesson to review key vocabulary and test your comprehension daily.
"""
            db.append({
                "id": article_id,
                "title": f"{base_title} — Lesson #{i}",
                "category": category,
                "color": data["color"],
                "time_ago": f"{(i * 2) % 50 + 1} mins ago",
                "views": f"{i * 190:,} views",
                "likes": (i * 4) % 35 + 5,
                "summary": base_summary,
                "story_preview": story_body,
                "content": full_article_text,
                "image": img_url
            })
            article_id += 1

    return db

# ---------- Initialization ----------
if "master_db" not in st.session_state or len(st.session_state.master_db) < 80:
    st.session_state.master_db = build_english_learning_database()

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

    items_per_page = 30
    total_pages = max(1, (len(articles_list) + items_per_page - 1) // items_per_page)
    
    if total_pages > 1:
        page_num = st.selectbox(
            f"📄 Page Navigation ({len(articles_list)} English lessons available)",
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
        cat_color = item.get("color", "#0284c7")
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
                    <b>🎧 English Text Preview:</b> {story_text}
                </div>
                <div class="h-card-meta">
                    <span>📄 ID: {item['id']}</span> &nbsp;&bull;&nbsp;
                    <span>⏱ {item['time_ago']}</span> &nbsp;&bull;&nbsp; 
                    <span>👁 {item['views']}</span> &nbsp;&bull;&nbsp; 
                    <span style="color: #059669; font-weight: 700;">✓ 100% English Practice</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        c1, c2, c3 = st.columns([1.5, 1.5, 7])
        with c1:
            if st.button(f"📖 Read Lesson", key=f"{prefix_key}_read_{item['id']}_{idx}"):
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
        <div class="q-brand-sub" style="padding-left: 42px;">English Mastery Hub.</div>
    </div>
    """, unsafe_allow_html=True)

    nav_options = ["🏠 Home", "🎧 24-7 Stories", "💬 English Pulse", "✨ AI Coach", "🔖 Bookmarks"]
    page_mapping = {
        "🏠 Home": "Home",
        "🎧 24-7 Stories": "24-7 English Stories",
        "💬 English Pulse": "English Pulse Fluency",
        "✨ AI Coach": "AI Assistant",
        "🔖 Bookmarks": "Bookmarks"
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
    st.markdown("<p style='font-size:12px; font-weight:700; color:#0f2942; margin-bottom:4px;'>🔍 Search Lessons</p>", unsafe_allow_html=True)
    search_query = st.text_input("Search", placeholder="Search vocabulary, tenses...", label_visibility="collapsed")

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
            st.markdown(f"**⏱️ Duration:** {article['time_ago']}")
            st.markdown(f"**👁️ Views:** {article['views']}")
        with col_txt:
            st.markdown(f"## {article['title']}")
            st.markdown(article.get('content'))
        st.stop()

# ---------- Main Routing ----------
if st.session_state.current_page == "24-7 English Stories":
    st.markdown("## 🎧 24-7 English: Immersive Stories & Articles")
    st.caption("Engaging moral fables and deep-dive reading material designed for natural English acquisition.")
    render_article_feed([i for i in st.session_state.master_db if i['category'] == '24-7 English Stories'], "stories_page")

elif st.session_state.current_page == "English Pulse Fluency":
    st.markdown("## 💬 English Pulse: Grammar, Phrasal Verbs & Fluency")
    st.caption("Master conversational phrasing, verb tenses, and professional vocabulary.")
    render_article_feed([i for i in st.session_state.master_db if i['category'] == 'English Pulse Fluency'], "pulse_page")

elif st.session_state.current_page == "AI Assistant":
    st.markdown("## ✨ QELVYQ AI English Coach")
    user_prompt = st.text_input("💬 Ask your English AI Coach any grammar or vocabulary question...", placeholder="e.g., Explain the difference between Present Perfect and Past Simple")
    if user_prompt:
        st.success(f"**AI Coach Analysis for '{user_prompt}':** Focus on core structural patterns and active conversational practice. Review our 80+ lessons in the feed for targeted examples.")
    st.markdown("---")
    render_article_feed(st.session_state.master_db[:20], "ai_page")

elif st.session_state.current_page == "Bookmarks":
    st.markdown(f"## 🔖 Your Saved Lessons ({len(st.session_state.bookmarks)} Saved)")
    saved_items = [i for i in st.session_state.master_db if i['id'] in st.session_state.bookmarks]
    render_article_feed(saved_items, "bookmarks_page")

else:
    # ---------- HOME DASHBOARD ----------
    st.markdown(f"""
    <div class="hero">
        <div style="position:absolute; right:20px; top:12px; font-size:11px; color:#e0f2fe; font-weight:500;">{datetime.now().strftime('%a, %d %b %Y')} &bull; <span style="color:#4ade80; font-weight:700;">● 100% English</span></div>
        <div class="usp-badge">🛡️ 24-7 English &bull; English Pulse &bull; 100% English Practice</div>
        <h1>QELVYQ — English Mastery & Stories Hub.</h1>
        <p>Master English listening, reading, grammar, and storytelling inspired by top acquisition channels.</p>
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

    st.markdown(f"""
    <div class="section-head">
        <h3>Featured English Lessons & Stories ({len(filtered_articles)} Available)</h3>
    </div>
    <div class="section-sub">✨ Immersive reading material and grammar guides in 100% English.</div>
    """, unsafe_allow_html=True)

    render_article_feed(filtered_articles, "home_feed")

st.markdown("<br>", unsafe_allow_html=True)

# ---------- Metrics Grid ----------
m1, m2, m3, m4 = st.columns(4)
with m1: st.metric("Live Active Visitors", f"{real_active_users} online", "🟢 Active session")
with m2: st.metric("Total Page Views", f"{st.session_state.page_views:,}", "📈 Live counter")
with m3: st.metric("Total English Lessons", f"{len(st.session_state.master_db)} active", "⚡ 100% English")
with m4: st.metric("Saved Bookmarks", f"{len(st.session_state.bookmarks)} saved", "🔖 Instant access")

st.markdown("""
<div class="footer">
    QELVYQ &bull; English Mastery & Stories Hub &bull; 100% English Edition
</div>
""", unsafe_allow_html=True)
