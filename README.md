# GenAI
Project of the lecture 194.207 Generative AI (VU 4,0) 2025W

# Installation
After downloading the sourcecode with `git clone`

Enter the created directory with `cd Genai`

To download dependencies, run

```
uv build
uv run pip install .
```

# Running the Project
To start up the server locally, run `uv run streamlit run Home.py`

# Gemini API Key

In order to run the project, one needs a Gemini API Key. It is possible to get it for free.

1. Sign In to Google AI Studio
    - Navigate to the Google AI Studio API Keys page. <https://aistudio.google.com/app/apikey>
    - Sign in with your Google Account.

2. Create Your API Key
    - Once you are on the API Keys page, look for and click the "Create API Key" button.
    - A dialog will appear. Create a new project to associate with your key.

3. Generate and Copy the Key
    - Then the system will instantly generate your new API key.
    - The key is a long string of alphanumeric characters. Copy it immediately using the copy icon next to the key.

4. Create a file .env in the root folder of the project.
    - Include `GEMINI_API_KEY = <YOUR_KEY>`