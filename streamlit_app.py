import streamlit as st
from generator import FootballSessionGenerator

# Page config
st.set_page_config(page_title="AI Football Coach", page_icon="⚽")

st.title("⚽ Elite Football Coach AI")
st.markdown("---")

# Sidebar for inputs
st.sidebar.header("Session Requirements")
age = st.sidebar.selectbox("Age Group", ["U6-U8", "U10-U12", "U14-U16", "Senior"])
skill = st.sidebar.text_input("Focus Skill", placeholder="e.g. Dribbling")
players = st.sidebar.slider("Number of Players", 2, 22, 12)

if st.sidebar.button("Generate Session"):
    with st.spinner("Coach is thinking..."):
        try:
            gen = FootballSessionGenerator()
            output = gen.generate_session(age, skill, players)
            st.markdown(output)
        except Exception as e:
            st.error("Make sure your API Key is set up in your .env file!")
