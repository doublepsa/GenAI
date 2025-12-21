from google import genai
from google.genai import types
from pathlib import Path
from typing import Union, List
import os
from dotenv import load_dotenv

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)

def summarize_notes(notes):
    prompt = f"""Summarize the attached lecture notes into one sentence per topic. Please do not include any introductory or concluding remarks. Every topic title should be in bold and do not use bullet points.

Notes: {notes}"""
    response = client.models.generate_content(
        model="gemini-3-pro-preview",
        contents=[
            prompt
        ],
    )
    return response.text

def summarize_pdf(pdf):
    prompt = "Summarize the attached slides into one sentence per topic. \
Please do not include any introductory or concluding remarks. \
Every topic title should be in bold and do not use bullet points."
    response = client.models.generate_content(
        model="gemini-3-pro-preview",
        contents=[
            types.Part.from_bytes(
                data=pdf,
                mime_type="application/pdf",
            ),prompt
        ],
    )
    return response.text

def compare_notes(lecture,notes):
    prompt=f"""# ROLE:
You are an expert study assistant.

# INPUT FORMAT:
you will be given two texts, written in markdown.

The first text is a summary of a lecture condensed so that each new idea that is important for studying consists of a single sentence.

The second text is set of student-written notes taken from the lecture.

# TASK:
Your task is to compare the lecture summary with the student notes. 

Identify every contradiction between the two texts. Each instance of contradiction indicates a piece of information the student took incorrectly. List all such errors.

Identify every topic in the lecture that is missing in the student notes. Each instance of missing information is a knowledge gap in the student notes. List all such gaps in the student's work.

# IMPORTANT CONSIDERATIONS:
1. The lecture summary is ALWAYS completely correct and complete. Every error is located in the student notes
2. Contradictions only occur when semantic information differs between the two texts. The student is allowed to rename variables, paraphrase, and otherwise change the text without causing contradiction.
3. Likewise, knowledge gaps only occur when semantic information is missing. The student is allowed to abbreviate topics as long as understanding of the topic is shown.

# OUTPUT FORMAT:
You will output a region of markdown text consisting of two top-level headers "ERRORS" and "GAPS". As numbered lists, add your list of identified contradictions under ERRORS and your list of knowledge gaps under GAPS. The student is the user, so refer to them in the second person.

After your response the user may ask follow up questions about your output. Respond to these questions as normal for a study assistant chatbot.

# LECTURE SUMMARY:
{lecture}

# STUDENT NOTES:
{notes}

# RESPONSE:
"""
    response = client.models.generate_content(
        model="gemini-3-pro-preview",
        contents=[
            prompt
        ],
    )
    return response.text
