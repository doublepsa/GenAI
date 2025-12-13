from mongoengine import Document, StringField, ListField, ReferenceField, DateTimeField
from datetime import datetime
from db_configs.db_connection import MongoDBConnection

class User(Document):
    username = StringField(required=True, unique=True)
    email = StringField(required=True, unique=True)
    roles = ListField(StringField(), default=['user'])
# ----------------------
# Course Schema
# ----------------------
class Course(Document):
    name = StringField(required=True, unique=True)
    description = StringField()
    lectures = ListField(ReferenceField('Lecture'))  # connection to lectures


# ----------------------
# Lecture Schema
# ----------------------
class Lecture(Document):
    lecture_number = StringField(required=True, unique_with='course')
    content = StringField()
    # LINK 1: The Lecture now explicitly belongs to a Course
    course = ReferenceField(Course, required=True)

class Slide(Document):
    title = StringField(required=True)
    file_url = StringField(required=True)
    # LINK 2: The Slide now belongs to a specific Lecture
    lecture = ReferenceField(Lecture, required=True)

# ----------------------
# Note Schema
# ----------------------
class Note(Document):
    title = StringField(required=True)
    content = StringField()
    file_url = StringField()
    # LINK 3: The Note belongs to a User AND a Lecture
    author = ReferenceField(User, required=True)
    lecture = ReferenceField(Lecture, required=True)