import streamlit as st

# Launch Play Store directly to a specific app package
st.link_button("Install ChatGPT App", "https://play.google.com")

# Technical Intent syntax (Chrome only)
intent_url = "intent://details?id=com.openai.chatgpt#Intent;scheme=market;package=com.android.vending;end"
st.markdown(f'<a href="{intent_url}" target="_blank">Open in Play Store App</a>', unsafe_allow_html=True)
