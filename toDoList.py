import streamlit as st

st.title("📝 My To-Do List")

# Initialize session state
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Add new task
task = st.text_input("Enter a new task")

if st.button("Add Task"):
    if task:
        st.session_state.tasks.append({"task": task, "done": False})

st.subheader("Your Tasks")

# Display tasks
for i, task in enumerate(st.session_state.tasks):
    
    col1, col2, col3 = st.columns([6,2,2])

    with col1:
        if task["done"]:
            st.write(f"✅ ~~{task['task']}~~")
        else:
            st.write(task["task"])

    with col2:
        if st.button("Done", key=f"done{i}"):
            st.session_state.tasks[i]["done"] = True

    with col3:
        if st.button("Delete", key=f"delete{i}"):
            st.session_state.tasks.pop(i)
            st.experimental_rerun()