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
            "category": "AI", "time_ago": "58 mins ago", "views": "7.8k views", "likes": 3,
            "summary": "Massive infrastructure investments continue as AI labs scale up their compute clusters for next-gen models.",
            "content": "The soaring demand for computational power has triggered talks around massive funding rounds and infrastructure partnerships to secure dedicated GPU capacity for frontier model training.",
            "image": "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=700&q=80",
        },
        {
            "id": 30031,
            "title": "Embedded AI evaluators won't be an easy solution, Hugging Face's policy chief says",
            "category": "Science", "time_ago": "1 hour ago", "views": "6.1k views", "likes": 6,
            "summary": "Experts weigh in on the complexities of placing neutral observers inside AI labs to monitor safety.",
            "content": "Integrating third-party evaluators directly inside model development pipelines introduces unique challenges regarding proprietary data, security protocols, and true neutrality.",
            "image": "https://images.unsplash.com/photo-1507413245164-6160d8298b31?auto=format&fit=crop&w=700&q=80",
        },
        {
            "id": 30041,
            "title": "Microsoft says AI agents are like insider threats as 'frontier models can't be trusted'",
            "category": "Technology", "time_ago": "1 hour ago", "views": "5.4k views", "likes": 7,
            "summary": "Enterprise security teams face new hurdles as autonomous agents gain deeper system access.",
            "content": "As employees increasingly rely on autonomous AI agents connected to corporate systems, Microsoft security analysts warn that these tools must be monitored under strict zero-trust guidelines.",
            "image": "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?auto=format&fit=crop&w=700&q=80",
        },
        {
            "id": 30051,
            "title": "Amazon is taking its biggest shot at Nvidia yet with new TorchNeuron dev tool",
            "category": "Business", "time_ago": "2 hours ago", "views": "8.9k views", "likes": 8,
            "summary": "AWS expands its developer toolkit to make alternative silicon chips more attractive for PyTorch workloads.",
            "content": "Amazon Web Services is pushing further into hardware optimization, releasing toolsets designed to streamline AI application development on alternative silicon platforms.",
            "image": "https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&w=700&q=80",
        }
    ]

