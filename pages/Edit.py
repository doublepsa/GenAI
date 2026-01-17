import streamlit as st
from src.genai.db_configs.db_connection import MongoDBConnection
from src.genai.db_configs.schemas import Course
from src.genai.llm import summarize_pdf

@st.cache_data(ttl=3600)
def get_course_names():
    """Initializes connection and fetches unique course names from DB."""
    # Use your class method to connect
    if not MongoDBConnection.setup():
        st.error("Could not connect to database.")
        return []

    try:
        # Use MongoEngine to get distinct values from the 'name' field
        courses = Course.objects.distinct('name')
        return sorted(courses)
    except Exception as e:
        st.error(f"Error fetching courses: {e}")
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
st.set_page_config(page_title="Edit Lecture", layout="centered")

st.title("📚 Lecture Summarizer")

# 2. Populate Dropdown
course_options = get_course_names()

ui_options = course_options + ["+ Add New Course..."]

col1, col2 = st.columns([3, 1])

with col1:
    selected_course = st.selectbox("Select Course", options=ui_options)
    
    # If user picks the add course option, show a text box for choosing the name
    if selected_course == "+ Add New Course...":
        course_name = st.text_input("Enter New Course Name", placeholder="e.g., AI Ethics 101")
    else:
        course_name = selected_course
    # Placeholder for the summary
    summary_placeholder = st.empty()

with col2:
    lecture_num = st.number_input("Lecture #", min_value=1, step=1)

    # 3. File Upload
    uploaded_pdf = st.file_uploader("Upload Lecture Slides (PDF)", type=["pdf"])

    if st.button("🚀 Process & Summarize", type="primary", use_container_width=True):
        if uploaded_pdf:
            with st.spinner(f"Analyzing {selected_course} Lec {lecture_num}..."):
                try:
                    pdf_bytes = uploaded_pdf.read()
                    
                    # Call llm.py function
                    summary = summarize_pdf(pdf_bytes, course_name, lecture_num)
                    get_course_names.clear()
                    # Update the placeholder in col1
                    summary_placeholder.subheader("Final Summary")
                    summary_placeholder.markdown(summary)
                    st.success("Summary generated and saved to database!")
                    
                except Exception as e:
                    st.error(f"An error occurred during processing: {e}")
        else:
            st.warning("Please upload a PDF file first.")
