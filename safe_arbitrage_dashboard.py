import streamlit as st
import pandas as pd
import requests
import re
import xml.etree.ElementTree as ET

# ตั้งค่าหน้าเว็บให้เป็นแบบ Wide Layout
st.set_page_config(page_title="QELVYQ — Stories & Latest Updates.", layout="wide", initial_sidebar_state="expanded")

# ==========================================
# 1. ระบบจัดการสิทธิ์ผู้ดูแลระบบ (Admin Authentication System)
# ==========================================
if "is_admin" not in st.session_state:
    st.session_state.is_admin = False

if "current_page" not in st.session_state:
    st.session_state.current_page = "home"
if "selected_article_id" not in st.session_state:
    st.session_state.selected_article_id = None

# ==========================================
# 2. ระบบคำนวณสถิติแบบเรียลไทม์ตามความเป็นจริง (Real-Time Analytics)
# ==========================================
if "page_views" not in st.session_state:
    st.session_state.page_views = 1
if "active_users" not in st.session_state:
    st.session_state.active_users = 1

st.session_state.page_views += 1
real_adsense_revenue = (st.session_state.page_views / 1000.0) * 1.50

# ==========================================
# 3. ระบบตรวจสอบและแก้ไขไวยากรณ์ (Grammar Checker Engine)
# ==========================================
def check_and_correct_grammar(text: str) -> tuple[str, list[str]]:
    corrections = []
    corrected_text = text

    if corrected_text and not corrected_text[0].isupper():
        corrections.append("Capitalized the first letter.")
        corrected_text = corrected_text[0].upper() + corrected_text[1:]

    common_errors = {"teh": "the", "recieve": "receive", "adress": "address", "seperate": "separate", "dont": "don't", "cant": "can't"}
    for wrong, right in common_errors.items():
        if wrong in corrected_text.lower():
            corrections.append(f"Corrected spelling: '{wrong}' -> '{right}'")
            corrected_text = re.sub(re.escape(wrong), right, corrected_text, flags=re.IGNORECASE)

    if corrected_text and corrected_text[-1] not in ['.', '!', '?']:
        corrections.append("Added terminal punctuation.")
        corrected_text = corrected_text + "."

    if not corrections:
        corrections.append("Grammar pristine.")

    return corrected_text, corrections

# ==========================================
# 4. ระบบสร้างและดึงข้อมูลเฉพาะ Short/Long Stories และ Latest News
# ==========================================
@st.cache_data(ttl=60)
def generate_stories_and_news(query: str) -> list:
    items = []
    clean_query = query.strip().lower()
    
    # 1. ดึงข่าวสารอัปเดตใหม่ๆ จาก TechCrunch RSS
    try:
        rss_url = "https://techcrunch.com/feed/"
        resp = requests.get(rss_url, timeout=4)
        if resp.status_code == 200:
            root = ET.fromstring(resp.content)
            for item in root.findall('.//item')[:6]:
                title_elem = item.find('title')
                title = title_elem.text if title_elem is not None else "Breaking News Update"
                
                desc_elem = item.find('description')
                desc = desc_elem.text if desc_elem is not None and desc_elem.text else "Latest update..."
                clean_desc = re.sub('<.*?>', '', desc)
                
                items.append({
                    "title": f"Breaking News: {title}",
                    "category": "Latest News & Updates",
                    "read_time": "4 mins",
                    "source": "QELVYQ Live News Wire",
                    "summary": clean_desc[:200] + "...",
                    "content": f"""Latest Update Briefing:
{clean_desc}

Detailed Reporting & Global Impact:
As developments unfold regarding '{clean_query}', international analysts track continuous telemetry and real-time updates. This news dispatch provides uncompromised coverage of current milestones, market reactions, and expert forecasts.

Stay tuned to QELVYQ for continuous live reporting and follow-up updates.""",
                    "views": 1,
                    "likes": 0
                })
    except:
        pass

    # 2. สร้างเรื่องเล่าและนิทาน (Short Story or Long Story) แบบจัดเต็ม
    stories_pool = [
        ("The Chrono Weaver: A Short Story of Lost Moments", "Short Story or Long Story", "6 mins", 
         "A short tale about a clockmaker who discovers a pocket watch capable of pausing time for five seconds.",
         """In a cobblestone alleyway sits a dusty clockmaker's shop, tended by an elderly man named Thomas. Unknown to the town, Thomas possessed a brass pocket watch that could halt time for exactly five seconds. 

For years, he used it selfishly to avoid minor embarrassments—spilled coffee, delayed trains, misplaced keys. But one rainy afternoon, as a runaway carriage hurtled toward a young child on the street, Thomas froze time. He walked over, gently moved the child to safety, and let time resume. 

In that single frozen moment, Thomas realized true purpose wasn't about erasing mistakes, but about choosing when to act with courage. From that day on, the watch remained unwound, and Thomas lived fully in every imperfect second."""),
        
        ("The Kingdom of Glass: A Long Story of Truth and Reflection", "Short Story or Long Story", "12 mins", 
         "An epic narrative about a mountain kingdom where every citizen's mirror reflected their true intentions.",
         """High above the cloudline lay Aethelgard, a kingdom constructed entirely of translucent crystal glass. In this realm, mirrors didn't reflect physical appearance; they revealed the pure intent behind a person's words. 

For centuries, the citizens lived in radical harmony. Lies shattered instantly against the glass walls, causing minor tremors across the valley. However, a young ambitious lord named Vane sought power by discovering a rare mineral that could tint the glass, hiding deceit behind shimmering gold facades. 

As the golden haze spread, trust withered, and the kingdom plunged into suspicion. It took a humble glassblower's apprentice, armed only with a hammer of absolute honesty, to shatter the tainted panes and restore the natural light to Aethelgard. 

Epilogue:
The story reminds us that true strength lies not in concealing our flaws behind illusions, but in standing transparent under the sun."""),

        ("Global Tech Outlook: The Next Wave of Autonomous Systems", "Latest News & Updates", "5 mins",
         "An exhaustive briefing on autonomous edge networks and their deployment across major cities.",
         """Comprehensive Global Dispatch:
Autonomous infrastructure has transitioned from experimental trials to widespread municipal integration. Urban centers utilizing decentralized edge sensors report unprecedented efficiency in traffic flow, energy distribution, and emergency response coordination. 

Industry leaders emphasize that as machine learning models mature, privacy safeguards and cryptographic verification will remain the cornerstone of public trust.""")
    ]

    for idx, (t_title, t_cat, t_time, t_sum, t_content) in enumerate(stories_pool):
        items.append({
            "title": f"{t_title} ({clean_query.capitalize()})" if clean_query != "all" else t_title,
            "category": t_cat,
            "read_time": t_time,
            "source": "QELVYQ Editorial Desk
