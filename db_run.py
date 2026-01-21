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

with open("data/generative-ai/lecture-1/student1.md","r", encoding="utf-8") as f:
    notes_text=f.read()
summarize_notes(notes_text,"Genai","1","test1")
with open("data/generative-ai/lecture-1/student2.md","r", encoding="utf-8") as f:
    notes_text=f.read()
summarize_notes(notes_text,"Genai","1","test2")
with open("data/generative-ai/lecture-1/student3.md","r", encoding="utf-8") as f:
    notes_text=f.read()
summarize_notes(notes_text,"Genai","1","test3")
