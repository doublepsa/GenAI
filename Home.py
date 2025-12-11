# app.py

import streamlit as st
from db import get_available_lectures
from llm import call_llm_api

if 'result' not in st.session_state:
    st.session_state.result=''


def submit_notes():
    # TODO: Start llm process. 'result' should give information on the process 
    st.session_state.result="form successfully submitted!"

st.title("Knowledge Gap Detector")

st.write("Welcome! This is a knowledge gap identifier. Please chose a lecture below, and submit your notes.")

with st.form("note_submission"):
    # st.markdown("##### Select which lecture your notes are for")
    st.selectbox("Select which lecture your notes are for", get_available_lectures(), key="lecture")
    st.text_area("Insert your notes",key="notes",height="content")
    st.form_submit_button('Submit my picks',on_click=submit_notes)

st.write(st.session_state.result)
###############################################
# elif page == "LLM Demo":                    #
#     st.subheader("LLM Demo (Placeholder)")  #
#                                             #
#     prompt = st.text_area("Enter a prompt") #
#                                             #
#     if st.button("Call LLM"):               #
#         try:                                #
#             response = call_llm_api(prompt) #
#             st.write(response)              #
#         except NotImplementedError as e:    #
#             st.error(str(e))                #
###############################################

