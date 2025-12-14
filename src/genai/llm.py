from google import genai
from google.genai import types
from pathlib import Path
from typing import Union, List
import os
from dotenv import load_dotenv

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)

def summarize_notes(notes):
    prompt = f"""Summarise the attached lecture notes into one sentence per topic. Please do not include any introductory or concluding remarks. Every topic title should be in bold and do not use bullet points.

Notes: {notes}"""
    response = client.models.generate_content(
        model="gemini-3-pro-preview",
        contents=[
            prompt
        ],
    )
    return response.text

def summarize_pdf(pdf):
    prompt = "Summarise the attached slides into one sentence per topic. \
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
