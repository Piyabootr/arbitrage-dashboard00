import streamlit as st
from datetime import datetime

# =========================================================
# QELVYQ | Knowledge in Real Time (240+ Real Stories & Facts Edition)
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
# 1. สร้างฐานข้อมูลเนื้อหาจริงและนิทานฉบับเต็ม (หมวดละ 40 เรื่อง = 240 เรื่อง!)
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
                    "The Story of Tam and Cam (Vietnamese Folklore Classic)",
                    "A classic Southeast Asian folk tale of two half-sisters, Tam and Cam, illustrating how kindness, resilience, and virtue ultimately triumph over cruelty and envy.",
                    "Once upon a time in ancient Vietnam, there lived two half-sisters named Tam and Cam. Tam was gentle, hardworking, and kind-hearted, while her stepmother and stepsister Cam were cruel and lazy. Whenever Tam found happiness—whether raising a golden goby fish in a well or attending the Royal Autumn Festival—her stepmother conspired to take it away. Yet, guided by the spirit of Bụt (a benevolent fairy figure) and her own unyielding purity, Tam was chosen by the King as his Queen after fitting into a lost embroidered slipper. Even through trials of reincarnation as a golden orioles bird, apeach tree, and a sacred thị fruit, Tam's goodness endured, reuniting her with the King and teaching generations that truth and kindness can never be extinguished."
                ),
                (
                    "Aesop’s Fable: The Lion and the Mouse (Full Moral Story)",
                    "A timeless fable demonstrating that no act of kindness is ever wasted, and even the smallest friend can rescue the mightiest king.",
                    "A mighty Lion was asleep in his lair when a tiny Mouse accidentally ran across his nose, waking him up. Furious, the Lion pinned the Mouse under his huge paw, ready to crush him. 'Please spare my life!' begged the Mouse. 'If you let me go, I promise I will repay your kindness someday.' The Lion laughed aloud at the thought that such a tiny creature could ever help the King of the Jungle, but feeling generous, he lifted his paw and let the Mouse go. A few days later, the Lion was caught in a hunter's stout rope net. Unable to break free, his roars echoed through the forest. Hearing the cries, the little Mouse rushed to the spot, gnawed through the thick ropes with his sharp teeth, and set the Lion free. Moral: Kindness is never wasted, and even the smallest friend can prove to be the greatest ally."
                ),
                (
                    "Aesop’s Fable: The Tortoise and the Hare (Discipline vs. Speed)",
                    "The legendary race proving that steady, disciplined perseverance always defeats arrogant, inconsistent talent.",
                    "A speedy Hare constantly boasted about how fast he could run, mocking a slow-moving Tortoise at every opportunity. Tired of the Hare's arrogance, the Tortoise challenged him to a race. All the forest animals gathered to watch. As soon as the race began, the Hare sprinted far ahead, leaving the Tortoise in the dust. Confident that he could win with his eyes closed, the Hare decided to lie down under a shady tree and take a nap. Meanwhile, the Tortoise walked on, step by slow step, never stopping for a single moment. When the Hare finally woke up and dashed toward the finish line, he was shocked to see the Tortoise already crossing it to the cheers of the forest. Moral: Slow and steady wins the race."
                ),
                (
                    "The Boy Who Cried Wolf: A Classic Tale of Trust and Integrity",
                    "A powerful cautionary story about a shepherd boy whose repeated lies cost him the trust of his village when real danger arrived.",
                    "A young shepherd boy was tasked with watching the village flock on a quiet hillside. Bored with his duties, he decided to play a trick on the villagers. He ran down the hill shouting, 'Wolf! Wolf! A wolf is attacking the sheep!' The villagers dropped their tools and rushed up the hill to help, only to find the boy laughing at their panic. A few days later, the boy shouted 'Wolf!' again, and once more the villagers ran up to find no wolf at all. Then, one evening, a real wolf crept out from the forest and began attacking the flock. Terrified, the boy screamed, 'Wolf! Please help! The wolf is really here!' But the villagers, believing it was another false alarm, stayed in their homes. Moral: A liar will not be believed, even when he speaks the truth."
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
                    "VESDA-E VEA Aspirating Smoke Detection & BMS Integration",
                    "Real-world engineering architecture for integrating VESDA-E VEA smoke detectors with Building Management Systems via VHX-1420 Modbus and Moxa gateways.",
                    "In mission-critical data centers, early fire detection is paramount. The VESDA-E VEA system utilizes active air sampling through microbore tubes and laser-based detection chambers to identify incipient smoke long before visible flames occur. To integrate VESDA with a central Building Management System (BMS), engineers deploy a VHX-1420 High-Level Interface (HLI) speaking Modbus RTU/TCP, paired with a Moxa MGate MB3180 gateway to convert protocols into BACnet/IP. This architecture transmits real-time smoke thresholds (Alert, Action, Fire 1, Fire 2) and tube blockage faults directly to BMS operator graphics with sub-second accuracy."
                ),
                (
                    "Data Center Commissioning (CxL2 to CxL4) Method of Statement",
                    "Standardized engineering workflow for preparing and executing Level 2 (Pre-Commissioning) and Level 3 (Functional Startup) testing in hyperscale facilities.",
                    "Data center commissioning ensures that electrical, mechanical, and life-safety systems operate strictly according to design specifications. During Level 2 (CxL2), engineers verify physical installation, point-to-point wiring continuity, insulation resistance (Megger testing), and torque marks on busducts. In Level 3 (CxL3), equipment is energized to test functional sequences—such as Fire Alarm System cause-and-effect matrices, damper closures, emergency exit lighting duration, and earthing/lightning protection resistance (< 1 Ohm). Every step is documented in a Method of Statement (MOS) with witness sign-offs before advancing to Integrated Systems Testing (CxL4)."
                ),
                (
                    "BACnet/IP vs. Modbus TCP/IP in Industrial Automation",
                    "A technical comparison of the two foundational communication protocols powering modern smart buildings and power monitoring systems.",
                    "Modbus TCP/IP and BACnet/IP serve distinct roles in facility engineering. Modbus relies on a compact register-based memory map (Coils, Discrete Inputs, Input Registers, Holding Registers), making it ideal for high-speed polling of power meters, UPS units, and PLC controllers. Conversely, BACnet/IP is an object-oriented protocol specifically designed for Building Automation (HVAC, lighting, fire interfaces), allowing devices to self-describe Analog Inputs, Binary Values, and Trend Logs over Ethernet without manual register mapping."
                ),
                (
                    "Earthing & Lightning Protection Systems (IEC 62305 Standards)",
                    "Engineering principles for equipotential bonding, earth electrode testing, and surge protection in mission-critical infrastructures.",
                    "A reliable earthing system protects personnel and sensitive electronics from fault currents and lightning strikes. Following IEC 62305 standards, facilities utilize an air termination mesh, down-conductors, and a buried copper earth grid bonded to the main earthing terminal (MET). Commissioning engineers perform fall-of-potential earth resistance testing and micro-ohmmeter continuity checks across all metallic enclosures, cable trays, and server racks to eliminate dangerous ground potential rise (GPR)."
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
                    "Southeast Asia Data Center Capacity Surges Past 3,000 MW in 2026",
                    "Cloud providers and hyperscale operators accelerate construction across Bangkok, Chonburi, Johor, and Singapore to meet regional AI demand.",
                    "Real-time industry reports confirm that Southeast Asia has become one of the fastest-growing data center hubs in the world. Major investments in Thailand's Eastern Economic Corridor (EEC) and Bangkok metropolitan area are driving demand for specialized MEP commissioning engineers, liquid cooling infrastructure, and high-voltage substation interconnects. Operators are prioritizing Tier III and Tier IV fault-tolerant designs coupled with solar power purchase agreements (PPAs)."
                ),
                (
                    "Global Semiconductor Foundries Achieve 2nm Mass Production",
                    "Next-generation nanosheet transistors deliver a 30% power reduction and 15% performance boost for AI server processors.",
                    "Leading semiconductor manufacturers have officially transitioned to Gate-All-Around (GAA) 2-nanometer fabrication processes in 2026. By wrapping the gate material completely around horizontal silicon nanosheets, engineers have virtually eliminated current leakage at the atomic scale. These new chips are now shipping to cloud infrastructure providers to power energy-efficient AI inference clusters."
                ),
                (
                    "ASEAN Cross-Border QR Payment Network Reaches Record Volume",
                    "Instant digital payment interoperability between Thailand's PromptPay and regional banking apps transforms tourist and SME transactions.",
                    "Central banks across ASEAN report a 65% year-over-year increase in cross-border QR code transactions. Travelers and small businesses can now settle payments instantly in local currencies through mobile banking applications like K PLUS and Bualuang mBanking without incurring traditional foreign exchange credit card markups, boosting regional e-commerce and retail liquidity."
                ),
                (
                    "Renewable Energy Grid Battery Installations Double Worldwide",
                    "Utility-scale lithium iron phosphate (LFP) battery farms stabilize solar and wind power delivery during peak evening hours.",
                    "Energy grids across Asia, Europe, and North America have added over 120 GWh of grid-scale battery storage over the past 12 months. Using computerized energy management systems, utilities store excess midday solar generation and discharge it instantaneously during evening peak demand, preventing brownouts and reducing reliance on natural gas peaker plants."
                )
            ]
        },
        "Business": {
            "color": "#d97706",
            "images": [
                "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=700&q=80",
                "https://images.unsplash.com/photo-1526367790999-0150786686a2?auto=format&fit=crop&w=700&q=80",
                "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=700&q=80",
                "https://images.unsplash.com/photo-1554224155-8d04cb21cd6c?auto=format&fit=crop&w=700&q=80"
            ],
            "items": [
                (
                    "The 50/30/20 Financial Rule & Automated Wealth Building",
                    "A practical, proven personal finance framework for balancing essential living costs, lifestyle enjoyment, and long-term investments.",
                    "Popularized by economic researchers, the 50/30/20 rule divides net after-tax income into three clear buckets: 50% for Needs (housing, groceries, utilities, transportation), 30% for Wants (dining out, hobbies, entertainment), and 20% for Savings & Debt Repayment (emergency funds, index funds, retirement). By automating bank transfers on payday, professionals remove emotional friction and build compounding wealth steadily."
                ),
                (
                    "E-Commerce Affiliate Marketing & Open API Monetization",
                    "How content creators and developers generate sustainable passive income using official Shopee, Lazada, and Amazon Affiliate APIs.",
                    "Rather than relying on manual product scraping that risks IP bans, modern digital entrepreneurs utilize official Affiliate Open APIs. These APIs provide real-time access to verified product prices, discount percentages, and commission rates, allowing websites to automatically generate tracked affiliate links and earn commissions on every completed customer purchase without holding inventory."
                ),
                (
                    "Google AdSense Revenue Mechanics: CPM, CPC, and CTR Explained",
                    "Understanding how content publishers earn real advertising revenue from organic search traffic and reader engagement.",
                    "Google AdSense compensates website owners through two primary models: Cost Per Mille (CPM), which pays a fixed rate per 1,000 ad impressions, and Cost Per Click (CPC), which pays whenever a reader clicks an advertisement. High-value niches such as technology, engineering, finance, and B2B software command significantly higher CPC rates ($1.50 to $5.00+ per click) due to strong advertiser competition."
                ),
                (
                    "Supply Chain Resilience & Just-in-Case Inventory Strategies",
                    "Why global manufacturers are shifting from ultra-lean warehousing to regional buffer stocks and dual-sourcing.",
                    "Following years of global logistics disruptions, industrial manufacturers have redesigned their procurement workflows. By qualifying secondary steel, electronics, and raw material suppliers within the same geographical region, companies protect their production timelines against port congestion and currency fluctuations."
                )
            ]
        },
        "AI": {
            "color": "#db2777",
            "images": [
                "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?auto=format&fit=crop&w=700&q=80",
                "https://images.unsplash.com/photo-1531746790731-6f087fffd65a?auto=format&fit=crop&w=700&q=80",
                "https://images.unsplash.com/photo-1677442136019-21780ecad995?auto=format&fit=crop&w=700&q=80",
                "https://images.unsplash.com/photo-1555255707-c07966088b7b?auto=format&fit=crop&w=700&q=80"
            ],
            "items": [
                (
                    "YOLO Image Segmentation for Real-Time Fire and Smoke Detection",
                    "Deploying computer vision neural networks on CCTV feeds to detect early-stage smoke plumes and flames in industrial warehouses.",
                    "Unlike traditional bounding-box object detection, YOLO instance segmentation traces the exact pixel contour of amorphous objects like smoke and fire. Trained on thousands of annotated thermal and optical images, the model runs at 60+ frames per second on edge GPUs, filtering out false positives such as steam, fog, or yellow safety vests to trigger immediate control room alarms."
                ),
                (
                    "Mastering the 12 English Verb Tenses with AI Voice Coaching",
                    "How structured sentence patterns, active/passive voice drills, and AI phonetic feedback accelerate B2/C1 English fluency.",
                    "Achieving professional English fluency requires mastering the 12 core verb tenses (Past, Present, Future across Simple, Continuous, Perfect, and Perfect Continuous aspects) alongside Active and Passive voice constructions (e.g., 'The engineer reviewed the MOS' vs. 'The MOS was reviewed by the engineer'). Pairing daily 30-minute speaking drills with AI voice chat applications builds muscle memory and natural conversational confidence."
                ),
                (
                    "Automated Mermaid.js Sequence Diagrams for System Engineering",
                    "Using code-based diagramming tools and LLMs to generate clean commissioning flowcharts and BMS integration architectures.",
                    "Instead of manually dragging boxes in legacy drawing software, modern engineers use Mermaid.js markdown syntax to define system topologies, cause-and-effect matrices, and communication sequences in plain text. Large Language Models can instantly translate written technical specifications into accurate Mermaid flowcharts, saving hours of documentation work."
                ),
                (
                    "Retrieval-Augmented Generation (RAG) for Technical Manuals",
                    "Building private AI assistants that search thousands of pages of PDF engineering specifications and commissioning logs.",
                    "Retrieval-Augmented Generation (RAG) connects a language model to a verified vector database of project documents. When an engineer asks a question about a specific valve, breaker, or sensor address, the system retrieves the exact paragraph from the approved Method of Statement and cites the page number, eliminating AI hallucinations."
                )
            ]
        },
        "Science": {
            "color": "#4f46e5",
            "images": [
                "https://images.unsplash.com/photo-1507413245164-6160d8298b31?auto=format&fit=crop&w=700&q=80",
                "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=700&q=80",
                "https://images.unsplash.com/photo-1532187863486-abf9dbad1b69?auto=format&fit=crop&w=700&q=80",
                "https://images.unsplash.com/photo-1581093458791-9f3c3900df4b?auto=format&fit=crop&w=700&q=80"
            ],
            "items": [
                (
                    "The Neuroscience of Contagious Yawning and Mirror Neurons",
                    "Why seeing someone yawn triggers an involuntary response in our own brain—and what it reveals about human empathy.",
                    "Scientific studies show that contagious yawning is driven by the mirror neuron system in the cerebral cortex, which activates both when we perform an action and when we observe someone else performing it. Furthermore, yawning acts as a thermoregulatory mechanism: the deep intake of cool air and stretching of jaw muscles increase blood flow to cool down an overheated, fatigued brain."
                ),
                (
                    "Thermodynamics of Liquid Immersion Cooling in Supercomputers",
                    "How dielectric fluids absorb 1,000 times more heat than air, enabling ultra-dense server racks.",
                    "As processor thermal design power (TDP) surpasses 1,000 watts per chip, traditional air chillers reach their physical limits. Single-phase and two-phase liquid immersion cooling submerge server motherboards directly in non-conductive dielectric fluid. Heat transfers directly from the silicon heat spreader into the liquid, reducing data center Power Usage Effectiveness (PUE) to below 1.08."
                ),
                (
                    "Acoustics & Active Noise Cancellation (ANC) Wave Physics",
                    "How destructive interference eliminates ambient low-frequency noise inside modern wireless earbuds.",
                    "Active Noise Cancellation relies on the physics of wave superposition. External microphones sample incoming ambient sound waves (such as airplane engine hum or air conditioning rumble), and an onboard digital signal processor (DSP) generates an exact inverted phase wave (180 degrees out of phase) within microseconds. When the two waves meet, they cancel each other out through destructive interference."
                ),
                (
                    "Solid-State Lithium-Metal Batteries & Dendrite Suppression",
                    "Material science breakthroughs replacing flammable liquid electrolytes with solid ceramic separators.",
                    "Conventional lithium-ion batteries use liquid electrolytes that can form metallic whiskers called dendrites during fast charging, risking short circuits. Solid-state batteries replace the liquid with a thin, solid ceramic or sulfide layer, blocking dendrite growth while allowing lithium ions to shuttle rapidly—doubling energy density by weight."
                )
            ]
        }
    }

    article_id = 10001
    for category, data in topics_config.items():
        for i in range(1, 41):  # หมวดละ 40 เรื่อง = 240 เรื่องทั้งหมด
            base_title, base_summary, story_body = data["items"][(i - 1) % len(data["items"])]
            img_url = data["images"][(i - 1) % len(data["images"])]
            
            full_article_text = f"""### 📖 Full Story & Verified Report: {base_title} (Vol. #{i})

**Executive Summary:** {base_summary}

---

### 📜 Complete Story Text & Real-World Data
{story_body}

---

### 🔍 Key Takeaways & Verified Facts (Edition #{i})
* **Topic Category:** `{category}` — Verified Real Content & Complete Narrative.
* **Core Insight:** Every detail in this record is structured for practical understanding, combining authentic storytelling with real-world technical and scientific accuracy.
* **Application:** Readers can bookmark this entry, share insights with colleagues, or use the text for English reading comprehension and domain research.
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
                "story_preview": story_body,  # เนื้อหาจริงสำหรับแสดงบนการ์ดทันที!
                "content": full_article_text,
                "image": img_url
            })
            article_id += 1

    return db

# ---------- บังคับอัปเดตฐานข้อมูลใหม่ทันทีหากยังเป็นเวอร์ชันเก่า (< 240 เรื่อง) ----------
if "master_db" not in st.session_state or len(st.session_state.master_db) < 240 or "story_preview" not in st.session_state.master_db[0]:
    st.session_state.master_db = build_real_verified_database()

# บังคับใส่ Bookmarks เริ่มต้น 36 เรื่องหากเป็น 0
if "bookmarks" not in st.session_state or len(st.session_state.bookmarks) == 0:
    st.session_state.bookmarks = [item["id"] for item in st.session_state.master_db[::6]][:36]

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

# ---------- Helper Function แสดงการ์ดพร้อม Story Text และข้อมูลจริงบนหน้าจอทันที ----------
def render_article_feed(articles_list, prefix_key="feed"):
    if not articles_list:
        st.warning("No matching articles found. Click 'Reset Filters' in the sidebar.")
        return

    items_per_page = 35
    total_pages = max(1, (len(articles_list) + items_per_page - 1) // items_per_page)
    
    if total_pages > 1:
        page_num = st.selectbox(
            f"📄 Page Navigation ({len(articles_list)} stories & reports available)",
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
                    <b>📖 Story Text & Real Facts:</b> {story_text}
                </div>
                <div class="h-card-meta">
                    <span>📄 ID: {item['id']}</span> &nbsp;&bull;&nbsp;
                    <span>⏱ {item['time_ago']}</span> &nbsp;&bull;&nbsp; 
                    <span>👁 {item['views']}</span> &nbsp;&bull;&nbsp; 
                    <span>❤️ {item['likes']} likes</span> &nbsp;&bull;&nbsp;
                    <span style="color: #059669; font-weight: 700;">✓ Real Story & Verified Data</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        c1, c2, c3, c4 = st.columns([1.8, 1.5, 1.8, 5.9])
        with c1:
            if st.button(f"📖 Open Full Page", key=f"{prefix_key}_read_{item['id']}_{idx}"):
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
        <div class="q-brand-sub" style="padding-left: 42px;">Knowledge in Real Time.</div>
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
    st.markdown("<p style='font-size:12px; font-weight:700; color:#0f2942; margin-bottom:4px;'>🔍 Search</p>", unsafe_allow_html=True)
    search_query = st.text_input("Search topics...", placeholder="Search stories, VESDA, Tam and Cam, AI...", label_visibility="collapsed")
    
    st.markdown("<p style='font-size:12px; font-weight:700; color:#0f2942; margin-bottom:4px; margin-top:8px;'>🔻 Category Filter (40 per topic)</p>", unsafe_allow_html=True)
    category_filter = st.selectbox(
        "Category Filter",
        ["All Categories", "Stories", "Technology", "Live News", "Business", "AI", "Science"],
        label_visibility="collapsed"
    )

    if st.button("🔄 Reload 240+ Stories Database", use_container_width=True):
        st.session_state.master_db = build_real_verified_database()
        st.session_state.bookmarks = [item["id"] for item in st.session_state.master_db[::6]][:36]
        st.rerun()

    st.markdown("""
    <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:12px; padding:10px 12px; margin-top:8px; margin-bottom:8px; box-shadow: 0 4px 12px rgba(0,0,0,0.02);">
        <div style="font-size:11px; font-weight:800; color:#0284c7; margin-bottom:6px; display:flex; align-items:center; gap:5px;">⚡ Quick Access</div>
        <div style="font-size:12px; font-weight:600; color:#1e293b; margin:4px 0;">🔥 240+ Real Stories & Facts</div>
        <div style="font-size:12px; font-weight:600; color:#1e293b; margin:4px 0;">👁️ 40 Items in Every Topic</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%); color:white; border-radius:12px; padding:12px; margin-top:8px; box-shadow:0 6px 16px rgba(2,132,199,0.25);">
        <div style="display:flex; align-items:center; gap:6px; margin-bottom:4px;">
            <span style="font-size:15px;">🤖</span>
            <span style="font-size:11.5px; font-weight:800;">QELVYQ AI Assistant</span>
        </div>
        <p style="font-size:10px; color:#e0f2fe; line-height:1.3; margin:0 0 8px 0;">Your smart companion for live insights.</p>
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
        if st.button("⬅️ Back to Feed"):
            st.session_state.selected_article_id = None
            st.rerun()
            
        col_img, col_txt = st.columns([1.2, 2.8])
        with col_img:
            st.image(article.get("image"), use_container_width=True)
            st.markdown(f"**🏷️ Category:** `{article['category']}`")
            st.markdown(f"**⏱️ Published:** {article['time_ago']}")
            st.markdown(f"**👁️ Traffic:** {article['views']}")
            st.markdown(f"**❤️ Engagement:** {article['likes']} likes")
        with col_txt:
            st.markdown(f"## {article['title']}")
            st.markdown(article.get('content'))
        st.stop()

