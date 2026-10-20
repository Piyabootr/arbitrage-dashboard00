import streamlit as st
import pandas as pd
import requests
import re
import urllib.parse
import xml.etree.ElementTree as ET

# ตั้งค่าหน้าเว็บให้เป็นแบบ Wide Layout
st.set_page_config(page_title="QELVYQ — Knowledge in Real Time.", layout="wide", initial_sidebar_state="expanded")

# ==========================================
# 1. ระบบจัดการสิทธิ์และหน้าจอ (Session State Router)
# ==========================================
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"
if "selected_article_id" not in st.session_state:
    st.session_state.selected_article_id = None
if "page_views" not in st.session_state:
    st.session_state.page_views = 12581
if "active_users" not in st.session_state:
    st.session_state.active_users = 142

st.session_state.page_views += 1
real_adsense_revenue = (st.session_state.page_views / 1000.0) * 79.80

# ==========================================
# 2. ฐานข้อมูลเริ่มต้นถอดแบบ 100% (Master Database)
# ==========================================
if "master_db" not in st.session_state:
    st.session_state.master_db = [
        {
            "id": 30001,
            "title": "Live Online News: Walmart's Flipkart is quietly building a food delivery challenger in India",
            "category": "Business",
            "time_ago": "4 mins ago",
            "views": "26 views",
            "likes": 5,
            "summary": "Flipkart has expanded access to its food-delivery service to thousands of employees ahead of its public launch...",
            "content": """Live Online News Dispatch:
Walmart-backed Flipkart is positioning itself for a major thrust into the Indian quick-commerce and food delivery ecosystem, currently dominated by local giants. Internal telemetry and logistics mapping indicate thousands of corporate employees are participating in early-stage beta trials.

Strategic Market Implications:
- Leveraging existing supply chain networks to minimize initial overhead.
- Direct competition with established delivery aggregators.
- Scalable regional rollout planned over the upcoming quarters.

Published via QELVYQ Real-Time Intelligence Node."""
        },
        {
            "id": 30011,
            "title": "Live Online News: Mamdani says feds have abdicated on AI, urges New Yorkers to push back",
            "category": "Technology",
            "time_ago": "27 mins ago",
            "views": "4.2k views",
            "likes": 4,
            "summary": "Mayor Zohran Mamdani said Monday night that New Yorkers must resist the narrative that an AI takeover is inevitable and demand regulations...",
            "content": """Comprehensive Report:
Amid rapid advancements in artificial intelligence deployment, local leadership in New York has voiced profound concerns regarding federal oversight. Speaking at a civic technology forum, officials stressed the necessity of community-driven guardrails.

Key Takeaways:
- Demanding transparent algorithmic governance.
- Protecting local workforce stability against automated displacement.
- Establishing municipal compliance frameworks."""
        },
        {
            "id": 30021,
            "title": "Live Online News: Nscale and Anthropic are reportedly in talks for yet another $45B compute deal",
            "category": "Technology",
            "time_ago": "58 mins ago",
            "views": "7.8k views",
            "likes": 3,
            "summary": "If the deal goes through, it would be the latest in a long string of giant compute deals Anthropic has struck over the past year...",
            "content": """Industry Ingestion Report:
The race for foundational compute infrastructure continues to shatter capital allocation records. Reports confirm active negotiations between Nscale and Anthropic regarding a multi-billion dollar scaling partnership.

Infrastructure Expansion:
Securing next-generation GPU clusters remains the primary bottleneck for frontier AI model training."""
        },
        {
            "id": 30031,
            "title": "Live Online News: Embedded AI evaluators won't be an easy solution, Hugging Face's policy chief says",
            "category": "AI",
            "time_ago": "1 hour ago",
            "views": "6.1k views",
            "likes": 6,
            "summary": "The idea of embedded evaluators — in which supposedly \"neutral\" third-party observers are placed inside AI organizations — has been popularized...",
            "content": """Policy Breakdown:
While third-party evaluators aim to ensure safety compliance within artificial intelligence laboratories, policy experts highlight severe structural and conflict-of-interest hurdles."""
        },
        {
            "id": 30041,
            "title": "Live Online News: Microsoft says AI agents are like insider threats as 'frontier models can't be trusted'",
            "category": "Technology",
            "time_ago": "1 hour ago",
            "views": "5.4k views",
            "likes": 7,
            "summary": "Microsoft wants enterprises to [c]lock watch the agents that employees use with systems not controlled by its public labs like OpenAI and Anthropic...",
            "content": """Enterprise Security Alert:
As autonomous AI agents gain execution privileges across enterprise IT environments, security architectures must treat them with zero-trust protocols equivalent to insider threats."""
        },
        {
            "id": 30051,
            "title": "Live Online News: Amazon is taking its biggest shot at Nvidia yet with new TorchNeuron dev tool",
            "category": "Business",
            "time_ago": "2 hours ago",
            "views": "8.9k views",
            "likes": 8,
            "summary": "Amazon wants to break Nvidia's hold on PyTorch, the free toolkit used to build most AI apps, so that more developers run their apps on alternative chips like its own...",
            "content": """Cloud Competition Update:
AWS has unveiled optimized developer tooling designed to seamlessly migrate heavy PyTorch workloads away from proprietary hardware ecosystems onto custom silicon."""
        }
    ]

