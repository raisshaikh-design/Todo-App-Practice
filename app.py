import streamlit as st

# 1. Setup Session State
if "tasks" not in st.session_state:
    st.session_state.tasks = [] # List of dicts: {"name": str, "done": bool}

st.title("📱 Task Master")

# 2. Mobile-style Navigation Bar
page = st.segmented_control(
    "Navigation", 
    ["Current", "Completed", "Settings"], 
    default="Current",
    label_visibility="collapsed"
)

st.divider()

# --- PAGE: CURRENT TASKS ---
if page == "Current":
    new_task = st.text_input("Add new task", placeholder="Enter task...")
    if st.button("Add", use_container_width=True) and new_task:
        st.session_state.tasks.append({"name": new_task, "done": False})
        st.rerun()

    for i, task in enumerate(st.session_state.tasks):
        if not task["done"]:
            col1, col2 = st.columns([0.8, 0.2])
            col1.write(f"⭕ {task['name']}")
            if col2.button("✅", key=f"done_{i}"):
                task["done"] = True
                st.rerun()

# --- PAGE: COMPLETED ---
elif page == "Completed":
    st.subheader("Finished Tasks")
    for task in st.session_state.tasks:
        if task["done"]:
            st.write(f"✔️ ~{task['name']}~")
    
    if st.button("Clear History"):
        st.session_state.tasks = [t for t in st.session_state.tasks if not t["done"]]
        st.rerun()

# --- PAGE: SETTINGS ---
elif page == "Settings":
    st.subheader("App Settings")
    st.color_picker("Theme Color", "#FF4B4B")
    if st.button("Delete All Data", type="primary"):
        st.session_state.tasks = []
        st.rerun()
