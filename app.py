import streamlit as st

st.title("✅ My To-Do List")

# 1. Initialize the list in the "Session State" so it doesn't reset
if "todos" not in st.session_state:
    st.session_state.todos = []

# 2. Input to add a new task
new_todo = st.text_input("What needs to be done?", placeholder="Enter a task...")

if st.button("Add Task"):
    if new_todo:
        st.session_state.todos.append(new_todo)
        st.rerun() # Refresh the app to show the new item

# 3. Display the list with "Done" buttons
st.write("---")
for index, task in enumerate(st.session_state.todos):
    col1, col2 = st.columns([0.8, 0.2])
    col1.write(f"**{index + 1}.** {task}")
    
    # Unique key for each button
    if col2.button("Done", key=f"btn_{index}"):
        st.session_state.todos.pop(index)
        st.rerun()

# 4. Sidebar info
st.sidebar.info(f"You have {len(st.session_state.todos)} tasks remaining.")
