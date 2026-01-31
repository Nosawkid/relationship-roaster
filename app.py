import streamlit as st
import requests
import json

# --- CONFIGURATION ---
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "single-roaster"  # The model we created earlier

# --- PAGE SETUP ---
st.set_page_config(page_title="Why Are You Single?", page_icon="💔", layout="centered")

# Custom CSS for the "Roaster" Vibe (Red & Black)
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        color: #ff4b4b;
    }
    h1 {
        text-align: center;
        color: #ff4b4b !important;
        font-family: 'Courier New', monospace;
        font-weight: 800;
    }
    .stTextArea textarea {
        background-color: #262730;
        color: white;
        border: 1px solid #4a4a4a;
    }
    div[data-testid="stMarkdownContainer"] p {
        font-size: 1.2rem;
        color: #bdbdbd;
    }
    </style>
    """, unsafe_allow_html=True)

# --- APP LOGIC ---
st.title("💔 WHY ARE YOU SINGLE?")
st.markdown("*An AI that uses advanced algorithms to hurt your feelings.*")

st.write("---")

# Input Section
user_bio = st.text_area("Tell me about yourself (Job, Hobbies, Age):", height=150, placeholder="Example: I'm a 24-year-old developer who loves Star Wars and has a best friend I'm secretly in love with...")

# The Button
if st.button("🔥 ROAST ME", type="primary"):
    if not user_bio:
        st.warning("Give me something to work with. I can't roast a ghost.")
    else:
        with st.spinner("Analyzing your flaws..."):
            try:
                # Call Ollama API
                payload = {
                    "model": MODEL_NAME,
                    "prompt": user_bio,
                    "stream": False,
                    "options": {"temperature": 0.8}
                }
                response = requests.post(OLLAMA_URL, json=payload)
                
                if response.status_code == 200:
                    result = response.json()
                    roast_text = result.get("response", "Error parsing response.")
                    
                    # Display the result
                    st.success("Analysis Complete:")
                    st.markdown(f"### 🤖 THE VERDICT:")
                    st.info(roast_text)
                else:
                    st.error(f"Error: {response.status_code} - Is Ollama running?")
                    
            except requests.exceptions.ConnectionError:
                st.error("🚨 CONNECTION ERROR: Make sure Ollama is running! Run `ollama serve` in your terminal.")

st.write("---")
st.caption("Powered by Local AI (Ollama) • Private & Offline")