import streamlit as st

st.title("Streamlit Calculator")


# Initialize session state
if "expression" not in st.session_state:
    st.session_state.expression = ""

# Function to update display
def add(value):
    st.session_state.expression += value

# Function to clear
def clear():
    st.session_state.expression = ""

# Function to calculate
def calculate():
    try:
        st.session_state.expression = str(eval(st.session_state.expression))
    except:
        st.session_state.expression = "Error"

# Display
st.text_input("Display", st.session_state.expression, disabled=True)

# Calculator buttons
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.button("7", on_click=add, args=("7",))
    st.button("4", on_click=add, args=("4",))
    st.button("1", on_click=add, args=("1",))
    st.button("0", on_click=add, args=("0",))

with col2:
    st.button("8", on_click=add, args=("8",))
    st.button("5", on_click=add, args=("5",))
    st.button("2", on_click=add, args=("2",))
    st.button(".", on_click=add, args=(".",))

with col3:
    st.button("9", on_click=add, args=("9",))
    st.button("6", on_click=add, args=("6",))
    st.button("3", on_click=add, args=("3",))
    st.button("=", on_click=calculate)

with col4:
    st.button("/", on_click=add, args=("/",))
    st.button("*", on_click=add, args=("*",))
    st.button("-", on_click=add, args=("-",))
    st.button("+", on_click=add, args=("+",))

st.button("C Clear", on_click=clear)