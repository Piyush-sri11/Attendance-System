from flask import Blueprint, request, render_template, redirect, url_for
from face_recognition import load_image_file, face_encodings, face_locations
from .models import Person
from flask_sqlalchemy import SQLAlchemy
import cv2
import numpy as np
from .models import db

attendance_bp = Blueprint('attendance', __name__)

@attendance_bp.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        mobile = request.form['mobile']
        email = request.form['email']
        image = request.files['image']
        image_path = "static/images/" + image.filename
        image.save(image_path)  # Save image to a folder
        face_image = load_image_file(image_path)
        face_image = cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB)
        face_location = face_locations(face_image)
        face_enc = face_encodings(face_image, face_location)[0]
        new_person = Person(name=name, address=address, mobile=mobile, email=email, image=image.filename, face_encoding=face_enc)
        db.session.add(new_person)
        db.session.commit()
        print("New person added to database:", new_person)  # Debugging statement
        return redirect(url_for('attendance.index1'))

@attendance_bp.route('/stored_data')
def stored_data():
    persons = Person.query.all()
    return render_template('stored_data.html', persons=persons)

@attendance_bp.route('/attendance')
def attendance():
    # Logic to display attendance records
    return render_template('attendance.html')