# ---------- Sidebar ----------
with st.sidebar:
    st.markdown("""
    <div class="q-brand">
        <div class="q-brand-mark">⚡</div>
        <div>
            <div class="q-brand-name">QELVYQ</div>
            <div class="q-brand-tag">Knowledge in Real Time</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### Navigation")
    nav_options = ["Home", "Live News", "Stories", "AI Assistant", "Analytics", "Bookmarks"]
    selected_nav = st.radio("Navigation Menu", nav_options, label_visibility="collapsed")
    
    if selected_nav != st.session_state.current_page:
        st.session_state.current_page = selected_nav
        st.session_state.selected_article_id = None
        st.rerun()

    st.markdown("---")
    st.markdown("### Search & Filter")
    search_query = st.text_input("Search topics...", placeholder="Type keyword...")
    category_filter = st.selectbox("Category Filter", ["All Categories", "Business", "Technology", "AI", "Science", "World"])

    st.markdown("---")
    st.markdown("### Quick Access")
    if st.button("🔥 Trending Now", use_container_width=True):
        st.toast("Showing trending live stories...")
    if st.button("👁️ Most Viewed", use_container_width=True):
        st.toast("Sorting by highest viewership...")

    st.markdown("""
    <div class="ai-panel">
        <div style="font-size:10px; font-weight:700; color:#64b5f6; letter-spacing:.08em;">QELVYQ AI ASSISTANT</div>
        <h4>Smart Companion</h4>
        <p>Summarize real-time intelligence instantly with conversational context.</p>
    </div>
    """, unsafe_allow_html=True)

# ---------- Dedicated Reader / Detail Page ----------
if st.session_state.current_page == "Home" and st.session_state.selected_article_id is not None:
    article = next((item for item in st.session_state.master_db if item["id"] == st.session_state.selected_article_id), None)
    
    if article:
        if st.button("← Back to Feed"):
            st.session_state.selected_article_id = None
            st.rerun()
            
        col_img, col_txt = st.columns([1, 2])
        with col_img:
            st.image(article["image"], use_container_width=True)
        with col_txt:
            cat_color = "#0878e8" if article["category"] == "Business" else "#7c3aed" if article["category"] == "AI" else "#059669"
            st.markdown(f'<span style="background:{cat_color}; color:#fff; padding:4px 10px; border-radius:20px; font-size:11px; font-weight:700;">{article["category"]}</span>', unsafe_allow_html=True)
            st.markdown(f"## {article['title']}")
            st.markdown(f"**Published:** {article['time_ago']} &nbsp;|&nbsp; **Views:** {article['views']} &nbsp;|&nbsp; **Likes:** {article['likes']}")
            st.markdown("---")
            st.write(article['content'])
            
            b_col1, b_col2 = st.columns(2)
            with b_col1:
                if st.button("❤️ Like Article", use_container_width=True):
                    article['likes'] += 1
                    st.success("Liked successfully!")
                    st.rerun()
            with b_col2:
                if st.button("🔖 Bookmark", use_container_width=True):
                    if article['id'] not in st.session_state.bookmarks:
                        st.session_state.bookmarks.append(article['id'])
                        st.success("Added to bookmarks!")
                    else:
                        st.info("Already in bookmarks.")
        st.stop()

# ---------- Main Content Routing ----------
if st.session_state.current_page == "Live News":
    st.markdown("## 📡 Live News Feeds")
    st.markdown("Real-time automated wire updates from global intelligence feeds.")
    for item in st.session_state.master_db:
        st.markdown(f"- **[{item['category']}]** {item['title']} *({item['time_ago']})*")
    st.stop()

elif st.session_state.current_page == "Stories":
    st.markdown("## 📖 Editorial & Long-form Stories")
    st.markdown("Deep-dive investigative pieces, technical case studies, and industry analysis.")
    for item in st.session_state.master_db:
        st.markdown(f"### {item['title']}")
        st.write(item['summary'])
        st.markdown("---")
    st.stop()

elif st.session_state.current_page == "AI Assistant":
    st.markdown("## 🤖 QELVYQ AI Intelligence Assistant")
    st.markdown("Ask anything about current market trends, technology breakthroughs, or real-time news indexing.")
    user_prompt = st.text_input("Query the live intelligence model...", placeholder="e.g., Summarize today's major AI infrastructure investments")
    if user_prompt:
        st.info(f"Analyzing real-time indices for: **{user_prompt}**...")
        st.success("Based on current data streams, major investments are concentrating heavily on proprietary data centers, specialized silicon development, and high-capacity GPU clusters.")
    st.stop()

elif st.session_state.current_page == "Analytics":
    st.markdown("## 📊 System Telemetry & Analytics")
    st.markdown("Live traffic monitoring, content engagement rates, and platform distribution telemetry.")
    c1, c2, c3 = st.columns(3)
    c1.metric("Platform Uptime", "99.998%", "+0.001%")
    c2.metric("Index Latency", "42 ms", "-4 ms")
    c3.metric("Verified Nodes", "1,240", "+12 active")
    st.stop()

elif st.session_state.current_page == "Bookmarks":
    st.markdown("## 🔖 Your Saved Bookmarks")
    saved_items = [i for i in st.session_state.master_db if i['id'] in st.session_state.bookmarks]
    if not saved_items:
        st.info("No bookmarks saved yet. Click 'Bookmark' inside any article view.")
    else:
        for item in saved_items:
            st.markdown(f"- **{item['title']}** *({item['category']})*")
    st.stop()

# ---------- HOME PAGE DASHBOARD ----------
# Hero Banner
st.markdown(f"""
<div class="hero">
    <div class="hero-status">Mon, 20 Oct 2026 10:25 AM &bull; <span style="color:#4ade80;">● Live</span></div>
    <span class="hero-tag">★ REAL-TIME NEWS AGGREGATOR</span>
    <h1>QELVYQ — Stories & Real-Time Updates.</h1>
    <p>Engaging, short & long stories, moral fables, and live breaking news updates powered by real-time online data.</p>
</div>
""", unsafe_allow_html=True)

# Filter articles based on sidebar search / category
filtered_articles = st.session_state.master_db
if search_query:
    filtered_articles = [a for a in filtered_articles if search_query.lower() in a['title'].lower() or search_query.lower() in a['summary'].lower()]
if category_filter != "All Categories":
    filtered_articles = [a for a in filtered_articles if a['category'].lower() == category_filter.lower()]

# Section Header
col_h1, col_h2 = st.columns([3, 1])
with col_h1:
    st.markdown("""
    <div class="section-head">
        <h3>Latest News & Updates</h3>
    </div>
    <div class="section-sub">Real-time news, technology, business, and more — updated continuously.</div>
    """, unsafe_allow_html=True)
with col_h2:
    st.markdown("""
    <div style="text-align:right; padding-top:10px;">
        <span class="small-pill">All</span> &nbsp;
        <span class="small-pill">News</span> &nbsp;
        <span class="small-pill">Tech</span> &nbsp;
        <span class="small-pill">Business</span>
    </div>
    """, unsafe_allow_html=True)

# News Grid (2 columns layout with images)
if not filtered_articles:
    st.info("No matching articles found based on your filter criteria.")
else:
    cols = st.columns(2)
    for idx, item in enumerate(filtered_articles):
        col = cols[idx % 2]
        with col:
            cat_color = "#0878e8" if item["category"] == "Business" else "#7c3aed" if item["category"] == "AI" else "#059669"
            
            with st.container():
                st.markdown(f"""
                <div class="news-card">
                    <img src="{item['image']}" class="news-image">
                    <div style="margin-top:8px;">
                        <span style="background:{cat_color}; color:#fff; padding:2px 8px; border-radius:12px; font-size:9px; font-weight:700;">{item['category']}</span>
                    </div>
                    <div class="news-title">{item['title']}</div>
                    <div class="news-summary">{item['summary']}</div>
                    <div class="news-meta">⏱ {item['time_ago']} &bull; 👁 {item['views']} &bull; ❤️ {item['likes']} likes</div>
                </div>
                """, unsafe_allow_html=True)
                
                if st.button(f"📖 Read Story (ID: {item['id']})", key=f"btn_read_{item['id']}"):
                    st.session_state.selected_article_id = item['id']
                    st.rerun()

st.markdown("<br>", unsafe_allow_html=True)

# ---------- Metrics Grid (Moved Below Latest News & Updates) ----------
m1, m2, m3, m4, m5 = st.columns(5)
with m1: st.metric("Live Active Visitors", f"{st.session_state.active_users} online", "+12% vs. yesterday")
with m2: st.metric("Total Page Views", f"{st.session_state.page_views:,}", "+18% vs. yesterday")
with m3: st.metric("Est. AdSense Revenue", "$1,006.48 USD", "+24% vs. yesterday")
with m4: st.metric("Total Articles & Tales", f"{len(st.session_state.master_db)} active", "+3 new in last hour")
with m5: st.metric("Live & Verified", "Trusted sources", "Real-time content")

# Footer
st.markdown("""
<div class="footer">
    QELVYQ &bull; Knowledge in Real Time &bull; Powered by Streamlit & Live Data Feeds
</div>
""", unsafe_allow_html=True)
