import base64
import streamlit as st
from app import run_agent

# PAGE CONFIG
st.set_page_config(
    page_title="FIB-SOL AI",
    page_icon="logo.png",
    layout="wide"
)

# FUNCTION TO LOAD IMAGE
def get_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

bg_image = get_base64("bg.jpg")

# CUSTOM CSS
st.markdown(f"""
<style>

/* Entire app background */
.stApp {{
    background-image: url("data:image/jpg;base64,{bg_image}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    color: white;
}}

/* Hide Streamlit stuff */
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
    backdrop-filter: blur(3px);
}}

.hero h1 {{
    font-size: 72px;
    margin-bottom: 10px;
}}

.hero p {{
    font-size: 24px;
    width: 70%;
    line-height: 1.6;
}}

/* Scroll button */
.chat-btn {{
    margin-top: 40px;
    background-color: #22c55e;
    color: white;
    padding: 16px 34px;
    border-radius: 999px;
    font-size: 20px;
    text-decoration: none;
    transition: 0.3s;
}}

.chat-btn:hover {{
    background-color: #16a34a;
    transform: scale(1.05);
}}

/* Chat section */
.chat-section {{
    margin-top: 100px;
    padding-bottom: 100px;
}}

/* Messages */
.user-msg {{
    background-color: rgba(30,41,59,0.85);
    padding: 14px 18px;
    border-radius: 18px;
    margin-bottom: 14px;
    width: fit-content;
    max-width: 75%;
    margin-left: auto;
    font-size: 16px;
}}

.bot-msg {{
    padding: 12px 4px;
    margin-bottom: 24px;
    max-width: 85%;
    font-size: 17px;
    line-height: 1.8;
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

# HERO SECTION
st.markdown("""
<div class="hero">
    <h1>🌱 FIB-SOL AI</h1>

    <p>
    Intelligent biofertilizer assistance powered by AI.
    Get product recommendations, crop guidance, dosage support,
    and agricultural insights instantly.
    </p>

    <a href="#chatbot">
        <button class="chat-btn">
            Chat With Our Bot
        </button>
    </a>
</div>
""", unsafe_allow_html=True)

# CHAT SECTION
st.markdown('<div id="chatbot" class="chat-section"></div>', unsafe_allow_html=True)

# SESSION STATE
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
prompt = st.chat_input("Ask about crops, products, dosage...")

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
