import streamlit as st
from src.genai.llm import summarize_notes,compare_notes,student_notes_comparison
from src.genai.db_configs.db_add import add_note
from src.genai.db_configs.db_connection import MongoDBConnection
from src.genai.db_configs.schemas import Lecture,Course,User,Note

# Ensure mongodb connection is activated
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
    
def get_available_lectures(course_name):
    """Fetches all lectures from DB for course course_name. Returns a dictionary whose keys are the course name + lecture number, and values are just the number"""
    try:
        course=Course.objects(name=course_name).first()
        lectures=Lecture.objects(course=course)
        lecture_names={lecture.course.name+": Lecture "+lecture.lecture_number:lecture.lecture_number for lecture in lectures}
        return lecture_names
    except Exception as e:
        st.error(str(e))
        return []

# Switch to main page if no user is logged in
if "user" not in st.session_state or st.session_state.user==None:
    st.switch_page("Home.py")

# Sidebar navigation
st.sidebar.write(f"Current User: {st.session_state.user}")
if st.sidebar.button("logout"):
    st.session_state.user=None
    st.switch_page("Home.py")
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
        # compares the user's notes with the lecture summary
        user=User.objects(username=st.session_state.user).first()
        student_note=Note.objects(author=user).first().content
        note_comparison = compare_notes(student_note, course_name,lecture_num)
    except Exception as e:
        st.error(e)
    if note_comparison:
        # Display result
        st.markdown("# Comparison against the lecture")
        st.markdown(note_comparison)
    try:
        # compares the user's notes with every other student note
        student_comparison=student_notes_comparison(course_name,lecture_num,st.session_state.user)
    except Exception as e:
        st.error(e)
    if student_comparison:
        # Display result
        st.markdown("# Comparison against other students")
        st.markdown(student_comparison)
