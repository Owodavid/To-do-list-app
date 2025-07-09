import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io

def generate_pdf(todo_dict):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    c.setFont("Times-Roman", 17)
    c.drawString(100, height - 50, "Your To-Do List")

    c.setFont("Times-Roman", 11)
    y = height - 100
    for deadline, task in todo_dict.items():
        if y < 50:
            c.showPage()
            y = height - 50
        c.drawString(60, y, f"- {deadline}: {task}")
        y -= 20

    c.save()
    buffer.seek(0)
    return buffer


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

col1, col2, col3 = st.columns([2, 6, 3])  # adjust ratios as needed

with col1:
    if st.button("🗑️ Clear List"):
        st.session_state.todo_list.clear()
        st.success("List cleared!")

with col3:
    if st.session_state.todo_list:
        pdf_buffer = generate_pdf(st.session_state.todo_list)
        st.download_button(
            label="📄Generate PDF",
            data=pdf_buffer,
            file_name="todo_list.pdf",
            mime="application/pdf"
        )