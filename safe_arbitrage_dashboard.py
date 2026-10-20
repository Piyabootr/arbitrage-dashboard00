            for a in matches:
                st.markdown(f"**{a['title']}**")
                st.caption(a["summary"])
        else:
            st.info("No matching stories found in the current demo database.")
    st.stop()

if st.session_state.current_page == "Analytics":
    st.markdown("## 📊 QELVYQ Analytics")
    st.caption("Overview of the current demo database and session counters.")
    c1, c2, c3 = st.columns(3)
    c1.metric("Stories in database", len(articles))
    c2.metric("Page views", f"{st.session_state.page_views:,}")
    c3.metric("Estimated ad revenue", f"${estimated_revenue:,.2f}")
    category_counts = {}
    for a in articles:
        category_counts[a["category"]] = category_counts.get(a["category"], 0) + 1
    st.markdown("### Stories by category")
    st.bar_chart(category_counts)
    st.stop()

# Hero banner
now = datetime.now().strftime("%d %b %Y  ·  %I:%M %p")
st.markdown(f"""
<div class="hero">
  <div class="hero-status">◷ &nbsp; {now} &nbsp; <span style="color:#45e0a1">● Live</span></div>
  <span class="hero-tag">✦ &nbsp; REAL-TIME NEWS AGGREGATOR</span>
  <h1>QELVYQ <span style="font-weight:500;color:#b9dcff">— Stories & Real-Time Updates.</span></h1>
  <p>Engaging stories, technology insights, and global updates — organized in one smarter knowledge hub.</p>
</div>
""", unsafe_allow_html=True)

# Metrics row
m1, m2, m3, m4 = st.columns(4)
m1.metric("Live Active Visitors", f"{st.session_state.active_users} online", "+12% vs. yesterday")
m2.metric("Total Page Views", f"{st.session_state.page_views:,}", "+18% vs. yesterday")
m3.metric("Est. AdSense Revenue", f"${estimated_revenue:,.2f} USD", "+24% vs. yesterday")
m4.metric("Stories & Updates", f"{len(articles)} stories", "Live feed")

st.markdown("")
left, right = st.columns([1.5, 1])
with left:
    st.markdown('<div class="section-head"><span style="font-size:22px">▣</span><h3>Latest News & Updates</h3></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Real-time news, technology, business, and more — all in one feed.</div>', unsafe_allow_html=True)
with right:
    st.markdown("<div style='text-align:right;padding-top:8px;color:#7b8eaa;font-size:12px'>LIVE FEED &nbsp; <span style='color:#0ca678'>● Connected</span></div>", unsafe_allow_html=True)

# Category chips as working buttons
chip_cols = st.columns(6)
chip_names = ["All", "Business", "Technology", "AI", "Science", "World"]
for i, name in enumerate(chip_names):
    with chip_cols[i]:
        if st.button(name, key=f"chip_{name}", use_container_width=True, type="primary" if (selected_cat == name or (name == "All" and selected_cat == "All Categories")) else "secondary"):
            st.session_state["category_filter_override"] = "All Categories" if name == "All" else name
            st.rerun()
if "category_filter_override" in st.session_state and st.session_state.category_filter_override != selected_cat:
    selected_cat = st.session_state.category_filter_override
    filtered_data = articles[:]
    if search_query:
        q = search_query.lower().strip()
        filtered_data = [a for a in filtered_data if q in a["title"].lower() or q in a["summary"].lower() or q in a["category"].lower()]
    if selected_cat != "All Categories":
        filtered_data = [a for a in filtered_data if a["category"] == selected_cat]
    if st.session_state.current_page == "Bookmarks":
        filtered_data = [a for a in filtered_data if a["id"] in st.session_state.bookmarks]

if st.session_state.current_page == "Stories":
    st.markdown("### 📚 Story Library")
elif st.session_state.current_page == "Bookmarks":
    st.markdown("### 🔖 Your Bookmarks")
elif st.session_state.current_page == "Live News":
    st.markdown("### 🔴 Live News Feed")

if not filtered_data:
    st.info("No stories match your current search or filters.")
else:
    for row_start in range(0, len(filtered_data), 2):
        row = st.columns(2, gap="medium")
        for offset, col in enumerate(row):
            index = row_start + offset
            if index >= len(filtered_data):
                continue
            item = filtered_data[index]
            colors = {"Business": "#7c3aed", "Technology": "#0ea5b7", "AI": "#f97316", "Science": "#16a34a", "World": "#3b82f6"}
            badge_color = colors.get(item["category"], "#3b82f6")
            with col:
                st.markdown('<div class="news-card">', unsafe_allow_html=True)
                image_col, text_col = st.columns([0.78, 1.55], gap="small")
                with image_col:
                    st.image(item["image"], use_container_width=True)
                with text_col:
                    st.markdown(f'<span class="news-category" style="background:{badge_color}">{item["category"]}</span>', unsafe_allow_html=True)
                    st.markdown(f'<div class="news-title">{item["title"]}</div>', unsafe_allow_html=True)
                    st.markdown(f'<div class="news-summary">{item["summary"]}</div>', unsafe_allow_html=True)
                    st.markdown(f'<div class="news-meta">◷ {item["time_ago"]} &nbsp; · &nbsp; ◉ {item["views"]}</div>', unsafe_allow_html=True)
                action1, action2, action3 = st.columns([1.4, 1, 1])
                with action1:
                    if st.button(f"▤ Read Story · {item['id']}", key=f"read_{item['id']}", use_container_width=True):
                        st.session_state.current_page = "Reader"
                        st.session_state.selected_article_id = item["id"]
                        st.rerun()
                with action2:
                    liked = item["id"] in st.session_state.liked_articles
                    if st.button(("♥ Liked" if liked else f"♡ {item['likes']} Like"), key=f"like_{item['id']}", use_container_width=True):
                        if not liked:
                            item["likes"] += 1
                            st.session_state.liked_articles.append(item["id"])
                        st.rerun()
                with action3:
                    saved = item["id"] in st.session_state.bookmarks
                    if st.button("🔖 Saved" if saved else "＋ Save", key=f"save_{item['id']}", use_container_width=True):
                        if saved:
                            st.session_state.bookmarks.remove(item["id"])
                        else:
                            st.session_state.bookmarks.append(item["id"])
                        st.rerun()
                st.markdown('</div>', unsafe_allow_html=True)
                st.markdown("")

st.markdown("""
<div class="footer">
  <div style="font-weight:700;color:#55769d;letter-spacing:.12em">QELVYQ · KNOWLEDGE IN REAL TIME</div>
  <div style="margin-top:5px">A smarter place to discover stories, technology, and ideas.</div>
  <div style="margin-top:5px">Demo metrics are illustrative. Verify news against original publishers before relying on it.</div>
</div>
""", unsafe_allow_html=True)