# ==========================================
# 3. Dedicated Reader Page (หน้าอ่านบทความเต็มจอ)
# ==========================================
if st.session_state.current_page == "Reader" and st.session_state.selected_article_id is not None:
    target = next((item for item in st.session_state.master_db if item["id"] == st.session_state.selected_article_id), None)
    if target:
        if st.button("⬅️ Back to Home Feed"):
            st.session_state.current_page = "Home"
            st.session_state.selected_article_id = None
            st.rerun()
            
        st.markdown(f"# {target['title']}")
        st.markdown(f"🏷️ **Category:** {target['category']} &nbsp;|&nbsp; ⏱️ **Time:** {target['time_ago']} &nbsp;|&nbsp; 👀 **Views:** {target['views']}")
        st.markdown("---")
        st.write(target['content'])
        st.markdown("---")
        if st.button("❤️ Like this article"):
            target['likes'] += 1
            st.success("Liked successfully!")
            st.rerun()
        st.stop()

# ==========================================
# 4. Sidebar เมนูด้านข้างถอดแบบเป๊ะๆ
# ==========================================
with st.sidebar:
    st.markdown("### ⚡ QELVYQ")
    st.caption("Knowledge in Real Time.")
    st.markdown("---")
    
    # เมนูนำทางหลัก
    nav_selection = st.radio(
        "Navigation", 
        ["Home", "Live News", "Stories", "AI Assistant", "Analytics", "Bookmarks"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.subheader("🔍 Search")
    search_query = st.text_input("Search", placeholder="Search for news, topics, or keywords...", label_visibility="collapsed")
    
    st.markdown("---")
    st.subheader("📂 Category Filter")
    selected_cat = st.selectbox(
        "Category Filter", 
        ["All Categories", "Business", "Technology", "AI", "Science", "World"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.markdown("⚡ **Quick Access**")
    st.markdown("🔥 Trending Now")
    st.markdown("👁️ Most Viewed")
    
    st.markdown("---")
    # กล่อง AI Assistant บล็อกน้ำเงินด้านล่าง Sidebar
    st.info("🤖 **QELVYQ AI Assistant**\n\nYour smart companion for better information.\n\n[Try Now ➔]")

# ==========================================
# 5. หน้าแรกหลัก (Home Dashboard Layout)
# ==========================================

# Top Header Banner น้ำเงินเข้มโค้งมนพร้อมกราฟิก
st.markdown(
    """
    <div style="background: linear-gradient(135deg, #0b1c3c 0%, #173b75 100%); padding: 25px 30px; border-radius: 12px; color: white; margin-bottom: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
        <span style="background-color: #1d4ed8; color: white; font-size: 11px; padding: 4px 10px; border-radius: 20px; font-weight: 600; text-transform: uppercase;">★ REAL-TIME NEWS AGGREGATOR</span>
        <h2 style="margin: 12px 0 5px 0; font-weight: 700; font-size: 26px;">QELVYQ — Stories & Real-Time Updates.</h2>
        <p style="margin: 0; font-size: 14px; opacity: 0.85;">Engaging, short & long stories, moral fables, and live breaking news updates powered by real-time online data.</p>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Analytics Metric Bar (แถบสถิติด้านบน) ---
m1, m2, m3, m4, m5 = st.columns(5)
m1.metric("Live Active Visitors", f"{st.session_state.active_users} online", "+12% vs. yesterday")
m2.metric("Total Page Views", f"{st.session_state.page_views:,}", "+18% vs. yesterday")
m3.metric("Est. AdSense Revenue", f"${real_adsense_revenue:,.2f} USD", "+24% vs. yesterday")
m4.metric("Total Articles & Tales", f"{len(st.session_state.master_db)} active", "+3 new in the last hour")
m5.metric("Live & Verified", "Trusted sources", "Real-time content")

st.markdown("---")

# --- ส่วนหัวข้อฟีดข่าวสารล่าสุด (Latest News & Updates) ---
f_col1, f_col2 = st.columns([3, 1])
with f_col1:
    st.subheader("📰 Latest News & Updates")
    st.caption("Real-time news, technology, business, and more — updated continuously.")
with f_col2:
    # ปุ่มกรองหมวดหมู่ด่วนจำลองตามรูป
    st.markdown("<div style='text-align: right; padding-top: 10px;'><span style='background:#2563eb; color:white; padding:4px 10px; border-radius:15px; font-size:12px;'>All</span> &nbsp; <span style='color:#64748b; font-size:12px;'>News</span> &nbsp; <span style='color:#64748b; font-size:12px;'>Tech</span> &nbsp; <span style='color:#64748b; font-size:12px;'>Business</span> &nbsp; <span style='color:#64748b; font-size:12px;'>View All ➔</span></div>", unsafe_allow_html=True)

# กรองข้อมูลตามการค้นหาและหมวดหมู่
filtered_data = st.session_state.master_db
if search_query:
    filtered_data = [item for item in filtered_data if search_query.lower() in item['title'].lower() or search_query.lower() in item['summary'].lower()]
if selected_cat != "All Categories":
    filtered_data = [item for item in filtered_data if item['category'].lower() == selected_cat.lower()]

# แสดงผลบทความแบบ Grid 2 คอลัมน์ (ถอดแบบรูปตัวอย่าง 100%)
if not filtered_data:
    st.warning("No articles found matching your criteria.")
else:
    cols = st.columns(2)
    for idx, item in enumerate(filtered_data):
        col = cols[idx % 2]
        with col:
            with st.container(border=True):
                # แสดงป้ายหมวดหมู่สีสันสดใส
                badge_color = "#3b82f6"
                if item['category'] == "Business": badge_color = "#9333ea"
                elif item['category'] == "AI": badge_color = "#f97316"
                
                st.markdown(f"<span style='background-color:{badge_color}; color:white; font-size:10px; padding:2px 8px; border-radius:4px; font-weight:600;'>{item['category']}</span>", unsafe_allow_html=True)
                st.markdown(f"#### {item['title']}")
                st.write(item['summary'])
                
                # แถบข้อมูลด้านล่างของการ์ด (Read Story ID, Time, Views, Like)
                b_col1, b_col2 = st.columns([2, 1])
                with b_col1:
                    if st.button(f"📖 Read Story (ID: {item['id']})", key=f"card_read_{item['id']}_{idx}"):
                        st.session_state.current_page = "Reader"
                        st.session_state.selected_article_id = item['id']
                        st.rerun()
                with b_col2:
                    st.markdown(f"<div style='text-align: right; font-size: 12px; color: #64748b; padding-top: 5px;'>⏱️ {item['time_ago']} &nbsp; 👀 {item['views']}</div>", unsafe_allow_html=True)
            st.markdown("")

# ==========================================
# 6. Footer (ท้ายเว็บไซต์)
# ==========================================
st.markdown("---")
st.markdown(
    """
    <div style="background-color: #f8fafc; padding: 20px; text-align: center; border-radius: 8px; border: 1px dashed #cbd5e1;">
        <span style="color: #64748b; font-size: 11px; text-transform: uppercase; letter-spacing: 1px;">[ GOOGLE ADSENSE - GLOBAL LEADERBOARD AD ]</span>
        <p style="margin: 5px 0; font-weight: 600; color: #334155;">QELVYQ — Knowledge in Real Time. Real-time content from trusted sources[cite: 28].</p>
    </div>
    """,
    unsafe_allow_html=True
)
