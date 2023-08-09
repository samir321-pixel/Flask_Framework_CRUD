# Flask Project README

This repository contains a Flask project that implements a CRUD API for managing student information. The API allows you to create, retrieve, update, and delete student records using the Flask framework.


- `README.md`: This file you're currently reading.
- `requirements.txt`: A list of Python packages required for the project.
- `run.py`: The entry point of the project, used to run the Flask application.
- `app/`: The main application package.
- `app/models.py`: Contains the SQLAlchemy models for the database.
- `app/views.py`: Contains the API views and routes.
- `test_app.py`: Contains the test cases for the Flask application.

## Getting Started

To set up and run the project locally, follow these steps:

1. Clone the repository to your local machine:

```
git clone <repository-url>
```

2. Navigate to the project directory:

```
cd project-root/
```

3. Install the required packages using pip:

```
pip install -r requirements.txt
```

4. Run the Flask application using the `run.py` script:

```
python run.py
```

The application will run on `http://127.0.0.1:5000/` by default.

## Testing

The project includes unit tests for the Flask application. The test cases are located in the `tests/test_app.py` file. To run the tests, execute the following command:

```
python -m unittest discover -s tests/
```

## Postman Collection

For testing the API endpoints, you can import the provided Postman collection:

[Postman Collection](https://api.postman.com/collections/12086421-721dbedc-c794-4c3d-b463-264e06354e62?access_key=PMAT-01H7CGYHTV70KS3EC92K45E3TQ)

This collection includes pre-configured requests for interacting with the API endpoints.

## Conclusion

This Flask project serves as a basic example of creating a RESTful API using Flask and SQLAlchemy. Feel free to modify and extend it according to your requirements.

For any questions or issues, please contact [your-email@example.com](mailto:your-email@example.com).