import unittest
import json
from app import create_app, db
from app.models import Student


class TestStudentAPI(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_get_student(self):
        with self.app.app_context():
            student = Student(name='John', age=20, location='New York')
            db.session.add(student)
            db.session.commit()

            response = self.client.get('/api/students/1/')
            self.assertEqual(response.status_code, 200)
            data = json.loads(response.data)
            self.assertEqual(data['name'], 'John')
            self.assertEqual(data['age'], 20)
            self.assertEqual(data['location'], 'New York')

    def test_update_student(self):
        with self.app.app_context():
            student = Student(name='John', age=20, location='New York')
            db.session.add(student)
            db.session.commit()

            new_data = {'name': 'Updated Name', 'age': 25, 'location': 'Updated Location'}
            response = self.client.put('/api/students/1/', data=json.dumps(new_data), content_type='application/json')
            self.assertEqual(response.status_code, 200)

            updated_student = Student.query.get(1)
            self.assertEqual(updated_student.name, 'Updated Name')
            self.assertEqual(updated_student.age, 25)
            self.assertEqual(updated_student.location, 'Updated Location')

    def test_delete_student(self):
        with self.app.app_context():
            student = Student(name='John', age=20, location='New York')
            db.session.add(student)
            db.session.commit()

            response = self.client.delete('/api/students/1/')
            self.assertEqual(response.status_code, 204)
            self.assertIsNone(Student.query.get(1))


if __name__ == '__main__':
    unittest.main()
