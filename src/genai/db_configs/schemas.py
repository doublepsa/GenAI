from mongoengine import Document, StringField, ListField, ReferenceField, DateTimeField
from datetime import datetime
from genai.db_configs.db_connection import MongoDBConnection

# ----------------------
# User Schema
# ----------------------
class User(Document):
    meta = {'collection': 'user'} # Explicitly match your DB collection name
    username = StringField(required=True, unique=True)
    email = StringField(required=True, unique=True)
    roles = ListField(StringField(), default=['user'])
# ----------------------
# Course Schema
# ----------------------
class Course(Document):
    meta = {'collection': 'course'}
    name = StringField(required=True, unique=True)
    #lectures = ListField(ReferenceField('Lecture'))  # connection to lectures

# ----------------------
# Lecture Schema
# ----------------------
class Lecture(Document):
    meta = {'collection': 'lecture'}
    lecture_number = StringField(required=True, unique_with='course')
    # LINK 1: The Lecture now explicitly belongs to a Course
    course = ReferenceField(Course, required=True)

# ----------------------
# Slide Schema
# ----------------------
class Slide(Document):
    meta = {'collection': 'slide'}
    title = StringField(required=True)
    file_url = StringField(required=True)
    # LINK 2: The Slide now belongs to a specific Lecture
    lecture = ReferenceField(Lecture, required=True, unique=True)
    summary=StringField()

# ----------------------
# Note Schema
# ----------------------
class Note(Document):
    meta = {'collection': 'note'}
    content = StringField()
    file_url = StringField()
    # LINK 3: The Note belongs to a User AND a Lecture
    author = ReferenceField(User, required=True)
    lecture = ReferenceField(Lecture, required=True,unique_with='author')
    summary = StringField()
