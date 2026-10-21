import streamlit as st
from datetime import datetime

# =========================================================
# QELVYQ | 24-7 English & English Pulse Mastery Hub (100% English)
# =========================================================
st.set_page_config(
    page_title="QELVYQ — 24-7 English & English Pulse Hub",
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
.h-card-img { width:150px; height:130px; object-fit:cover; border-radius:10px; border:1px solid #e2e8f0; flex-shrink:0; }
.h-card-content { flex-grow:1; }
.h-card-title { font-size:15.5px; line-height:1.35; font-weight:800; color:#0f172a; margin:4px 0 6px; }
.h-card-summary { color:#1e293b; font-size:12.5px; line-height:1.55; margin:0 0 8px; font-weight: 500; }
.h-card-story-box { background:#f8fafc; border-left:3px solid #0284c7; padding:10px 12px; border-radius:6px; color:#334155; font-size:12px; line-height:1.65; margin-bottom:8px; }
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
# 1. Complete 24-7 English & English Pulse Database (240 Lessons)
# =========================================================
def build_complete_english_database():
    db = []
    topics_config = {
        "24-7 English Stories": {
            "color": "#0284c7",
            "images": [
                "https://images.unsplash.com/photo-1516979187457-637abb4f9353?auto=format&fit=crop&w=700&q=80",
                "https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8?auto=format&fit=crop&w=700&q=80",
                "https://images.unsplash.com/photo-1506880018603-83d5b814b5a6?auto=format&fit=crop&w=700&q=80",
                "https://images.unsplash.com/photo-1476275466078-4007374efbbe?auto=format&fit=crop&w=700&q=80"
            ],
            "items": [
                (
                    "24-7 English Story: The Clockmaker's Five Seconds",
                    "Intermediate listening and reading story about an old watchmaker who learns the value of living in the present moment.",
                    "In a narrow cobblestone alleyway of an old European town, there lived an elderly clockmaker named Thomas. He possessed a brass pocket watch handed down by his grandfather that could pause time for five seconds. For decades, he used it to undo minor mistakes like spilled coffee. One rainy afternoon, he paused time to rescue a child from a runaway carriage. Looking at the gears, he realized that erasing every minor flaw robs us of personal growth. From that day forward, he lived fully in every imperfect second.",
                    "Cobblestone (n.): Rounded stones used for paving streets | Hurtle (v.): To move at a high speed in an uncontrolled manner | Rob someone of (phrasal v.): To deprive someone of something important.",
                    "Past Simple vs. Past Continuous: 'As Thomas walked (Past Simple) home, a carriage was hurtling (Past Continuous) toward a child.'"
                ),
                (
                    "24-7 English Story: The Midnight Train to Zurich",
                    "A suspenseful everyday English story practicing travel vocabulary, past tenses, and natural dialogue.",
                    "Elena arrived at the central station ten minutes before midnight. The platform was covered in thick autumn fog, and only a few passengers were waiting near the yellow line. When she boarded carriage four, she noticed a leather briefcase left on the seat opposite hers. Inside was a notebook written inthree different languages, containing schedules for European power grids. Instead of panicking, Elena calmly alerted the train conductor, who thanked her for her sharp observation and composure under pressure.",
                    "Board (v.): To get on a train, plane, or ship | Opposite (prep.): Facing across from someone | Composure (n.): The state of being calm and in control of oneself.",
                    "Past Perfect for earlier past actions: 'Someone had left (Past Perfect) the briefcase before Elena boarded (Past Simple) the train.'"
                ),
                (
                    "24-7 English Story: The Coffee Shop on Corner Street",
                    "Daily life conversational story focusing on small talk, polite requests, and describing people.",
                    "Every morning at seven thirty, Arthur sat at the corner table of the Blue Bean Cafe. He always ordered a black Americano and read the financial newspaper for forty minutes. One Tuesday, a young software engineer named Maya accidentally sat at his table because the cafe was completely full. What began as an awkward apology turned into a fascinating daily mentorship. Arthur shared decades of business wisdom, while Maya taught him how modern cloud applications are deployed around the world.",
                    "Awkward (adj.): Causing difficulty or mild embarrassment | Mentorship (n.): Guidance provided by a more experienced person | Deploy (v.): To bring resources or software into effective action.",
                    "Adverbs of Frequency & Past Habits: 'He always ordered (Past Simple) coffee' / 'What began (Past Simple) as an apology turned into a friendship.'"
                ),
                (
                    "24-7 English Story: The Lighthouse Keeper's Logbook",
                    "Descriptive English storytelling focused on weather expressions, perseverance, and nature vocabulary.",
                    "For thirty-two years, Captain Henrik maintained the beacon on Stormcrag Island. Before automated GPS navigation became universal, his lantern was the only signal keeping cargo vessels away from the jagged coastal reefs. During the great winter gale of 1998, the main electrical generator failed at two in the morning. Henrik climbed the winding iron stairs with a backup oil lamp and manually rotated the lenses until dawn, proving that human dedication remains the ultimate safeguard.",
                    "Beacon (n.): A light or signal that guides navigators | Jagged (adj.): Having rough, sharp points | Safeguard (n.): A measure taken to protect someone or something.",
                    "Prepositions of Time and Duration: 'For thirty-two years' (duration) vs. 'During the winter gale' (specific period) vs. 'Until dawn' (endpoint)."
                )
            ]
        },
        "Classic Books & Folklore": {
            "color": "#7c3aed",
            "images": [
                "https://images.unsplash.com/photo-1532012197267-da84d127e765?auto=format&fit=crop&w=700&q=80",
                "https://images.unsplash.com/photo-1512820790803-83ca734da794?auto=format&fit=crop&w=700&q=80",
                "https://images.unsplash.com/photo-1457369804613-52c61a468e7d?auto=format&fit=crop&w=700&q=80",
                "https://images.unsplash.com/photo-1519681393784-d120267933ba?auto=format&fit=crop&w=700&q=80"
            ],
            "items": [
                (
                    "Folklore Classic: The Story of Tam and Cam",
                    "A classic Vietnamese folk tale retold in clear English, illustrating how kindness and resilience triumph over envy.",
                    "Once upon a time in ancient Vietnam, there lived two half-sisters named Tam and Cam. Tam was gentle, hardworking, and kind-hearted, while her stepmother and Cam were cruel and lazy. Whenever Tam found joy—whether raising a golden fish or preparing for the Royal Festival—her stepmother conspired against her. Yet, aided by benevolent magic and her own unyielding purity, Tam matched the lost embroidered slipper and became Queen. Through every trial, her virtue endured, teaching that goodness can never be extinguished.",
                    "Conspire (v.): To make secret plans jointly to commit a harmful act | Benevolent (adj.): Well-meaning and kindly | Unyielding (adj.): Firm and resolute; not giving way to pressure.",
                    "Passive Voice in Storytelling: 'Tam was chosen (Past Simple Passive) by the King after the slipper was found.'"
                ),
                (
                    "Book Adaptation: The Alchemist's Desert Journey",
                    "An English adaptation of the timeless quest for personal purpose, treasure, and learning from omens.",
                    "Santiago, a young Andalusian shepherd, kept having a recurring dream about a hidden treasure near the Egyptian pyramids. Selling his flock, he crossed the Strait of Gibraltar and worked for a crystal merchant in Tangier for a year. Joining a desert caravan, he met an Englishman studying alchemy and learned to read the silent language of the desert wind. When he finally reached the pyramids, he discovered that the physical gold had been buried back under the sycamore tree where his journey began, but the wisdom lay in the journey itself.",
                    "Recurring (adj.): Occurring again periodically or repeatedly | Caravan (n.): A group of travelers journeying together through a desert | Alchemy (n.): A medieval forerunner of chemistry focused on transformation.",
                    "Participle Clauses for Concise Writing: 'Selling his flock (Present Participle clause), he crossed the Strait of Gibraltar.'"
                ),
                (
                    "Book Adaptation: The Old Fisherman and the Marlin",
                    "A powerful story of endurance, dignity, and respect for nature adapted for B2 English readers.",
                    "For eighty-four days, an aging Cuban fisherman named Santiago had sailed into the Gulf Stream without catching a single fish. On the eighty-fifth day, he rowed far beyond the customary coastal waters and hooked a giant marlin longer than his skiff. For three days and three nights, the old man held the taut line across his scarred shoulders, speaking to the noble fish as a brother. Though sharks eventually claimed the catch on the voyage home, Santiago returned with undefeated spirit.",
                    "Customary (adj.): According to the customs or usual practices | Skiff (n.): A shallow, flat-bottomed open boat | Taut (adj.): Stretched or pulled tight; not slack.",
                    "Past Perfect Continuous: 'He had been sailing (Past Perfect Continuous) for eighty-four days before he hooked (Past Simple) the marlin.'"
                ),
                (
                    "Aesop's Fables Collection: The Lion, the Mouse & The Tortoise",
                    "Moral fables retold in crisp, memorable English for vocabulary retention and speaking retell practice.",
                    "In the heart of the forest, a mighty Lion spared the life of a tiny Mouse who accidentally woke him. Days later, when the Lion was trapped in a hunter's rope net, that same little Mouse gnawed through the cords and set him free. Across the meadow, a slow Tortoise accepted a race challenge from a boastful Hare. While the overconfident Hare slept under an oak tree, the Tortoise marched steadily across the finish line, proving that daily discipline beats erratic talent.",
                    "Spare (v.): To refrain from harming or destroying | Gnaw (v.): To bite at or nibble something persistently | Erratic (adj.): Not even or regular in pattern or movement.",
                    "Contrast Connectors: 'While (conjunction) the Hare slept, the Tortoise marched steadily' / 'Even though he was small, he saved the king.'"
                )
            ]
        },
        "English Pulse: Grammar & 12 Tenses": {
            "color": "#059669",
            "images": [
                "https://images.unsplash.com/photo-1455390582262-044cdead277a?auto=format&fit=crop&w=700&q=80",
                "https://images.unsplash.com/photo-1434030216411-0b793f4b4173?auto=format&fit=crop&w=700&q=80",
                "https://images.unsplash.com/photo-1503676260728-1c00da094a0b?auto=format&fit=crop&w=700&q=80",
                "https://images.unsplash.com/photo-1513258496099-48168024aec0?auto=format&fit=crop&w=700&q=80"
            ],
            "items": [
                (
                    "English Pulse: Mastering All 12 Verb Tenses Easily",
                    "Stop translating in your head and master the 12 English verb tenses as a logical coordinate system of time.",
                    "Instead of memorizing isolated rules, view the 12 English tenses as 3 times (Past, Present, Future) multiplied by 4 aspects (Simple, Continuous, Perfect, Perfect Continuous). Simple tenses state facts and habits ('I write code'). Continuous tenses highlight ongoing actions in progress ('I am writing code right now'). Perfect tenses build a bridge showing completed results before a reference point ('I have written the report'). Perfect Continuous tenses measure the duration of an ongoing action ('I have been writing since 8 AM').",
                    "Aspect (n.): A grammatical category expressing how an action extends over time | Ongoing (adj.): Continuing to exist or develop | Reference point (n.): A basis or standard for evaluation.",
                    "The 4 Present Tenses Formula: Simple (S + V1) | Continuous (S + am/is/are + V-ing) | Perfect (S + have/has + V3) | Perfect Continuous (S + have/has + been + V-ing)."
                ),
                (
                    "English Pulse: Active vs. Passive Voice Constructions",
                    "Learn when and how to shift between Active and Passive voice in everyday speech and technical writing.",
                    "In an Active sentence, the subject performs the action: 'The commissioning engineer tested the fire alarm panel.' In a Passive sentence, the object becomes the focus: 'The fire alarm panel was tested by the commissioning engineer.' We use the Passive Voice when the action or the receiver is more important than the doer, or when writing formal engineering reports and Method of Statements. To form the passive, always combine the appropriate tense of the verb 'to be' with the Past Participle (V3).",
                    "Perform (v.): To carry out, accomplish, or fulfill an action | Receiver (n.): The person or thing that receives an action | Past Participle (n.): The third form of a verb (e.g., written, tested, built).",
                    "Passive Voice Transformation across Tenses: Present Simple ('is tested') | Past Simple ('was tested') | Present Perfect ('has been tested') | Future ('will be tested')."
                ),
                (
                    "English Pulse: The 5 Basic Sentence Structure Patterns",
                    "Build rock-solid English sentences every time by mastering the 5 core structural patterns of English.",
                    "Every English sentence, no matter how long, is built on one of five core patterns: 1) S + V (Subject + Intransitive Verb: 'The system works.'), 2) S + V + O (Subject + Transitive Verb + Object: 'Engineers review documents.'), 3) S + V + C (Subject + Linking Verb + Complement: 'The server is online.'), 4) S + V + IO + DO (Indirect Object + Direct Object: 'She sent the client the report.'), and 5) S + V + O + OC (Object + Object Complement: 'They kept the cables organized.').",
                    "Intransitive (adj.): A verb that does not take a direct object | Complement (n.): A word or phrase that completes the predicate | Clause (n.): A unit of grammatical organization containing a subject and verb.",
                    "Expanding Core Patterns: Start with a core pattern ('Engineers review documents') and add modifiers ('Every morning, senior engineers carefully review the commissioning documents')."
                ),
                (
                    "English Pulse: Zero, First, Second & Third Conditionals",
                    "Express facts, future plans, hypothetical dreams, and past regrets with complete accuracy.",
                    "Conditionals connect a condition ('If' clause) to a result. The Zero Conditional states universal truths ('If water reaches 100 degrees, it boils'). The First Conditional deals with real future possibilities ('If we finish the test today, we will submit the report tomorrow'). The Second Conditional imagines unreal present situations ('If I had more free time, I would read more books'). The Third Conditional reflects on past situations that cannot be changed ('If we had checked the gateway settings earlier, the system would have connected').",
                    "Hypothetical (adj.): Imagined or suggested but not necessarily real | Universal truth (n.): A fact that is always true everywhere | Regret (n.): A feeling of sadness about something that cannot be changed.",
                    "Conditional Verb Formulas: Zero (If + Present, Present) | 1st (If + Present, will + V1) | 2nd (If + Past Simple, would + V1) | 3rd (If + had + V3, would have + V3)."
                )
            ]
        },
        "English Pulse: Speaking & Phonetics": {
            "color": "#db2777",
            "images": [
                "https://images.unsplash.com/photo-1590602847861-f357a9332bbc?auto=format&fit=crop&w=700&q=80",
                "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&w=700&q=80",
                "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=700&q=80",
                "https://images.unsplash.com/photo-1543269865-cbf427effbad?auto=format&fit=crop&w=700&q=80"
            ],
            "items": [
                (
                    "English Pulse: Consonants, Vowels & Clear Pronunciation",
                    "Master tricky English consonant clusters, final sounds, and vowel length to speak clearly and confidently.",
                    "Clear pronunciation is not about erasing your accent; it is about making your speech effortlessly understood. Many learners drop final consonant sounds like /t/, /d/, /k/, and /s/, which makes past tense verbs and plurals hard to hear. Practice releasing your breath clearly at the end of words like 'worked', 'tested', and 'systems'. Additionally, distinguish between short and long vowels—such as 'ship' vs. 'sheep' or 'full' vs. 'fool'—by relaxing or tensing your jaw.",
                    "Consonant cluster (n.): A group of consonants without vowels between them (e.g., str, spl) | Intonation (n.): The rise and fall of the voice in speaking | Articulate (v.): To pronounce words clearly and distinctly.",
                    "Pronouncing -ED Endings: Pronounce as /t/ after voiceless sounds ('worked'), /d/ after voiced sounds ('called'), and /ɪd/ after T or D ('started', 'needed')."
                ),
                (
                    "English Pulse: The Shadowing Technique for B2 Fluency",
                    "How to train your mouth muscles, rhythm, and natural speed by echoing native English speakers in real time.",
                    "Shadowing is an active speaking exercise where you listen to a native English audio clip and repeat the words out loud just half a second behind the speaker, like a shadow. Instead of pausing the audio to think, you match the speaker's exact rhythm, word stress, and connected speech. Practicing shadowing for fifteen minutes every evening bridges the gap between passive listening and active speaking, training your brain to produce English phrases automatically without hesitation.",
                    "Connected speech (n.): Spoken language in a continuous sequence where words link together | Hesitation (n.): The action of pausing before saying or doing something | Rhythm (n.): A strong, regular, repeated pattern of sound.",
                    "Word Linking Rules: Consonant-to-Vowel linking ('pick_it_up' sounds like 'pi-ki-tup' / 'turn_it_on' sounds like 'tur-ni-ton')."
                ),
                (
                    "English Pulse: How to Stop Translating in Your Head",
                    "A practical 3-step daily routine to start thinking directly in English during work and daily life.",
                    "When you translate word-by-word from your native language, conversations move too fast for you to keep up. To start thinking directly in English, use the '3-Level Inner Monologue' method. Level 1: Name objects and actions around you in English throughout the day ('commuting to work', 'reviewing drawings'). Level 2: Narrate your immediate plans in simple sentences ('I need to finish this table before lunch'). Level 3: Hold a two-minute evening reflection out loud, summarizing what went well today.",
                    "Inner monologue (n.): The internal voice of your thoughts | Narrate (v.): To give a spoken or written account of events | Keep up (phrasal v.): To move or progress at the same rate as someone else.",
                    " natural Sentence Starters for Thinking Out Loud: 'Let me see...', 'The main point is...', 'What I mean is...', 'On the other hand...'"
                ),
                (
                    "English Pulse: Word Stress & Sentence Melody in English",
                    "Why English is a stress-timed language and how stressing the right words makes you sound natural.",
                    "English is a stress-timed language, meaning that some words are spoken loudly and slowly while others are reduced and spoken quickly. In any sentence, we stress 'Content Words'—nouns, main verbs, adjectives, and adverbs—because they carry the meaning. Conversely, we reduce 'Function Words'—prepositions, articles, and auxiliary verbs. For example, in 'I am going to the office to check the server,' the stressed beats fall on 'GO-ing', 'OF-fice', 'CHECK', and 'SER-ver'.",
                    "Stress-timed (adj.): A language where stressed syllables occur at roughly equal intervals | Content words (n.): Words that carry meaning | Reduce (v.): To shorten a vowel sound to a weak schwa /ə/ sound.",
                    "Shifting Stress Changes Meaning: 'I didn't say he took the file' (Someone else said it) vs. 'I didn't say he took the FILE' (He took something else)."
                )
            ]
        },
        "Vocabulary & Phrasal Verbs": {
            "color": "#d97706",
            "images": [
                "https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8?auto=format&fit=crop&w=700&q=80",
                "https://images.unsplash.com/photo-1481627834876-b7833e8f5570?auto=format&fit=crop&w=700&q=80",
                "https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?auto=format&fit=crop&w=700&q=80",
                "https://images.unsplash.com/photo-1497633762265-9d179a990aa6?auto=format&fit=crop&w=700&q=80"
            ],
            "items": [
                (
                    "50 Essential Phrasal Verbs for Daily Life & Work",
                    "Learn high-frequency phrasal verbs in natural context rather than memorizing dry dictionary lists.",
                    "Native speakers use phrasal verbs constantly in both casual conversation and workplace meetings. Instead of saying 'postpone', they say 'put off'. Instead of 'investigate', they say 'look into'. Instead of 'cancel', they say 'call off'. When learning phrasal verbs, group them by situations rather than by the main verb. For example, in a project meeting, you might 'bring up' an issue, 'sort out' a problem, 'carry out' a test, and 'follow up' with the client the next day.",
                    "Put off (phrasal v.): To postpone or delay | Look into (phrasal v.): To investigate or examine | Sort out (phrasal v.): To resolve a problem or organize things.",
                    "Separable vs. Inseparable Phrasal Verbs: 'Turn off the alarm' or 'Turn the alarm off' (Separable) vs. 'Look into the issue' (Inseparable—cannot say 'Look the issue into')."
                ),
                (
                    "Natural English Collocations: Words That Belong Together",
                    "Sound like a native speaker by pairing the right verbs and adjectives with the right nouns.",
                    "Why do we say 'make a mistake' instead of 'do a mistake', or 'heavy rain' instead of 'strong rain'? The answer is collocations—natural combinations of words that native speakers instinctively pair together. Learning vocabulary in 2-to-3 word chunks prevents unnatural phrasing. In everyday life, we 'make progress', 'do research', 'take a break', 'pay attention', 'catch a cold', and 'meet a deadline'. Memorizing these partnerships is the fastest shortcut to B2/C1 accuracy.",
                    "Collocation (n.): The habitual juxtaposition of a particular word with another word | Instinctively (adv.): Without conscious thought; by natural intuition | Shortcut (n.): An accelerated way of doing something.",
                    "Make vs. Do Rule of Thumb: Use 'DO' for routine tasks and work ('do homework', 'do a job', 'do business') and 'MAKE' for creating or deciding ('make a plan', 'make a decision')."
                ),
                (
                    "Everyday English Idioms Used in Real Conversations",
                    "Understand colorful English expressions that you will hear in movies, podcasts, and office chats.",
                    "Idioms carry meanings that cannot be understood just by looking at the individual words. When a colleague says, 'Let's call it a day,' they mean it is time to stop working for today. If someone says a task is 'a piece of cake', it is very easy. When you are 'on the same page' with your team, everyone agrees and understands the plan. And when you 'hit the nail on the head', you have described the exact root cause of a problem.",
                    "Call it a day (idiom): To decide to stop working | On the same page (idiom): Having the same understanding | Hit the nail on the head (idiom): To be딪 exactly right about something.",
                    "Using Idioms Naturally: Use 1 or 2 idioms in spoken conversation to sound warm and natural, but prefer clear, direct verbs in formal technical documents."
                ),
                (
                    "Smart Memory Techniques: Spaced Repetition & Active Recall",
                    "How to remember new English words permanently without forgetting them the next morning.",
                    "Reading a vocabulary list ten times is passive recognition; your brain quickly forgets what it does not actively retrieve. To lock new English words into long-term memory, combine 'Active Recall' with 'Spaced Repetition'. Whenever you learn a new word, immediately write two personal sentences connected to your own life and job. Then, test yourself on the word after 1 day, 3 days, 7 days, and 14 days. Retrieving the word just before you are about to forget it cements the neural connection.",
                    "Retrieve (v.): To get or bring something back from memory | Cement (v.): To make something strong or permanent | Recognition (n.): Identification of something from previous encounters.",
                    "The 3-Sentence Context Method: For every new word, write 1 Past sentence, 1 Present sentence, and 1 Question to master its usage completely."
                )
            ]
        },
        "Workplace & Technical English": {
            "color": "#4f46e5",
            "images": [
                "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=700&q=80",
                "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=700&q=80",
                "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=700&q=80",
                "https://images.unsplash.com/photo-1581092160607-ee22621dd758?auto=format&fit=crop&w=700&q=80"
            ],
            "items": [
                (
                    "Technical English: Writing Clear Commissioning Documents (MOS)",
                    "How to write professional Method of Statements, test procedures, and review responses in clear English.",
                    "In international engineering projects, technical documents must be unambiguous, concise, and verifiable. When writing a Commissioning Method of Statement (MOS) for Level 2 (CxL2) or Level 3 (CxL3), use imperative verbs for step-by-step test procedures ('Verify power supply voltage', 'Simulate a smoke alarm condition', 'Record the BACnet point status on the BMS workstation'). When responding to consultant review comments, use polite, action-oriented phrasing: 'The sequence diagram has been updated in Section 4.2 to clarify the Modbus HLI interface.'",
                    "Unambiguous (adj.): Not open to more than one interpretation; clear | Imperative (adj.): Giving an authoritative command or instruction | Clarify (v.): To make a statement or situation less confused and more comprehensible.",
                    "Present Perfect Passive for Document Revisions: 'The table has been revised', 'The earthing diagram has been added', 'All comments have been addressed.'"
                ),
                (
                    "Workplace English: Leading Technical Meetings & Site Walkthroughs",
                    "Confident English phrases for explaining system architectures, troubleshooting, and coordinating with teams.",
                    "Communicating clearly on site or in project meetings builds immediate professional credibility. To open a walkthrough, say: 'Today we will walk through the VESDA-E VEA aspirating smoke detection setup and verify the BMS integration.' To explain a technical issue calmly, say: 'We noticed a communication timeout on the Moxa gateway, and we are currently checking the baud rate and slave ID settings.' To close a meeting effectively, summarize action items: 'To wrap up, we will complete the pre-testing by Thursday.'",
                    "Walk through (phrasal v.): To slowly और carefully explain or inspect a process | Credibility (n.): The quality of being trusted and believed in | Wrap up (phrasal v.): To bring a meeting or task to a successful conclusion.",
                    "Polite Professional Requests: 'Could we double-check the wiring diagram?' / 'Would you mind confirming the IP address allocation?'"
                ),
                (
                    "Workplace English: Professional Emails That Get Fast Replies",
                    "Templates and phrasing for sending project updates, requesting approvals, and following up politely.",
                    "A great workplace email respects the reader's time by placing the main point in the first two sentences. Start with a clear subject line: '[Project Update] CxL3 BMS Integration Test Schedule – Rev.02'. Open warmly: 'I hope your week is going well.' State your purpose directly: 'Please find attached the revised Method of Statement for the Fire Alarm and VESDA systems.' Specify the required action: 'We would appreciate your review and approval by Friday so we can proceed with site testing next week.'",
                    "Please find attached (phrase): Standard formal phrase indicating a file is included | Proceed (v.): To begin or continue a course of action | Appreciate (v.): To be grateful for something.",
                    "Email Sign-offs: 'Best regards,' / 'Kind regards,' / 'Thank you for your continued support.'"
                ),
                (
                    "Technical English: Explaining Flowcharts & Sequence Diagrams",
                    "How to verbally present system cause-and-effect matrices and communication architectures in English.",
                    "When presenting a system flowchart or sequence diagram to clients or consultants, use clear sequential transitions to guide their eyes. Start with the trigger: 'First, when the smoke detector senses particles above the Action threshold, it sends a signal to the Fire Alarm Control Panel.' Explain the intermediate step: 'Simultaneously, the high-level interface translates the data into Modbus TCP/IP.' Conclude with the final outcome: 'As a result, the BMS triggers an audible alarm on the operator dashboard within three seconds.'",
                    "Threshold (n.): The magnitude or intensity that must be exceeded for a certain reaction to occur | Simultaneously (adv.): At the same time | Outcome (n.): The way a thing turns out; a consequence.",
                    "Cause-and-Effect Transitions: 'First / Initially' -> 'Once this occurs' -> 'Simultaneously / At the same time' -> 'Consequently / As a result'."
                )
            ]
        }
    }

    article_id = 10001
    for category, data in topics_config.items():
        for i in range(1, 41):  # 40 lessons per category = 240 lessons total
            item_tuple = data["items"][(i - 1) % len(data["items"])]
            base_title, base_summary, story_body, vocab_notes, grammar_notes = item_tuple
            img_url = data["images"][(i - 1) % len(data["images"])]
            
            full_article_text = f"""### 📖 Lesson & Story Module: {base_title} (Episode #{i})

**Learning Objective:** {base_summary}

---

### 🎧 Full Reading & Listening Script (100% English)
{story_body}

---

### 📚 Key Vocabulary & Expressions to Master
* {vocab_notes.replace(" | ", "\n* ")}

---

### 🧩 Grammar & Sentence Structure Spotlight
* **Pattern Breakdown:** {grammar_notes}
* **Speaking & Shadowing Practice:** Read the script above out loud 3 times. First, focus on clear consonant and vowel pronunciation. Second, practice linking words smoothly. Third, close your eyes and summarize the main idea in your own words in 3 sentences!
"""
            db.append({
                "id": article_id,
                "title": f"{base_title} — Ep. #{i}",
                "category": category,
                "color": data["color"],
                "time_ago": f"{(i * 3) % 50 + 5} mins read/listen",
                "views": f"{i * 150:,} learners",
                "likes": (i * 4) % 35 + 10,
                "summary": base_summary,
                "story_preview": story_body,
                "vocab_preview": vocab_notes,
                "grammar_preview": grammar_notes,
                "content": full_article_text,
                "image": img_url
            })
            article_id += 1

    return db

# ---------- Auto-Refresh Session State to Load the New 240 English Lessons ----------
if "db_version" not in st.session_state or st.session_state.db_version != "v_247_pulse_240":
    st.session_state.master_db = build_complete_english_database()
    st.session_state.db_version = "v_247_pulse_240"

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

# ---------- Helper Function to Render Rich English Lesson Cards ----------
def render_article_feed(articles_list, prefix_key="feed"):
    if not articles_list:
        st.warning("No matching lessons or stories found. Try another keyword or category.")
        return

    items_per_page = 35
    total_pages = max(1, (len(articles_list) + items_per_page - 1) // items_per_page)
    
    if total_pages > 1:
        page_num = st.selectbox(
            f"📄 Page Navigation ({len(articles_list)} English stories & lessons available)",
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
        story_text = item.get("story_preview", "")
        vocab_text = item.get("vocab_preview", "")
        grammar_text = item.get("grammar_preview", "")

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
                    <b>🎧 Story & Lesson Text:</b> {story_text}<br><br>
                    <b>📚 Key Vocabulary:</b> {vocab_text}<br>
                    <b>🧩 Grammar Focus:</b> {grammar_text}
                </div>
                <div class="h-card-meta">
                    <span>📄 Lesson ID: {item['id']}</span> &nbsp;&bull;&nbsp;
                    <span>⏱ {item['time_ago']}</span> &nbsp;&bull;&nbsp; 
                    <span>👁 {item['views']}</span> &nbsp;&bull;&nbsp; 
                    <span>❤️ {item['likes']} likes</span> &nbsp;&bull;&nbsp;
                    <span style="color: #059669; font-weight: 700;">✓ 24-7 English & English Pulse Curriculum</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        c1, c2, c3, c4 = st.columns([1.8, 1.5, 1.8, 5.9])
        with c1:
            if st.button("📖 Open Full Lesson", key=f"{prefix_key}_read_{item['id']}_{idx}"):
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
        <div class="q-brand-sub" style="padding-left: 42px;">24-7 English & Pulse Hub</div>
    </div>
    """, unsafe_allow_html=True)

    nav_options = [
        "🏠 Home (All 240)",
        "🎧 24-7 English Stories",
        "📚 Classic Books & Folklore",
        "🧩 Grammar & 12 Tenses",
        "🗣️ Speaking & Phonetics",
        "🔖 Saved Bookmarks"
    ]
    page_mapping = {
        "🏠 Home (All 240)": "Home",
        "🎧 24-7 English Stories": "24-7 English Stories",
        "📚 Classic Books & Folklore": "Classic Books & Folklore",
        "🧩 Grammar & 12 Tenses": "English Pulse: Grammar & 12 Tenses",
        "🗣️ Speaking & Phonetics": "English Pulse: Speaking & Phonetics",
        "🔖 Saved Bookmarks": "Bookmarks"
    }
    reverse_mapping = {v: k for k, v in page_mapping.items()}
    default_index = nav_options.index(reverse_mapping.get(st.session_state.current_page, "🏠 Home (All 240)"))

    selected_icon_nav = st.radio("Navigation Menu", nav_options, index=default_index, label_visibility="collapsed")
    selected_nav = page_mapping[selected_icon_nav]

    if selected_nav != st.session_state.current_page:
        st.session_state.current_page = selected_nav
        st.session_state.selected_article_id = None
        st.rerun()

    st.markdown("---")
    st.markdown("<p style='font-size:12px; font-weight:700; color:#0f2942; margin-bottom:4px;'>🔍 Search Stories & Grammar</p>", unsafe_allow_html=True)
    search_query = st.text_input("Search topics...", placeholder="Search stories, tenses, passive voice, idioms...", label_visibility="collapsed")

    st.markdown("<p style='font-size:12px; font-weight:700; color:#0f2942; margin-bottom:4px; margin-top:8px;'>🔻 Topic Filter (40 per topic)</p>", unsafe_allow_html=True)
    category_filter = st.selectbox(
        "Category Filter",
        [
            "All Categories",
            "24-7 English Stories",
            "Classic Books & Folklore",
            "English Pulse: Grammar & 12 Tenses",
            "English Pulse: Speaking & Phonetics",
            "Vocabulary & Phrasal Verbs",
            "Workplace & Technical English"
        ],
        label_visibility="collapsed"
    )

    if st.button("🔄 Reload All 240 Lessons", use_container_width=True):
        st.session_state.master_db = build_complete_english_database()
        st.rerun()

    st.markdown("""
    <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:12px; padding:10px 12px; margin-top:8px; margin-bottom:8px; box-shadow: 0 4px 12px rgba(0,0,0,0.02);">
        <div style="font-size:11px; font-weight:800; color:#0284c7; margin-bottom:6px; display:flex; align-items:center; gap:5px;">⚡ English Mastery Tracks</div>
        <div style="font-size:12px; font-weight:600; color:#1e293b; margin:4px 0;">🎧 24-7 English Listening Stories</div>
        <div style="font-size:12px; font-weight:600; color:#1e293b; margin:4px 0;">💬 English Pulse 12 Verb Tenses</div>
        <div style="font-size:12px; font-weight:600; color:#1e293b; margin:4px 0;">📖 Books, Folklore & Workplace</div>
    </div>
    """, unsafe_allow_html=True)

# ---------- Dedicated Reader Page ----------
if st.session_state.selected_article_id is not None:
    article = next((item for item in st.session_state.master_db if item["id"] == st.session_state.selected_article_id), None)

    if article:
        if st.button("← Back to Lesson Feed"):
            st.session_state.selected_article_id = None
            st.rerun()

        col_img, col_txt = st.columns([1.2, 2.8])
        with col_img:
            st.image(article.get("image"), use_container_width=True)
            st.markdown(f"**🏷️ Module:** `{article['category']}`")
            st.markdown(f"**⏱️ Practice Time:** {article['time_ago']}")
            st.markdown(f"**👁️ Learners:** {article['views']}")
            st.markdown(f"**❤️ Likes:** {article['likes']}")
        with col_txt:
            st.markdown(f"## {article['title']}")
            st.markdown(article.get('content'))
        st.stop()

# ---------- Main Routing for Specific Pages ----------
if st.session_state.current_page == "24-7 English Stories":
    st.markdown("## 🎧 24-7 English Stories (40 Listening & Reading Tales)")
    st.caption("Immersive moral stories, daily conversations, and suspense tales to build natural English comprehension.")
    list_247 = [i for i in st.session_state.master_db if i['category'] == '24-7 English Stories']
    render_article_feed(list_247, prefix_key="page_247")

elif st.session_state.current_page == "Classic Books & Folklore":
    st.markdown("## 📚 Classic Books & World Folklore (40 Adapted Stories)")
    st.caption("Read timeless stories including Tam and Cam, The Alchemist's Journey, The Old Fisherman, and Aesop's Fables in clear English.")
    list_books = [i for i in st.session_state.master_db if i['category'] == 'Classic Books & Folklore']
    render_article_feed(list_books, prefix_key="page_books")

elif st.session_state.current_page == "English Pulse: Grammar & 12 Tenses":
    st.markdown("## 🧩 English Pulse: Grammar, 12 Tenses & Sentence Patterns (40 Lessons)")
    st.caption("Master the 12 verb tenses, active vs. passive voice constructions, and the 5 basic sentence structure patterns.")
    list_grammar = [i for i in st.session_state.master_db if i['category'] == 'English Pulse: Grammar & 12 Tenses']
    render_article_feed(list_grammar, prefix_key="page_grammar")

elif st.session_state.current_page == "English Pulse: Speaking & Phonetics":
    st.markdown("## 🗣️ English Pulse: Speaking, Phonetics & Shadowing (80 Lessons)")
    st.caption("Consonants & vowels pronunciation, word stress, phrasal verbs, and workplace English communication.")
    list_speaking = [
        i for i in st.session_state.master_db
        if i['category'] in ['English Pulse: Speaking & Phonetics', 'Vocabulary & Phrasal Verbs', 'Workplace & Technical English']
    ]
    render_article_feed(list_speaking, prefix_key="page_speaking")

elif st.session_state.current_page == "Bookmarks":
    st.markdown(f"## 🔖 Your Saved English Lessons ({len(st.session_state.bookmarks)} Saved)")
    st.caption("Review your bookmarked stories, vocabulary lists, and grammar patterns anytime.")
    saved_items = [i for i in st.session_state.master_db if i['id'] in st.session_state.bookmarks]
    render_article_feed(saved_items, prefix_key="page_bookmarks")

else:
    # ---------- HOME PAGE DASHBOARD ----------
    st.markdown(f"""
    <div class="hero">
        <div style="position:absolute; right:20px; top:12px; font-size:11px; color:#e0f2fe; font-weight:500;">{datetime.now().strftime('%a, %d %b %Y %H:%M:%S')} &bull; <span style="color:#4ade80; font-weight:700;">● 100% English Immersion</span></div>
        <div class="usp-badge">🛡️ 24-7 English &bull; English Pulse &bull; Books & Stories &bull; 240 Complete Lessons</div>
        <h1>QELVYQ — 24-7 English & English Pulse Mastery Hub.</h1>
        <p>Your complete all-in-one platform for English stories, classic books, the 12 verb tenses, active/passive voice, vocabulary, and conversational fluency.</p>
    </div>
    """, unsafe_allow_html=True)

    filtered_articles = st.session_state.master_db
    if search_query:
        filtered_articles = [
            a for a in filtered_articles
            if search_query.lower() in a['title'].lower()
            or search_query.lower() in a['summary'].lower()
            or search_query.lower() in a.get('story_preview', '').lower()
            or search_query.lower() in a.get('vocab_preview', '').lower()
            or search_query.lower() in a.get('grammar_preview', '').lower()
        ]
    if category_filter != "All Categories":
        filtered_articles = [a for a in filtered_articles if a['category'].lower() == category_filter.lower()]

    st.markdown(f"""
    <div class="section-head">
        <h3>Complete English Stories, Books & Fluency Lessons ({len(filtered_articles)} Available)</h3>
    </div>
    <div class="section-sub">✨ Showing full story scripts, key vocabulary, and grammar patterns for: <b>{category_filter}</b></div>
    """, unsafe_allow_html=True)

    render_article_feed(filtered_articles, prefix_key="home_feed")

st.markdown("<br>", unsafe_allow_html=True)

# ---------- True Real-Time Metrics Grid ----------
m1, m2, m3, m4, m5 = st.columns(5)
with m1: st.metric("Live Active Learners", f"{real_active_users} online", "🟢 Real-time session")
with m2: st.metric("Total Page Views", f"{st.session_state.page_views:,}", "📈 Live counter")
with m3: st.metric("Est. AdSense Revenue", f"${real_adsense_revenue:,.4f} USD", "💎 Calculated real-time")
with m4: st.metric("Total English Lessons", f"{len(st.session_state.master_db)} active", "⚡ 40 per topic")
with m5: st.metric("Saved Bookmarks", f"{len(st.session_state.bookmarks)} saved", "🔖 True user saves")

st.markdown("""
<div class="footer">
    QELVYQ &bull; 24-7 English & English Pulse Mastery Hub &bull; 100% English Immersion Edition
</div>
""", unsafe_allow_html=True)
