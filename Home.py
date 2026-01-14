import streamlit as st
from src.genai.llm import summarize_notes,compare_notes
from src.genai.db_configs.db_add import add_note
from src.genai.db_configs.db_connection import MongoDBConnection
from src.genai.db_configs.schemas import Lecture,Course,User

# Initialize mongodb connection
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
    """Fetches all lectures from DB for course course_name. Returns a dictionary whose keys are the course name + lecture number, and values are just the number"""
    try:
        course=Course.objects(name=course_name).first()
        lectures=Lecture.objects(course=course)
        lecture_names={lecture.course.name+": Lecture "+lecture.lecture_number:lecture.lecture_number for lecture in lectures}
        return lecture_names
    except Exception as e:
        st.error(str(e))
        return []

    
# Set up initial state values
if 'user' not in st.session_state:
    st.session_state.user = None
# Hide sidebar if no user is logged in
if st.session_state.user==None:
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"] {display: none}
        </style>
        """,
        unsafe_allow_html=True
    )

if st.session_state.user==None: # if no user is logged in, show a login page
    st.title("Sign In")

    username=st.text_input("Username")
    if st.button("Sign in"):
        user=User.objects(username=username).first()
        if not user:
            st.error("Username not found, do you want to sign up?")
        else:
            st.session_state.user=user.username
            st.rerun()
    if st.button("Sign Up"):
        st.switch_page("pages/sign_up.py")
else: # otherwise, show the actual page
    # Sidebar navigation
    st.sidebar.write(f"Current User: {st.session_state.user}")
    if st.sidebar.button("logout"):
        st.session_state.user=None
        st.rerun()
    st.sidebar.markdown("**Navigation:**")
    st.sidebar.page_link('Home.py', label='Home')
    st.sidebar.page_link('pages/Edit.py', label='Edit')
    st.sidebar.page_link('pages/Comparison.py', label='Comparison')

    st.title("Knowledge Gap Detector")
    st.write("Welcome! This is a knowledge gap identifier. Please choose a lecture and submit your notes.")

    courses=get_course_names()
    # Select Course
    course_name = st.selectbox("Select Course",courses,key="selected_course")
    lectures=get_available_lectures(course_name)
    if len(lectures)==0: # Because courses are created on lecture upload, this only occurs if there are no courses
        st.error("Unfortunately, No courses were found in the database. If you are a lecturer, go to the `Edit` page to add your first lecture. If you are a student, ask your professor if they would join the app. If you think you recieved this message in error, please contact your administrator.")
    else:
        # Select lecture
        lecture_name=st.selectbox("Select which lecture your notes are for", lectures.keys(),key="selected_lecture")
        lecture_num=lectures[lecture_name]
        # Option 1: File Upload
        uploaded_file=st.file_uploader("Upload a Markdown file (.md)", type=["md", "txt"],key="uploaded_file")

        # Option 2: Plain Text
        notes=st.text_area("Or, paste your notes here", key="notes",height=300)

        # Form Submit
        if st.button('Submit my picks',type="primary"): 
            # Prioritize uploaded file content over text area
            if st.session_state.uploaded_file is not None:
                # Read the file and decode it to string
                final_notes = st.session_state.uploaded_file.getvalue().decode("utf-8")
            else:
                final_notes = st.session_state.notes

            summary=''
            if final_notes.strip():
                summary = summarize_notes(final_notes,course_name,lecture_num,st.session_state.user)
            else:
                st.error("Please provide some notes before submitting.")
            if summary:
                comparision = compare_notes(summary, course_name,lecture_num)

                # Display result
                st.markdown(comparision)
