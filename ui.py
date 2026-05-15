import streamlit as st
from app import run_agent

st.set_page_config(
    page_title="FIB-SOL AI",
    page_icon="🌱",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>

/* Main background */
.stApp {
    background-color: #0f1117;
    color: white;
}

/* Hide default header */
header {
    visibility: hidden;
}

/* Chat bubbles */
.user-msg {
    background-color: #1e293b;
    padding: 14px;
    border-radius: 18px;
    margin-bottom: 12px;
    font-size: 16px;
}

.bot-msg {
    background-color: #161b22;
    padding: 16px;
    border-radius: 18px;
    margin-bottom: 20px;
    border: 1px solid #2d3748;
    font-size: 16px;
    line-height: 1.7;
}

/* Bottom input area */
.stChatInputContainer {
    background-color: #0f1117;
}

/* Spinner */
.loading {
    display: flex;
    gap: 6px;
    padding: 10px 0;
}

.loading span {
    width: 10px;
    height: 10px;
    background: #4ade80;
    border-radius: 50%;
    animation: bounce 1.4s infinite ease-in-out both;
}

.loading span:nth-child(1) {
    animation-delay: -0.32s;
}

.loading span:nth-child(2) {
    animation-delay: -0.16s;
}

@keyframes bounce {
    0%, 80%, 100% {
        transform: scale(0);
    }
    40% {
        transform: scale(1);
    }
}

</style>
""", unsafe_allow_html=True)

# Title
st.markdown(
    "<h1 style='text-align:center;'>FIB-SOL AI </h1>",
    unsafe_allow_html=True
)

# Session state for messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat
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

# ChatGPT-style bottom input
prompt = st.chat_input("Ask about crops, products, dosage, soil health...")

# When user sends message
if prompt:

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # Display user message
    st.markdown(
        f"<div class='user-msg'>{prompt}</div>",
        unsafe_allow_html=True
    )

    # Loading animation
    loading_placeholder = st.empty()

    loading_placeholder.markdown("""
    <div class='loading'>
        <span></span>
        <span></span>
        <span></span>
    </div>
    """, unsafe_allow_html=True)

    # Generate response
    response = run_agent(prompt)

    # Remove loading animation
    loading_placeholder.empty()

    # Save bot response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    # Display response
    st.markdown(
        f"<div class='bot-msg'>{response}</div>",
        unsafe_allow_html=True
    )
