import streamlit as st
from genai import db

# Set up initial session state
if 'result' not in st.session_state:
    st.session_state.result=''


def submit_slides():
    # Function run when the lecture_submission form is submitted
    # If the lecture has already been created, overrights the lecture with a new one
    # Otherwise, creates a new lecture
    # TODO: connect to db
    if st.session_state.lecture in db.get_available_lectures():
        #db.modify_lecture(st.session_state.lecture,st.session_state.slides)
        st.session_state.result="editing existing state!"
    else:
        #db.add_lecture(st.session_state.lecture,st.session_state.slides)
        st.session_state.result="creating new lecture!"
    
    

st.subheader("Edit Lectures")
st.write("Use this page to edit/add new lectures to the app")
with st.form("lecture_submission"):
    # Form for submitting new lectures and updating old ones
    # Should only be able to be accessed by priviliged users
    st.selectbox("Select an existing Lecture or create a new one", db.get_available_lectures(), key="lecture",accept_new_options=True)
    st.file_uploader("(Re)Upload this lecture's slides",key="slides")
    st.form_submit_button("Submit Slides",on_click=submit_slides)

st.write(st.session_state.result)
