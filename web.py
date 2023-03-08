import streamlit as st          # pip install streamlit
from modules import functions   # import funtions from modules/funtions.py

todos = functions.get_todos()   # get todos list

def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo + '\n')
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""      # clear input text box after enter/add
    
st.title("My Todo App")
st.subheader("This is my to app")
st.write("This app si to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        #print(index)
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]     # remove todo from sesstion state
        st.experimental_rerun()        # rerun
    
st.text_input(label="Enter a new todo:", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

#st.session_state    # show current sesstion state, keys and values