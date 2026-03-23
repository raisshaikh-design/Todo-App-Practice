import streamlit as st
import requests

st.title("Local Android LLM")

# Input from user
user_input = st.text_area("Enter text to improve:")

if st.button("Improve Text"):
    # Assuming your local Android LLM server is running on port 11434
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "gemma:2b",  # Use a mobile-friendly model
            "prompt": f"Improve this text: {user_input}",
            "stream": False
        }
    )
    st.write(response.json().get("response"))
