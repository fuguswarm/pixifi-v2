import streamlit as st
import random
from recommender.tool import recommend

st.set_page_config(page_title="DeFi Protocol Recommender", layout="wide")
st.title("🔍 DeFi Protocol Recommender")

user_input = st.text_input("💬 Your favorite project or theme:")

loading_messages = [
    "🔍 Analyzing DeFi protocols...",
    "⏳ Crunching the numbers...",
    "🤖 Fetching the latest data...",
    "📊 Compiling recommendations..."
]

if st.button("🔎 Recommend"):
    if not user_input:
        st.warning("Please enter a valid prompt.")
    else:
        with st.spinner(random.choice(loading_messages)):
            result = recommend(user_input)
        st.success("✅ Here are your protocol recommendations:")
        st.markdown(result, unsafe_allow_html=True)