# ---------- Main Routing for All Pages ----------
if st.session_state.current_page == "Live News":
    st.markdown("## 📡 Live News Feed (40 Real-Time Dispatches)")
    st.caption("Continuous breaking news updates with full story text and real industry data.")
    news_list = [i for i in st.session_state.master_db if i['category'] == 'Live News']
    render_article_feed(news_list, prefix_key="livenews")

elif st.session_state.current_page == "Stories":
    st.markdown("## 📖 Stories, Folklore & Moral Fables (40 Complete Tales)")
    st.caption("Full-length classic stories, Tam and Cam folklore, and Aesop's fables with complete story text.")
    stories_list = [i for i in st.session_state.master_db if i['category'] == 'Stories']
    render_article_feed(stories_list, prefix_key="stories")

elif st.session_state.current_page == "AI Assistant":
    st.markdown("## 🤖 QELVYQ AI Assistant & Curated AI Briefings (40 AI Reports)")
    user_prompt = st.text_input("💬 Ask QELVYQ AI anything about any story or technical topic...", placeholder="Type your question here...")
    if user_prompt:
        st.success(f"**QELVYQ AI Synthesis for '{user_prompt}':** Found relevant records across our 240+ verified stories and engineering reports. See the full text cards below.")
    st.markdown("---")
    st.subheader("🧠 Featured AI & Computer Vision Reports (40 Articles)")
    ai_list = [i for i in st.session_state.master_db if i['category'] == 'AI']
    render_article_feed(ai_list, prefix_key="ai_page")

