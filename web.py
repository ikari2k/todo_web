import streamlit as st
import functions

st.set_page_config(page_title='Ikari2k Todo App', layout="wide")
todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my todo list:")
st.write("This app is to increase your <b>productivity</b>",unsafe_allow_html=True)

st.text_input(label="New todo" , placeholder="Add new todo...", 
              label_visibility="hidden", on_change=add_todo, key='new_todo')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()


#st.session_state
##run app by using command: stremalit run web.py
## https://ikari2todoweb.streamlit.app/