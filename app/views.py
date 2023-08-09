from flask import Blueprint, request, jsonify
from app.models import db, Student

api_bp = Blueprint('api', __name__)


@api_bp.route('/students', methods=['GET', 'POST'])
def students_endpoint():
    if request.method == 'GET':
        # Retrieve all student records from the database
        students = Student.query.all()

        # Prepare student data for JSON serialization
        students_data = [
            {
                'id': student.id,
                'name': student.name,
                'age': student.age,
                'location': student.location
            }
            for student in students
        ]
        # Return the student data as JSON response
        return jsonify(students_data), 200

    elif request.method == 'POST':
        # Extract JSON data from the request
        data = request.json
        # Create a new Student instance with provided data
        student = Student(name=data['name'], age=data['age'], location=data['location'])
        # Add the student to the session and commit changes to the database
        db.session.add(student)
        db.session.commit()
        # Prepare the newly added student data for JSON serialization
        student_data = {
            'id': student.id,
            'name': student.name,
            'age': student.age,
            'location': student.location
        }
        # Return the newly added student data as JSON response with 201 status code
        return jsonify(student_data), 201


@api_bp.route('/students/<int:student_id>/', methods=['GET', 'PUT', 'DELETE'])
def student_detail(student_id):
    student = Student.query.get_or_404(student_id)

    if request.method == 'GET':
        # Prepare student data for JSON serialization
        student_data = {
            'id': student.id,
            'name': student.name,
            'age': student.age,
            'location': student.location
        }
        return jsonify(student_data)

    elif request.method == 'PUT':
        # Extract JSON data from the request
        data = request.json

        # Update student attributes with provided data
        student.name = data['name']
        student.age = data['age']
        student.location = data['location']

        # Commit changes to the database
        db.session.commit()

        # Prepare updated student data for JSON serialization
        updated_student_data = {
            'id': student.id,
            'name': student.name,
            'age': student.age,
            'location': student.location
        }
        return jsonify(updated_student_data)

    elif request.method == 'DELETE':
        # Delete the student from the database
        db.session.delete(student)
        db.session.commit()

        return '', 204  # No content, indicating successful deletion
