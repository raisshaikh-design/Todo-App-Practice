import streamlit as st
import streamlit.components.v1 as components

def share_to_gemini(task_text):
    # Intent URL specifically for the Gemini App
    # This sends a "SEND" action with your text directly to the Gemini package
    intent_url = f"intent:#Intent;action=android.intent.action.SEND;type=text/plain;S.android.intent.extra.TEXT={task_text};package=com.google.android.apps.bard;end"
    
    # Custom HTML button to trigger the intent
    design = f"""
    <a href="{intent_url}" style="text-decoration:none;">
        <button style="
            width: 100%; 
            background-color: #4285F4; 
            color: white; 
            border: none; 
            padding: 12px; 
            border-radius: 8px; 
            font-weight: bold;
            cursor: pointer;">
            ✨ Send Tasks to Gemini AI
        </button>
    </a>
    """
    components.html(design, height=70)

# Example Usage:
tasks = [t['name'] for t in st.session_state.tasks if not t['done']]
if tasks:
    prompt = f"Can you help me prioritize or suggest a plan for these tasks: {', '.join(tasks)}?"
    share_to_gemini(prompt)
else:
    st.info("Add some tasks first to share with Gemini!")
