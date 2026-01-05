import streamlit as st
from src.genai.db_configs.schemas import User

st.title("Sign Up")
username=st.text_input("Create a Username")
email=st.text_input("Add your email address")
if st.button("Create User"):
    try: User(username=username,email=email).save()
    except:
        st.error("Username or Email not unique, try again")
    st.session_state.user=username
    st.switch_page("Home.py")
