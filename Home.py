import streamlit as st
from genai.db import get_available_lectures
from genai.llm import summarize_notes

# Set up session state to initial values
if 'result' not in st.session_state:
    st.session_state.result=''


def submit_notes():
    # Run when the note_submission form is submitted
    summary=summarize_notes(st.session_state.notes)
    # TODO: send summary to db
    st.session_state.result=summary

st.title("Knowledge Gap Detector")

st.write("Welcome! This is a knowledge gap identifier. Please chose a lecture below, and submit your notes.")

with st.form("note_submission"):
    # Form for submitting student notes to the app
    st.selectbox("Select which lecture your notes are for", get_available_lectures(), key="lecture")
    st.text_area("Insert your notes",key="notes",height="content")
    st.form_submit_button('Submit my picks',on_click=submit_notes)

st.write(st.session_state.result)
