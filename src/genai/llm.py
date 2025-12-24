import os
from pathlib import Path
from google import genai
from google.genai import types
from src.genai.db_configs.schemas import Course, Lecture, Slide, Note, User
from src.genai.db_configs.db_connection import MongoDBConnection

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
model="gemini-3-pro-preview"


def summarize_pdf(pdf_bytes, course_name, lec_num):
    if not MongoDBConnection.setup():
        return "Database connection failed."

    # 1. Manual Get or Create for Course
    course_obj = Course.objects(name=course_name).first()
    if not course_obj:
        # Save new course to DB if it doesn't exist
        course_obj = Course(name=course_name).save()
        print(f"Created new course: {course_name}")

    # 2. Manual Get or Create for Lecture
    # Since lecture_number is unique_with='course', we check both
    lecture_obj = Lecture.objects(course=course_obj, lecture_number=str(lec_num)).first()
    if not lecture_obj:
        lecture_obj = Lecture(course=course_obj, lecture_number=str(lec_num)).save()
        print(f"Created new lecture: {lec_num}")
    '''
    # 2. Get Course and Lecture references
    course_obj = Course.objects(name=course_name).first()
    if not course_obj:
        return f"Error: Course '{course_name}' not found in database."

    # Find or create the lecture
    lecture_obj = Lecture.objects(course=course_obj, lecture_number=str(lec_num)).first()
    if not lecture_obj:
        lecture_obj = Lecture(course=course_obj, lecture_number=str(lec_num)).save()

    '''
    # 3. LLM Processing
    prompt = """Summarise the attached slides into one sentence per topic. 
    Topic titles in **bold**, no bullet points, no intro/outro."""
    try:
        response = client.models.generate_content(
            model=model,
            contents=[
                types.Part.from_bytes(data=pdf_bytes, mime_type="application/pdf"),
                prompt
            ],
        )
        summary_text = response.text
    except Exception as e:
        return f"LLM Error: {str(e)}"
    # 4. Save to Slide Collection
    # This creates a new Slide document linked to the specific Lecture object
    try:
        Slide(
            title=f"Slides - {course_name} Lecture {lec_num}",
            file_url="local_upload", # Placeholder for the file path
            lecture=lecture_obj,
            summary=summary_text
        ).save()
    except Exception as e:
        return f"Database Save Error: {str(e)}"

    return summary_text

def summarize_notes(notes_text, course_name, lec_num, username):
    """Summarizes markdown notes and saves to the Note collection."""
    if not MongoDBConnection.setup():
        return "Database connection failed."

    # 1. Get references for Lecture and User
    course_obj = Course.objects(name=course_name).first()
    lecture_obj = Lecture.objects(course=course_obj, lecture_number=str(lec_num)).first()
    user_obj = User.objects(username=username).first()

    if not all([lecture_obj, user_obj]):
        return "Error: User or Lecture not found."

    # 2. LLM Processing
    prompt = f"""Summarise the attached lecture notes into one sentence per topic. 
    Topic titles in **bold**, no bullet points.

    Notes: {notes_text}"""

    response = client.models.generate_content(
        model=model,
        contents=[prompt],
    )
    summary_text = response.text

    # 3. Save to Note Collection
    Note(
        content=notes_text,
        author=user_obj,
        lecture=lecture_obj,
        summary=summary_text
    ).save()

    return summary_text
