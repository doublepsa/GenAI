from genai.db_configs.db_add import add_lecture, add_note, add_user
from src.genai.db_configs.db_connection import MongoDBConnection
from src.genai.db_configs.schemas import User,Course,Lecture,Slide,Note
from src.genai.llm import summarize_pdf,summarize_notes
from mongoengine.connection import _get_db

# 1. Connect
if not MongoDBConnection.setup():
    print("Could not connect to database. Exiting.")
    exit()

User.objects.delete()
Course.objects.delete()
Lecture.objects.delete()
Slide.objects.delete()
Note.objects.delete()

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
User(username="test1",email="test1").save()
User(username="test2",email="test2").save()
User(username="test3",email="test3").save()

genai=Course(name="Genai")
genai.save()
lec1=Lecture(lecture_number='1',course=genai)
lec1.save()

with open("data/generative-ai/lecture-1/slides.pdf","rb") as f:
    pdf_bytes=f.read()

summarize_pdf(pdf_bytes,"Genai",'1')

with open("data/generative-ai/lecture-1/student1.md","r") as f:
    notes_text=f.read()
summarize_notes(notes_text,"Genai","1","test1")
with open("data/generative-ai/lecture-1/student2.md","r") as f:
    notes_text=f.read()
summarize_notes(notes_text,"Genai","1","test2")
with open("data/generative-ai/lecture-1/student3.md","r") as f:
    notes_text=f.read()
summarize_notes(notes_text,"Genai","1","test3")
