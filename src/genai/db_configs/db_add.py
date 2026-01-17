from genai.db_configs.schemas import User, Lecture, Course, Slide, Note
from mongoengine import NotUniqueError
import os

def add_course(name: str) -> Course | None:
    """ Adds a new course to the database.
    Args:
        name: The name of the course to add.
    """
    try:
        new_course = Course(name=name)
        new_course.save()
        print(f"Course '{name}' created.")
        return new_course
    except NotUniqueError:
        print(f"Course '{name}' already exists.")
        return Course.objects(name=name).first()
    except Exception as e:
        print(f"Error adding course: {e}")
        return None

def add_lecture(course_obj: Course, number: str) -> Lecture | None:
    """ Adds a new lecture to the database and links it to a course.
    Args:
        course_obj: The Course object to which the lecture belongs.
        number: The lecture number.
    """
    try:
        # Create the lecture with the link to the course
        new_lecture = Lecture(
            lecture_number=number,
            course=course_obj # <--- Link established here
        )
        new_lecture.save()
        
        # Optional: Add this lecture to the Course's list of lectures (Double linking)
        course_obj.update(push__lectures=new_lecture)
        
        print(f"Lecture '{number}' added to Course '{course_obj.name}'.")
        return new_lecture
    except Exception as e:
        print(f"Error adding lecture: {e}")
        return None


def add_slide(lecture_obj: Lecture, title: str, file_url: str, summary: str) -> Slide | None:
    """ Adds a new slide to the database and links it to a lecture.
    Args:
        lecture_obj: The lecture object to which the slide belongs.
        title: The title of the slide.
        file_url: The URL of the slide file.
        summary: A brief summary of the slide content.
    """
    try:
        new_slide = Slide(
            title=title, 
            file_url=file_url,
            lecture=lecture_obj # <--- Link established here
        )
        new_slide.save()
        print(f"Slide '{title}' linked to Lecture '{lecture_obj.title}'.")
        return new_slide
    except Exception as e:
        print(f"Error adding slide: {e}")
        return None


def add_user(username: str, email: str, roles: list = None) -> User | None:
    """ Adds a new user to the database.
    Args:
        username: The username of the new user.
        email: The email of the new user.
        roles: A list of roles assigned to the user. Defaults to ['user'].
    """
    if roles is None: roles = ['user']
    try:
        new_user = User(username=username, email=email, roles=roles)
        new_user.save()
        print(f"User '{username}' added.")
        return new_user
    
    # Handle duplicate username error
    except NotUniqueError:
        print(f"User '{username}' already exists.")
        return User.objects(username=username).first()
    
    # Handle other exceptions
    except Exception as e:
        print(f"Error adding user: {e}")
        return None

# --- 5. Add Note (Modified for Markdown Files) ---
def add_note(user_obj, lecture_obj, md_file_path: str = None, content: str = None, summary: str = None):
    """ Adds a new note to the database, linked to a user and lecture.
    Args:
        user_obj: The user object who created the note.
        lecture_obj: The lecture object to which the note belongs.
        md_file_path: The file path of the markdown file containing the note content.
        content: Direct content of the note (if not using a file).
        summary: A brief summary of the note content.
    """
    # If content is passed directly (from Streamlit), use it
    final_content = content

    # Only look for a file path if content wasn't provided directly
    if not final_content and md_file_path:
        if os.path.exists(md_file_path):
            with open(md_file_path, "r", encoding="utf-8") as f:
                final_content = f.read()
    
    if not final_content:
        print("No content provided to save.")
        return None

    # Save the note to the database
    try:
        new_note = Note(
            content=final_content,
            author=user_obj,
            lecture=lecture_obj,
            summary=summary
        )
        new_note.save()
        return new_note
    
    # Handle exceptions
    except Exception as e:
        print(f"Error saving note to DB: {e}")
        return None
