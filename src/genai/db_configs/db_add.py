from genai.db_configs.schemas import User, Lecture, Course, Slide, Note
from mongoengine import NotUniqueError
import os

def add_course(name: str) -> Course | None:
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

def add_lecture(course_obj: Course, number: str, content: str = None) -> Lecture | None:
    try:
        # Create the lecture with the link to the course
        new_lecture = Lecture(
            lecture_number=number,
            content=content,
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


def add_slide(lecture_obj: Lecture, title: str, file_url: str) -> Slide | None:
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
    if roles is None: roles = ['user']
    try:
        new_user = User(username=username, email=email, roles=roles)
        new_user.save()
        print(f"User '{username}' added.")
        return new_user
    except NotUniqueError:
        print(f"User '{username}' already exists.")
        return User.objects(username=username).first()
    except Exception as e:
        print(f"Error adding user: {e}")
        return None

# --- 5. Add Note (Modified for Markdown Files) ---
def add_note(user_obj: User, lecture_obj: Lecture, title: str, md_file_path: str = None, content: str = None) -> Note | None:
    """
    Creates a Note document. 
    Accepts EITHER raw string 'content' OR a 'md_file_path' to a local .md file.
    """
    final_content = content

    # Logic: If a file path is provided, read the markdown file
    if md_file_path:
        if os.path.exists(md_file_path):
            try:
                with open(md_file_path, "r", encoding="utf-8") as f:
                    final_content = f.read()
                print(f"Read markdown content from: {md_file_path}")
            except Exception as e:
                print(f"Error reading file: {e}")
                return None
        else:
            print(f"Error: File not found at {md_file_path}")
            return None

    try:
        new_note = Note(
            title=title,
            content=final_content, # Store final 
            author=user_obj,
            lecture=lecture_obj
        )
        new_note.save()
        print(f"Note '{title}' added successfully.")
        return new_note
    except Exception as e:
        print(f"Error saving note to DB: {e}")
        return None
