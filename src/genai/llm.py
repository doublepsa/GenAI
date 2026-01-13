import os
from pathlib import Path
from google import genai
from google.genai import types
from src.genai.db_configs.schemas import Course, Lecture, Slide, Note, User
from src.genai.db_configs.db_connection import MongoDBConnection
import warnings

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
    #Old Promt
    #prompt = """Summarise the attached slides into one sentence per topic. 
    #Topic titles in **bold**, no bullet points, no intro/outro."""
    # 3. LLM Processing
    prompt = """
    # ROLE
    You are a document analysis assistant whose task is to faithfully extract and reorganize information from university lecture slides.

    # SOURCE OF TRUTH
    The attached PDF lecture slides are the ONLY source of information.
    Do NOT add, infer, generalize, or assume anything beyond what is explicitly stated on the slides.

    # TASK
    Create a detailed, structured study summary of the lecture slides.

    You must:
    1. Preserve the logical structure of the slides, including sections and subtopics.
    2. Extract all important examinable information, including:
    - Definitions
    - Key concepts
    - Relationships between concepts
    - Algorithms or step-by-step procedures
    - Mathematical expressions or formulas (rewrite exactly as shown, using LaTeX if needed)
    - Assumptions, constraints, and conditions
    3. Rephrase the slide content only to improve clarity and readability, without changing meaning.
    4. Include information conveyed by figures, diagrams, tables, or graphs **only if the slide explicitly explains them** (e.g., captions or accompanying text).

    # STRICT RULES (NO HALLUCINATION)
    - Do NOT introduce examples, explanations, or background knowledge not present in the slides.
    - Do NOT merge topics unless they are presented together on the same slide or under the same slide heading.
    - If information is ambiguous or incomplete on the slide, preserve it as-is without completing it.

    # OUTPUT FORMAT
    - Use **bold** section headers that correspond to slide titles or major headings.
    - Under each header, write multiple complete sentences that cover all bullet points from the slides.
    - Do NOT use bullet points or numbered lists.
    - Do NOT add introductions, conclusions, or commentary.

    # QUALITY TARGET
    The summary should be detailed enough that a student who studied only this output would not lose any examinable information compared to the original slides.

    # LECTURE SLIDES:
    (See attached PDF)

    # RESPONSE:
    """

    
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

def compare_notes(summary,course_name,lecture_num):
    if not MongoDBConnection.setup():
        return "Database connection failed."
    course_obj = Course.objects(name=course_name).first()
    lecture_obj = Lecture.objects(course=course_obj, lecture_number=str(lecture_num)).first()
    slide_obj = Slide.objects(lecture=lecture_obj).first()
    
    prompt=f"""# ROLE:
You are an expert study assistant.

# INPUT FORMAT:
you will be given two texts, written in markdown.

The first text is a summary of a lecture condensed so that each new idea that is important for studying consists of a single sentence.

The second text is a set of student-written notes taken from the lecture.

# TASK:
Your task is to compare the lecture summary with the student notes. 

Identify every contradiction between the two texts. Each instance of contradiction indicates a piece of information the student took incorrectly. List all such errors.

Identify every topic in the lecture that is missing in the student notes. Each instance of missing information is a knowledge gap in the student notes. List all such gaps in the student's work.

# IMPORTANT CONSIDERATIONS:
1. The lecture summary is ALWAYS completely correct. Every error is located in the student notes
2. Contradictions only occur when semantic information differs between the two texts. The student is allowed to rename variables, paraphrase, and otherwise change the text without causing contradiction.
3. Likewise, knowledge gaps only occur when semantic information is missing. The student is allowed to abbreviate topics as long as understanding of the topic is shown.
4. although the lecture summary is always correct, it is not necessarily complete. If the student notes contain something not in the lecture summary, as long as it is not contradictory, do not put it in the errors. 

# OUTPUT FORMAT:
You will output a region of markdown text consisting of two top-level headers "ERRORS" and "GAPS". As numbered lists, add your list of identified contradictions under ERRORS and your list of knowledge gaps under GAPS. The student is the user, so refer to them in the second person.

After your response the user may ask follow up questions about your output. Respond to these questions as normal for a study assistant chatbot.

# LECTURE SUMMARY:
{slide_obj.summary}

# STUDENT NOTES:
{summary}

# RESPONSE:
"""
    response = client.models.generate_content(
        model="gemini-3-pro-preview",
        contents=[
            prompt
        ],
    )
    return response.text