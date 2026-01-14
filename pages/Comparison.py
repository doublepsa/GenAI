import streamlit as st
from src.genai.llm import summarize_notes,compare_notes,student_notes_comparison
from src.genai.db_configs.db_add import add_note
from src.genai.db_configs.db_connection import MongoDBConnection
from src.genai.db_configs.schemas import Lecture,Course,User

if not MongoDBConnection.setup():
    st.error("Could not connect to database.")
    st.stop()

def get_course_names():
    """Fetches unique course names from DB."""
    try:
        # Use MongoEngine to get distinct values from the 'name' field
        courses = Course.objects.distinct("name")
        return courses
    except Exception as e:
        st.error(f"Error fetching courses: {e}")
        return []
# @st.cache_data(ttl=3600)
def get_available_lectures(course_name):
    """Fetches all lectures from DB"""
    try:
        course=Course.objects(name=course_name).first()
        lectures=Lecture.objects(course=course)
        lecture_names={lecture.course.name+": Lecture "+lecture.lecture_number:lecture.lecture_number for lecture in lectures}
        return lecture_names
    except Exception as e:
        st.error(str(e))
        return []

# Sidebar navigation
st.sidebar.write(f"Current User: {st.session_state.user}")
if st.sidebar.button("logout"):
    st.session_state.user=None
    st.rerun()
st.sidebar.markdown("**Navigation:**")
st.sidebar.page_link('Home.py', label='Home')
st.sidebar.page_link('pages/Edit.py', label='Edit')
st.sidebar.page_link('pages/Comparison.py', label='Comparison')
st.title("Note Comparer")

st.write("Use this page to compare your already submitted notes with other students and the lecture slides")

courses=get_course_names()
# Select Course
course_name = st.selectbox("Select Course",courses,key="selected_course")
lectures=get_available_lectures(course_name)
# Select lecture
lecture_name=st.selectbox("Select which lecture your notes are for", lectures.keys(),key="selected_lecture")
lecture_num=lectures[lecture_name]
# Form Submit
if st.button('Run the LLM',type="primary"): 
    try:
        comparison=student_notes_comparison(course_name,lecture_num,st.session_state.user)
    except Exception as e:
        raise e
    if comparison:
        # Display result
        st.markdown(comparison)
    # if summary:
        # comparision = compare_notes(summary, course_name,lecture_num)
        # Display result
        # st.markdown(comparison)
