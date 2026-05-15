
import base64
import streamlit as st
from app import run_agent

# PAGE CONFIG
st.set_page_config(
    page_title="FIB-SOL AI",
    page_icon="logo.png",
    layout="wide"
)

# LOAD BACKGROUND IMAGE

def get_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

bg_image = get_base64("bg.jpg")

# CUSTOM CSS
st.markdown(f"""
<style>

html {{
    scroll-behavior: smooth;
}}

/* App Background */
.stApp {{
    background-image: linear-gradient(rgba(0,0,0,0.55), rgba(0,0,0,0.65)),
    url("data:image/jpg;base64,{bg_image}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    color: white;
}}

/* Hide streamlit junk */
header {{
    visibility: hidden;
}}

#MainMenu {{
    visibility: hidden;
}}

footer {{
    visibility: hidden;
}}

/* Hero section */
.hero {{
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 0 10%;
}}

.hero h1 {{
    font-size: 82px;
    margin-bottom: 20px;
}}

.hero p {{
    font-size: 24px;
    max-width: 900px;
    line-height: 1.8;
}}

/* Floating chat button */
.floating-chat {{
    position: fixed;
    right: 30px;
    bottom: 30px;
    z-index: 999;
}}

.floating-chat a {{
    text-decoration: none;
    background-color: #22c55e;
    color: white;
    padding: 16px 24px;
    border-radius: 999px;
    font-size: 18px;
    font-weight: bold;
    box-shadow: 0 4px 18px rgba(0,0,0,0.35);
    transition: 0.3s;
}}

.floating-chat a:hover {{
    background-color: #16a34a;
    transform: scale(1.05);
}}

/* Section cards */
.section-card {{
    background: rgba(17, 24, 39, 0.75);
    backdrop-filter: blur(6px);
    padding: 40px;
    border-radius: 28px;
    margin-bottom: 35px;
    border: 1px solid rgba(255,255,255,0.08);
}}

.section-card h2 {{
    color: #4ade80;
    margin-bottom: 20px;
}}

.section-card p,
.section-card li {{
    font-size: 18px;
    line-height: 1.8;
}}

/* Chat area */
.chat-title {{
    text-align: center;
    margin-top: 100px;
    margin-bottom: 40px;
}}

.chat-title h1 {{
    font-size: 48px;
}}

.user-msg {{
    background-color: rgba(30,41,59,0.9);
    padding: 16px 20px;
    border-radius: 20px;
    margin-bottom: 18px;
    width: fit-content;
    max-width: 75%;
    margin-left: auto;
    font-size: 16px;
}}

.bot-msg {{
    padding: 14px 4px;
    margin-bottom: 26px;
    max-width: 85%;
    font-size: 17px;
    line-height: 1.9;
}}

/* Loading animation */
.loading {{
    display: flex;
    gap: 6px;
    padding: 12px 0;
}}

.loading span {{
    width: 10px;
    height: 10px;
    background: #4ade80;
    border-radius: 50%;
    animation: bounce 1.4s infinite ease-in-out both;
}}

.loading span:nth-child(1) {{
    animation-delay: -0.32s;
}}

.loading span:nth-child(2) {{
    animation-delay: -0.16s;
}}

@keyframes bounce {{
    0%, 80%, 100% {{
        transform: scale(0);
    }}
    40% {{
        transform: scale(1);
    }}
}}

</style>
""", unsafe_allow_html=True)

# FLOATING CHAT BUTTON
st.markdown("""
<div class="floating-chat">
    <a href="#chatbot">💬 Chat With Our Bot</a>
</div>
""", unsafe_allow_html=True)

# HERO SECTION
st.markdown("""
<div class="hero">
    <h1>🌱 FIB-SOL AI</h1>

    <p>
    Revolutionizing sustainable agriculture with advanced microbial formulations,
    intelligent crop solutions, and AI-powered agricultural assistance.
    </p>
</div>
""", unsafe_allow_html=True)

# OVERVIEW SECTION
st.markdown("""
<div class="section-card">
    <h2>Company Overview</h2>

    <p>
    FIB-SOL Life Technologies is focused on next-generation biofertilizer and
    microbial agricultural solutions designed to improve crop productivity,
    soil health, nutrient uptake, and sustainability.
    </p>

    <p>
    The company specializes in advanced gel-based microbial technology with
    high microbial payload, long shelf life, and reduced logistics footprint.
    </p>
</div>
""", unsafe_allow_html=True)

# TECHNOLOGY SECTION
st.markdown("""
<div class="section-card">
    <h2>IG4 Technology</h2>

    <ul>
        <li>High microbial payload formulation technology</li>
        <li>18+ months stability</li>
        <li>100% water soluble</li>
        <li>Reduced logistics and storage costs</li>
        <li>Flexible microbial combinations</li>
        <li>Lower contamination risk</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# PRODUCTS SECTION
st.markdown("""
<div class="section-card">
    <h2>Core Products</h2>

    <ul>
        <li><b>Sakthi Max</b> – Soil nutrition and vegetative growth support</li>
        <li><b>Surya Max</b> – Flowering and fruiting enhancement</li>
        <li><b>Nutrigel Plus</b> – Balanced foliar nutrition</li>
        <li><b>Super-Tri</b> – Natural microbial fungicide</li>
        <li><b>Super-Soil</b> – Soil disease prevention and immunity support</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# BENEFITS SECTION
st.markdown("""
<div class="section-card">
    <h2>Why FIB-SOL?</h2>

    <ul>
        <li>Improves nutrient absorption</li>
        <li>Supports higher crop yield</li>
        <li>Enhances plant immunity</li>
        <li>Reduces dependency on chemical fertilizers</li>
        <li>Eco-friendly and sustainable</li>
        <li>Supports multiple application methods</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# CHAT SECTION
st.markdown('<div id="chatbot"></div>', unsafe_allow_html=True)

st.markdown("""
<div class="chat-title">
    <h1>💬 FIB-SOL AI Assistant</h1>
</div>
""", unsafe_allow_html=True)

# CHAT HISTORY
if "messages" not in st.session_state:
    st.session_state.messages = []

# DISPLAY CHAT
for message in st.session_state.messages:

    if message["role"] == "user":
        st.markdown(
            f"<div class='user-msg'>{message['content']}</div>",
            unsafe_allow_html=True
        )

    else:
        st.markdown(
            f"<div class='bot-msg'>{message['content']}</div>",
            unsafe_allow_html=True
        )

# CHAT INPUT
prompt = st.chat_input("Ask about crops, dosage, products, soil health...")

# RESPONSE
if prompt:

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    st.markdown(
        f"<div class='user-msg'>{prompt}</div>",
        unsafe_allow_html=True
    )

    loading = st.empty()

    loading.markdown("""
    <div class='loading'>
        <span></span>
        <span></span>
        <span></span>
    </div>
    """, unsafe_allow_html=True)

    response = run_agent(prompt)

    loading.empty()

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    st.markdown(
        f"<div class='bot-msg'>{response}</div>",
        unsafe_allow_html=True
    )