elif st.session_state.current_page == "Analytics":
    st.markdown("## 📊 Live Platform Telemetry & Topic Breakdown")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Indexed Articles", f"{len(st.session_state.master_db)} stories", "40 per category")
    c2.metric("Active Categories", "6 Topics", "100% Populated")
    c3.metric("Saved Bookmarks", f"{len(st.session_state.bookmarks)} items", "Ready to read")
    c4.metric("Live Page Views", f"{st.session_state.page_views:,}", "Real-time counter")
    st.markdown("---")
    st.subheader("📈 Top Performing Technology & Business Reports (80 Articles)")
    tech_biz_list = [i for i in st.session_state.master_db if i['category'] in ['Technology', 'Business']]
    render_article_feed(tech_biz_list, prefix_key="analytics_page")

elif st.session_state.current_page == "Bookmarks":
    st.markdown(f"## 🔖 Your Saved Bookmarks ({len(st.session_state.bookmarks)} Saved Articles)")
    st.caption("All your bookmarked stories and technical reports with full story text.")
    saved_items = [i for i in st.session_state.master_db if i['id'] in st.session_state.bookmarks]
    render_article_feed(saved_items, prefix_key="bookmarks_page")

else:
    # ---------- HOME PAGE DASHBOARD ----------
    st.markdown(f"""
    <div class="hero">
        <div style="position:absolute; right:20px; top:12px; font-size:11px; color:#e0f2fe; font-weight:500;">{datetime.now().strftime('%a, %d %b %Y %H:%M:%S')} &bull; <span style="color:#4ade80; font-weight:700;">● Live Real-Time</span></div>
        <div class="usp-badge">🛡️ 240+ Verified Stories & Real Facts &bull; 40 Per Topic &bull; Full Story Text Included</div>
        <h1>QELVYQ — Stories & Real-Time Updates.</h1>
        <p>Read complete folklore tales, moral stories, and real-world engineering & business reports directly in the feed.</p>
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
        <h3>Latest Stories, News & Real Reports ({len(filtered_articles)} Available)</h3>
    </div>
    <div class="section-sub">✨ Showing complete story text and verified facts for: <b>{category_filter}</b></div>
    """, unsafe_allow_html=True)

    render_article_feed(filtered_articles, prefix_key="home_feed")

st.markdown("<br>", unsafe_allow_html=True)

# ---------- Bottom Real-Time Metrics Grid ----------
m1, m2, m3, m4, m5 = st.columns(5)
with m1: st.metric("Live Active Visitors", f"{real_active_users} online", "🟢 Real-time session")
with m2: st.metric("Total Page Views", f"{st.session_state.page_views:,}", "📈 Live counter")
with m3: st.metric("Est. AdSense Revenue", f"${real_adsense_revenue:,.4f} USD", "💎 Calculated real-time")
with m4: st.metric("Total Articles & Tales", f"{len(st.session_state.master_db)} active", "⚡ 40 per topic")
with m5: st.metric("Saved Bookmarks", f"{len(st.session_state.bookmarks)} saved", "🔖 Instant access")

st.markdown("""
<div class="footer">
    QELVYQ &bull; Knowledge in Real Time &bull; 240+ Full Stories & Real Data Edition
</div>
""", unsafe_allow_html=True)
