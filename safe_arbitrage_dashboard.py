import streamlit as st
from datetime import datetime

# =========================================================
# QELVYQ | Knowledge & English Learning Hub (24-7 English & English Pulse Edition)
# =========================================================
st.set_page_config(
    page_title="QELVYQ — English Learning & Real-Time Updates",
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
# 1. สร้างฐานข้อมูลเนื้อหา (รวม 24-7 English และ English Pulse)
# =========================================================
def build_english_learning_database():
    db = []
    topics_config = {
        "24-7 English (Stories)": {
            "color": "#7c3aed",
            "images": [
                "https://images.unsplash.com/photo-1532012197267-da84d127e765?auto=format&fit=crop&w=700&q=80",
                "https://images.unsplash.com/photo-1512820790803-83ca734da794?auto=format&fit=crop&w=700&q=80",
                "https://images.unsplash.com/photo-1457369804613-52c61a468e7d?auto=format&fit=crop&w=700&q=80"
            ],
            "items": [
                (
                    "Always Talk English | Graded Reader & Learn English Through Stories",
                    "A guided conversational story designed to boost your daily speaking confidence and listening fluency.",
                    "Transcript & Story Practice:\n\n'How do you usually start your day?' Sarah asked her colleague during their morning coffee break. Instead of translating from Thai in her head, Sarah practiced thinking directly in English. 'I wake up early, brew a cup of hot coffee, and review my daily tasks.' By repeating simple sentence structures and active verb tenses every day, speaking English becomes second nature. Practice speaking aloud even when you are alone to train your vocal muscles."
                ),
                (
                    "Think Easier and Speak Better in English | Graded Reader Fast Practice",
                    "Master the art of eliminating mental translation and speaking fluidly without hesitation.",
                    "Transcript & Story Practice:\n\nMany English learners struggle because they translate word-for-word from their native language. To speak fluently, you must learn basic sentence patterns: Subject + Verb + Object. When you see an object, describe it directly in English ('This is a blue cup'). Over time, your brain creates direct neural pathways for English, allowing you to respond instantly in conversations without freezing up."
                ),
                (
                    "How to Introduce Yourself in English Confidently | Step-by-Step Guide",
                    "A step-by-step graded listening lesson on making a powerful first impression in professional and social settings.",
                    "Transcript & Story Practice:\n\n'Hello everyone, my name is Piyabutt. I am a data center commissioning engineer based in Bangkok.' When introducing yourself, keep it clear, confident, and engaging. Mention your current profession, a key project you are managing (such as TOPAZ BKK2 commissioning method statements), and one personal hobby. Smile, make eye contact, and speak at a steady, relaxed pace."
                )
            ]
        },
        "English Pulse (Real-World Phrasal Verbs)": {
            "color": "#059669",
            "images": [
                "https://images.unsplash.com/photo-1554224155-8d04cb21cd6c?auto=format&fit=crop&w=700&q=80",
                "https://images.unsplash.com/photo-1526367790999-0150786686a2?auto=format&fit=crop&w=700&q=80",
                "https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?auto=format&fit=crop&w=700&q=80"
            ],
            "items": [
                (
                    "Stop Saying 'I Want' at a Hotel! | Travel English & Phrasal Verbs",
                    "Learn natural conversational alternatives used by native speakers when checking into hotels and ordering services.",
                    "Lesson Breakdown:\n\nSaying 'I want a room key' can sound too demanding in English. Instead, use polite phrasal verbs and modal phrases: 'Could I please check in?' or 'I'd like to pick up my room key.' In English Pulse episodes, we explore how softening your tone with words like 'Could', 'Would', and 'I'm hoping to' instantly transforms your hospitality English from rude to polite and natural."
                ),
                (
                    "Wake Up vs. Get Up in 40 Seconds | Morning Routine Phrasal Verbs",
                    "Clarify the subtle differences between waking up and getting out of bed using daily routine scenarios.",
                    "Lesson Breakdown:\n\n- Wake Up: The exact moment your eyes open and you are no longer sleeping (e.g., 'I woke up at 6:00 AM today').\n- Get Up: The physical action of getting out of bed and standing up (e.g., 'I got up at 6:15 AM after checking my phone'). Mastering these small phrasal verb distinctions makes your daily storytelling sound authentic and native."
                ),
                (
                    "The 4 Meanings of 'TAKE OFF' Natives Hide From You! | Spoken English",
                    "Unlock multiple meanings of essential phrasal verbs for daily office and casual conversations.",
                    "Lesson Breakdown:\n\n1. Aircraft departure ('Our flight takes off at 9 PM').\n2. Removing clothing or shoes ('Please take off your jacket').\n3. Becoming suddenly successful ('Her online business really took off').\n4. Leaving a place abruptly ('I have to take off now for a meeting'). Learning phrasal verbs in context is the fastest route to B2/C1 fluency."
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
                    "The Story of Tam and Cam (Vietnamese Folklore Classic in English)",
                    "A classic folk tale of two half-sisters, illustrating how kindness and virtue ultimately triumph over cruelty.",
                    "Once upon a time in ancient Vietnam, there lived two half-sisters named Tam and Cam. Tam was gentle and kind, while Cam was lazy and cruel. Through patience and the help of a benevolent spirit, Tam's goodness ultimately brought her happiness and justice. A timeless story of moral resilience."
                )
            ]
        },
        "Technology": {
            "color": "#0284c7",
            "images": [
                "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=700&q=80"
            ],
            "items": [
                (
                    "VESDA-E VEA Aspirating Smoke Detection & BMS Integration",
                    "Engineering architecture for integrating VESDA-E VEA smoke detectors with Building Management Systems.",
                    "In mission-critical data centers, early fire detection is vital. Integrating VESDA aspirating smoke detectors with BMS via Modbus and Moxa gateways ensures rapid hazard response."
                )
            ]
        }
    }

    article_id = 10001
    for category, data in topics_config.items():
        for i in range(1, 41):  # 40 เรื่องต่อหมวด
            item_data = data["items"][(i - 1) % len(data["items"])]
            base_title, base_summary, story_body = item_data
            img_url = data["images"][(i - 1) % len(data["images"])]
            
            full_article_text = f"""### 🎧 Audio & Graded Reader Practice: {base_title} (Vol. #{i})

**Overview / Objective:** {base_summary}

---

### 📚 Lesson Content & Story Transcript
{story_body}

---

### 💡 Language Study Tips & Active Practice (Edition #{i})
- **Focus Area:** `{category}` — Designed for English listening, speaking, and vocabulary retention.
- **Action Item:** Read the transcript aloud three times. Focus on pronunciation, intonation, and active/passive voice patterns.
- **Fluency Goal:** Think directly in English without translating into your native language.
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

# ---------- Initialization ----------
if "master_db" not in st.session_state or len(st.session_state.master_db) < 160:
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
        st.warning("No matching lessons found.")
        return

    items_per_page = 35
    total_pages = max(1, (len(articles_list) + items_per_page - 1) // items_per_page)
    
    if total_pages > 1:
        page_num = st.selectbox(
            f"📄 Page Navigation ({len(articles_list)} lessons available)",
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
        cat_color = item.get("color", "#0878e8")
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
                    <b>🎧 Transcript & Practice Text:</b> {story_text}
                </div>
                <div class="h-card-meta">
                    <span>📄 ID: {item['id']}</span> &nbsp;&bull;&nbsp;
                    <span>⏱ {item['time_ago']}</span> &nbsp;&bull;&nbsp; 
                    <span>👁 {item['views']}</span> &nbsp;&bull;&nbsp; 
                    <span>❤️ {item['likes']} likes</span> &nbsp;&bull;&nbsp;
                    <span style="color: #059669; font-weight: 700;">✓ English Practice Ready</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        c1, c2, c3, c4 = st.columns([1.8, 1.5, 1.8, 5.9])
        with c1:
            if st.button(f"🎧 Practice Lesson", key=f"{prefix_key}_read_{item['id']}_{idx}"):
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
        <div class="q-brand-sub" style="padding-left: 42px;">English & Real-Time Hub.</div>
    </div>
    """, unsafe_allow_html=True)

    nav_options = ["🏠 Home", "🎧 24-7 English", "⚡ English Pulse", "📖 Stories", "✨ AI Assistant", "🔖 Bookmarks"]
    page_mapping = {
        "🏠 Home": "Home", "🎧 24-7 English": "24-7 English (Stories)", "⚡ English Pulse": "English Pulse (Real-World Phrasal Verbs)",
        "📖 Stories": "Stories", "✨ AI Assistant": "AI Assistant", "🔖 Bookmarks": "Bookmarks"
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
    search_query = st.text_input("🔍 Search Lessons", placeholder="Search phrasal verbs, stories...", label_visibility="collapsed")
    
    category_filter = st.selectbox(
        "Category Filter",
        ["All Categories", "24-7 English (Stories)", "English Pulse (Real-World Phrasal Verbs)", "Stories", "Technology"],
        label_visibility="collapsed"
    )

    if st.button("🔄 Reset English Database", use_container_width=True):
        st.session_state.master_db = build_english_learning_database()
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
            st.markdown(f"**🏷️ Track:** `{article['category']}`")
            st.markdown(f"**⏱️ Duration:** {article['time_ago']}")
            st.markdown(f"**👁️ Learners:** {article['views']}")
        with col_txt:
            st.markdown(f"## {article['title']}")
            st.markdown(article.get('content'))
        st.stop()

# ---------- Main Routing ----------
if st.session_state.current_page == "24-7 English (Stories)":
    st.markdown("## 🎧 24-7 English — Graded Reader & Story Listening")
    st.caption("Master English through engaging stories, practical learning tips, and natural listening practice available 24/7.")
    list_247 = [i for i in st.session_state.master_db if i['category'] == '24-7 English (Stories)']
    render_article_feed(list_247, prefix_key="247eng")

elif st.session_state.current_page == "English Pulse":
    st.markdown("## ⚡ English Pulse — Phrasal Verbs & Real-World Situations")
    st.caption("Learn natural conversational phrasal verbs, idioms, and situational English for B1-B2 learners.")
    list_pulse = [i for i in st.session_state.master_db if i['category'] == 'English Pulse (Real-World Phrasal Verbs)']
    render_article_feed(list_pulse, prefix_key="engpulse")

elif st.session_state.current_page == "AI Assistant":
    st.markdown("## 🤖 QELVYQ English Fluency Coach")
    user_prompt = st.text_input("💬 Ask AI for English sentence corrections or vocabulary explanations...", placeholder="e.g., Explain the difference between wake up and get up")
    if user_prompt:
        st.success(f"**AI Fluency Analysis:** Great question! When discussing '{user_prompt}', remember that consistency in daily listening and active speaking practice is the key to B2/C1 mastery.")
    st.markdown("---")
    st.subheader("📚 Recommended Practice Lessons")
    render_article_feed(st.session_state.master_db[:20], prefix_key="ai_page")

elif st.session_state.current_page == "Bookmarks":
    st.markdown(f"## 🔖 Your Saved Lessons ({len(st.session_state.bookmarks)} Saved)")
    saved_items = [i for i in st.session_state.master_db if i['id'] in st.session_state.bookmarks]
    render_article_feed(saved_items, prefix_key="bookmarks_page")

else:
    # ---------- HOME PAGE DASHBOARD ----------
    st.markdown(f"""
    <div class="hero">
        <div style="position:absolute; right:20px; top:12px; font-size:11px; color:#e0f2fe; font-weight:500;">{datetime.now().strftime('%a, %d %b %Y %H:%M:%S')} &bull; <span style="color:#4ade80; font-weight:700;">● Active Practice</span></div>
        <div class="usp-badge">🎧 24-7 English &bull; ⚡ English Pulse &bull; Complete Transcripts</div>
        <h1>QELVYQ — English Learning & Real-Time Hub.</h1>
        <p>Master conversational English naturally through graded stories, phrasal verbs, and immersive listening transcripts.</p>
    </div>
    """, unsafe_allow_html=True)

    filtered_articles = st.session_state.master_db
    if search_query:
        filtered_articles = [
            a for a in filtered_articles
            if search_query.lower() in a['title'].lower()
            or search_query.lower() in a['summary'].lower()
        ]
    if category_filter != "All Categories":
        filtered_articles = [a for a in filtered_articles if a['category'].lower() == category_filter.lower()]

    st.markdown(f"""
    <div class="section-head">
        <h3>English Learning Feeds ({len(filtered_articles)} Lessons Available)</h3>
    </div>
    <div class="section-sub">✨ Showing listening transcripts and practice cards for: <b>{category_filter}</b></div>
    """, unsafe_allow_html=True)

    render_article_feed(filtered_articles, prefix_key="home_feed")

st.markdown("<br>", unsafe_allow_html=True)

# Footer Metrics
m1, m2, m3, m4, m5 = st.columns(5)
with m1: st.metric("Active Learners", f"{real_active_users} online", "🟢 Real-time session")
with m2: st.metric("Total Lessons Read", f"{st.session_state.page_views:,}", "📈 Live counter")
with m3: st.metric("Est. AdSense Revenue", f"${real_adsense_revenue:,.4f} USD", "💎 Calculated real-time")
with m4: st.metric("Active Audio Tracks", f"{len(st.session_state.master_db)} active", "⚡ Ready to study")
with m5: st.metric("Saved Lessons", f"{len(st.session_state.bookmarks)} saved", "🔖 Instant access")

st.markdown("""
<div class="footer">
    QELVYQ &bull; English Learning & Real-Time Intelligence Edition
</div>
""", unsafe_allow_html=True)
