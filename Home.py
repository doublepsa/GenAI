import streamlit as st
from genai.db import get_available_lectures
from genai.llm import summarize_notes
from genai.db_configs.db_add import add_note
# Set up session state to initial values

if 'result' not in st.session_state:
    st.session_state.result = ''

def submit_notes():
    # Prioritize uploaded file content over text area
    if st.session_state.uploaded_file is not None:
        # Read the file and decode it to string
        final_notes = st.session_state.uploaded_file.getvalue().decode("utf-8")
    else:
        final_notes = st.session_state.notes

    if final_notes.strip():
        summary = summarize_notes(final_notes)
        st.session_state.result = summary
        # TODO: send summary to db
        # add_note(user="User1", lecture=st.session_state.lecture, summary=summary, content=final_notes)
    else:
        st.error("Please provide some notes before submitting.")

st.title("Knowledge Gap Detector")

st.write("Welcome! This is a knowledge gap identifier. Please choose a lecture and submit your notes.")

with st.form("note_submission"):
    # Select lecture
    st.selectbox("Select which lecture your notes are for", get_available_lectures(), key="lecture")
    
    # Option 1: File Upload
    st.file_uploader("Upload a Markdown file (.md)", type=["md", "txt"], key="uploaded_file")
    
    # Option 2: Plain Text
    st.text_area("Or, paste your notes here", key="notes", height=300)
    
    # Form Submit
    st.form_submit_button('Submit my picks', on_click=submit_notes)

# Display result
if st.session_state.result:
    st.subheader("Summary")
    st.markdown(st.session_state.result)