import warnings
from google import genai
from google.genai import types
from pathlib import Path
from typing import Union, List
import os
from dotenv import load_dotenv
import warnings

# Load the variables from .env
load_dotenv()

# accessing the Gemini API key
API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)

def student_notes_comparison(base_data_path: str, lecture_number: int, student_notes: str) -> str:
    """
    Uses Gemini to compare a specific student notes file with all the others for the same lecture.

    Args:
        base_data_path: The root directory for the data (e.g., 'data/').
        lecture_number: The specific lecture number to analyze (e.g., 1 for 'lecture-1').
        student_notes: The specific student notes to compare (e.g., 'tylers-notes.md').
    """

    lecture_folder = Path(base_data_path) / f'lecture-{lecture_number}'

    print(f"--- Comparing Student Notes in: {lecture_folder} ---")
    lecture_notes = list(lecture_folder.glob('*.md'))
    lecture_notes_names = [path.name for path in lecture_notes]

    if len(lecture_notes) <= 1:
        warnings.warn(f"Not enough student notes for lecture-{lecture_number} to perform comparison.", UserWarning)
        return ""
    if student_notes not in lecture_notes_names:
        warnings.warn(f"Specified student notes file {student_notes} not found in lecture-{lecture_number}.", UserWarning)
        return ""
    
    uploaded_files = []
    # Upload files one by one
    for path in lecture_notes:
        print(f"Uploading {path}...")
        file_ref = client.files.upload(file=path)
        uploaded_files.append(file_ref)
    prompt = f"Compare the file {student_notes} with all the other attachments. \
            They are student notes. \
            Highlight any significant differences in content coverage, depth of explanation, and clarity. \
            Suggest what could be improved in {student_notes} based on the other notes."
    response = client.models.generate_content(
        model="gemini-3-pro-preview",
        contents=[
        prompt, *uploaded_files
        ],
    )

    # save student notes comparison to a text file
    comparison_file = lecture_folder / f"students_comparison_{student_notes}.txt"
    comparison_file.write_text(response.text, encoding="utf-8")
    return response.text

if __name__ == "__main__":
    base_data_path = 'data/generative-ai'
    
    student_notes_comparison = student_notes_comparison(base_data_path, 6, 'tylers-notes.md')
    print(student_notes_comparison)