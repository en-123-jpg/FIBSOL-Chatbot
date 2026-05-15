import streamlit as st
from app import run_agent

st.title("Biofertilizer AI Agent")

query = st.text_input("Ask something:")

if st.button("Run"):
    st.write(run_agent(query))