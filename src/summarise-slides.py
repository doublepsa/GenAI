from google import genai
from google.genai import types
from pathlib import Path
from typing import Union, List
import os
from dotenv import load_dotenv

# Load the variables from .env
load_dotenv()

# accessing the Gemini API key
API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)

def summarise_slides(base_data_path: str, lecture_number: Union[int, List[int]]) -> List[tuple]:
    """
    Uses Gemini to summarise a group of slide decks of a course.

    Args:
        base_data_path: The root directory for the data (e.g., 'data/').
        lecture_number: The specific lecture folder to analyze (e.g., 1 for 'lecture-1').
    """

    if isinstance(lecture_number, int):
        # Convert the single integer into a list containing that integer
        lecture_number = [lecture_number]
    
    responses = []

    for lec_num in lecture_number:
        lecture_folder = Path(base_data_path) / f'lecture-{lec_num}'
        print(f"--- Analyzing Notes in: {lecture_folder} ---")

        responses_lec_num = []
        lecture_slides = list(lecture_folder.glob('*.pdf'))
        prompt = "Summarise the attached slides into one sentence per topic. \
            Please do not include any introductory or concluding remarks. \
            Every topic title should be in bold and do not use bullet points."
        
        # Summarize each slide deck in the lecture folder
        for file_path in lecture_slides:
            response = client.models.generate_content(
                model="gemini-3-pro-preview",
                contents=[
                types.Part.from_bytes(
                    data=file_path.read_bytes(),
                    mime_type="application/pdf",
                    ),prompt
                ],
            )
            responses_lec_num.append(response.text)
        
        # merge all per-file responses into one string with a blank line between items
        merged = "\n\n".join(responses_lec_num)

        # save merged summary to a text file
        if merged:
            summary_file = lecture_folder / "summary_slides.txt"
            summary_file.write_text(merged, encoding="utf-8")
        else:
            print(f"No summaries for lecture-{lec_num}; skipped writing summary_slides.txt")
        responses.append((lec_num, merged))
    return responses

# Example usage
if __name__ == "__main__":
    base_data_path = 'data/generative-ai'
    lecture_number = list(range(1, 7))  # Lectures 1 to 6
    summaries = summarise_slides(base_data_path, lecture_number)
    for lec_num, summary in summaries:
        print(f"Lecture {lec_num} Summaries:")
        print(summary)
        print("-----")
