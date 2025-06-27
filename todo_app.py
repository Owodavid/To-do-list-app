import streamlit as st

# Title and subtitle
st.title("📝 To-Do List App")
st.subheader("A simple task manager built with Streamlit")

# Create a placeholder dictionary to hold tasks (use session state)
if "todo_list" not in st.session_state:
    st.session_state.todo_list = {}

# Input fields to add task
with st.form("task_form", clear_on_submit=True):
    date = st.text_input("Enter the task deadline (e.g. 25-06-25 13:00)")
    task = st.text_input("Enter the task details")
    submitted = st.form_submit_button("Add Task")
    
    if submitted:
        if date and task:
            st.session_state.todo_list[date] = task
            st.success("Task added!")
        else:
            st.error("Please enter both deadline and task")

# Show current tasks
st.write("### 📋 Current Tasks")
if st.session_state.todo_list:
    for date, task in list(st.session_state.todo_list.items()):
        col1, col2 = st.columns([4, 1])
        col1.write(f"**{date}** — {task}")
        if col2.button("✅ Done", key=date):
            del st.session_state.todo_list[date]
            st.rerun()
else:
    st.info("Your list is empty!")

# Clear all button
if st.button("🗑️ Clear Entire List"):
    st.session_state.todo_list.clear()
    st.rerun()