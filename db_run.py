from genai.db_configs.db_connection import MongoDBConnection
from genai.db_configs.db_add import add_course, add_lecture, add_user, add_note

# 1. Connect
if not MongoDBConnection.setup():
    print("Could not connect to database. Exiting.")
    exit()

student = add_user("johnny_coder", "john@coder.com")


# 2. Retrieve (or Create) the User and Lecture you want to link
course = "GenAI WS25"
lec1 = add_lecture(course, "Intro to LLMs", "1")
student = add_user("jane_doe", "jane@uni.edu")

# 3. Add the Markdown Note
if student and lec1:
    # We pass the filename to 'md_file_path'
    add_note(
        user_obj=student,
        lecture_obj=lec1,
        title="lecture 1 notes",
        md_file_path="data/generative-ai/lecture-6/buraks-notes.md"  # <--- The script will read this file
    )

    
