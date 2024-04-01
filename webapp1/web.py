
import functions as fc
import streamlit as st

todos = fc.get_todos()
def add_toDo():
    todo=st.session_state["new_todo"]+"\n"
    if(todo!=""):
        todos.append(todo)
        fc.write_todos(todos)
        st.session_state["new_todo"]=""

todos=fc.get_todos()

st.header("To Do list made by Doulgas")
st.write("This is a todo app to help you be more productive and never forget a thing")

for index,todo in enumerate(todos):
    checkbox=st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        fc.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="",placeholder="Add a new todo on your list..",
              on_change=add_toDo,key='new_todo')