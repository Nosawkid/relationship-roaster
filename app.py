import streamlit as st
import os
from groq import Groq

# --- CONFIGURATION ---
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# --- PAGE SETUP ---
st.set_page_config(page_title="Why Are You Single?", page_icon="💔", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ff4b4b; }
    h1 { text-align: center; color: #ff4b4b !important; font-family: 'Courier New', monospace; font-weight: 800; }
    .stTextArea textarea { background-color: #262730; color: white; border: 1px solid #4a4a4a; }
    div[data-testid="stMarkdownContainer"] p { font-size: 1.2rem; color: #bdbdbd; }
    </style>
    """, unsafe_allow_html=True)

# --- APP LOGIC ---
st.title("💔 WHY ARE YOU SINGLE?")
st.markdown("*An AI that uses advanced algorithms to hurt your feelings.*")
st.write("---")

user_bio = st.text_area("Tell me about yourself (Job, Hobbies, Age):", height=150, placeholder="Example: I'm a 24-year-old developer...")

if st.button("🔥 ROAST ME", type="primary"):
    if not user_bio:
        st.warning("Give me something to work with.")
    else:
        with st.spinner("Analyzing your flaws..."):
            try:
                # --- THE UPDATED "MEAN" PROMPT ---
                system_prompt = """
                You are a ruthless, cynical stand-up comedian and psychological profiler. 
                Your job is to roast the user by explaining EXACTLY why they are single based on their bio.

                ### GUIDELINES:
                1. **Be Analytical yet Brutal:** Don't just insult them; deconstruct their life choices. Connect A (their job) to B (their loneliness).
                2. **No Mercy:** If they are a developer, mock their god complex or lack of social skills. If they mention gym, mock their vanity. If they mention anime, mock their delusion.
                3. **Format:** You must provide a paragraph between 3 to 6 sentences long.
                4. **Tone:** Dry, witty, dark, and observant. No emojis. No "just kidding."
                5. **The Hook:** Start with a direct attack on their most prominent trait.

                Example Output for a Dev:
                "You treat dating like a debugging session, expecting a stack trace for every failed interaction. The reality is that human emotions don't have documentation, and you can't push a hotfix for your personality. You're single because you're waiting for a partner who is open-source and specifically typed, but you bring nothing to the repo but legacy code and anxiety."
                """

                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "system",
                            "content": system_prompt
                        },
                        {
                            "role": "user",
                            "content": user_bio,
                        }
                    ],
                    model="llama-3.3-70b-versatile",  # <--- FIXED COMMA HERE
                    temperature=1.0, 
                )
                
                roast_text = chat_completion.choices[0].message.content
                st.success("Analysis Complete:")
                st.info(roast_text)
                
            except Exception as e:
                st.error(f"Error: {e}")

st.write("---")
st.caption("Hosted on Streamlit Cloud • Powered by Llama 3")