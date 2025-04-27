import streamlit as st

def check_password():
    if "password_correct" not in st.session_state:
        # Ask for password
        password = st.text_input("Enter the access password:", type="password")
        if password == st.secrets["password"]:
            st.session_state["password_correct"] = True
            return True
        else:
            st.error("Incorrect password")
            return False
    elif not st.session_state["password_correct"]:
        st.error("Incorrect password")
        return False
    else:
        return True

