from flask_sqlalchemy import SQLAlchemy
from enum import Enum

db = SQLAlchemy()

class AttendanceStatus(Enum):
    PRESENT = "Present"
    ABSENT = "Absent"

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    mobile = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    face_encoding = db.Column(db.PickleType, nullable=False)

class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    status = db.Column(
        db.Enum(AttendanceStatus, name="attendance_status"),
        nullable=False
    )  # Only 'Present' or 'Absent' allowed
    
    person = db.relationship('Person', backref=db.backref('attendances', lazy=True))