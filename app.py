import streamlit as st
import streamlit.components.v1 as components

# 1. Define the share function
def android_share(text):
    # This JS checks if the browser supports native sharing (Chrome/Android)
    js_code = f"""
    <script>
    function share() {{
        if (navigator.share) {{
            navigator.share({{
                title: 'My Tasks',
                text: '{text}',
                url: window.location.href
            }}).then(() => console.log('Successful share'))
              .catch((error) => console.log('Error sharing', error));
        }} else {{
            alert("Web Share not supported on this browser.");
        }}
    }}
    </script>
    <button onclick="share()" style="
        width: 100%; 
        background-color: #FF4B4B; 
        color: white; 
        border: none; 
        padding: 10px; 
        border-radius: 5px;
        cursor: pointer;">
        📤 Share Tasks to AI Apps
    </button>
    """
    components.html(js_code, height=60)

# 2. Call it in your app
st.subheader("Action")
tasks_string = ", ".join([t['name'] for t in st.session_state.tasks if not t['done']])
android_share(f"Here are my current tasks: {tasks_string}")
