import streamlit as st
import streamlit.components.v1 as components

# 1. INITIALIZE APP STATE (Prevents the AttributeError)
if "tasks" not in st.session_state:
    st.session_state.tasks = []  # List of dicts: {"name": str, "done": bool}

st.set_page_config(page_title="Task Master AI", page_icon="✅")

# 2. MOBILE NAVIGATION BAR
st.title("📱 Task Master")
page = st.segmented_control(
    "Navigation", 
    ["Current", "Completed", "Settings"], 
    default="Current",
    label_visibility="collapsed"
)
st.divider()

# --- HELPER: GEMINI INTENT BUTTON ---
import streamlit as st
import streamlit.components.v1 as components
import urllib.parse

def share_to_gemini(task_text):
    # 1. Prepare the URL
    query = urllib.parse.quote(task_text)
    gemini_url = f"https://gemini.google.com{query}"
    
    # 2. JavaScript that COPIES text first, then provides a link
    # This avoids the "about:blank#blocked" because the link is a simple <a> tag
    html_code = f"""
    <div style="background:#f0f2f6; padding:15px; border-radius:10px; border:1px solid #dcdfe3;">
        <p style="margin:0 0 10px 0; font-family:sans-serif; font-size:14px; color:#31333F;">
            <b>Step 1:</b> Copy your tasks
        </p>
        <button onclick="navigator.clipboard.writeText('{task_text}'); alert('Tasks Copied!')" 
            style="width:100%; background-color:#4285F4; color:white; border:none; padding:10px; border-radius:5px; cursor:pointer; font-weight:bold;">
            📋 Click to Copy Tasks
        </button>
        <p style="margin:15px 0 10px 0; font-family:sans-serif; font-size:14px; color:#31333F;">
            <b>Step 2:</b> Open Gemini and Paste
        </p>
        <a href="{gemini_url}" target="_blank" style="text-decoration:none;">
            <div style="width:100%; background-color:#1a73e8; color:white; padding:10px; border-radius:5px; text-align:center; font-weight:bold;">
                ✨ Open Gemini App
            </div>
        </a>
    </div>
    """
    components.html(html_code, height=180)

# Example Usage:
tasks = [t['name'] for t in st.session_state.tasks if not t['done']]
if tasks:
    prompt = f"Plan these tasks for me: {', '.join(tasks)}"
    share_to_gemini(prompt)


# --- PAGE: CURRENT TASKS ---
if page == "Current":
    # Add Task Input
    with st.container():
        new_task = st.text_input("Add new task", placeholder="What's on your mind?")
        if st.button("Add Task", use_container_width=True) and new_task:
            st.session_state.tasks.append({"name": new_task, "done": False})
            st.rerun()

    st.write("### Your List")
    active_tasks = [t for t in st.session_state.tasks if not t['done']]
    
    if not active_tasks:
        st.info("All caught up! Add a task to start.")
    else:
        for i, task in enumerate(st.session_state.tasks):
            if not task["done"]:
                col1, col2 = st.columns([0.8, 0.2])
                col1.write(f"⭕ {task['name']}")
                if col2.button("✅", key=f"done_{i}"):
                    task["done"] = True
                    st.rerun()
        
        # GEMINI ACTION
        st.divider()
        task_names = [t['name'] for t in active_tasks]
        prompt = f"I have these tasks: {', '.join(task_names)}. Can you help me prioritize them and give a quick 1-sentence tip for the most important one?"
        share_to_gemini(prompt)

# --- PAGE: COMPLETED ---
elif page == "Completed":
    st.subheader("Completed Tasks")
    completed_tasks = [t for t in st.session_state.tasks if t['done']]
    
    if not completed_tasks:
        st.write("No completed tasks yet.")
    else:
        for task in completed_tasks:
            st.write(f"✔️ ~~{task['name']}~~")
        
        if st.button("Clear History", type="secondary"):
            st.session_state.tasks = [t for t in st.session_state.tasks if not t["done"]]
            st.rerun()

# --- PAGE: SETTINGS ---
elif page == "Settings":
    st.subheader("App Settings")
    st.write("Customize your experience.")
    st.color_picker("App Accent Color", "#4285F4")
    
    if st.button("Reset All Data", type="primary", use_container_width=True):
        st.session_state.tasks = []
        st.rerun()
