from flask import Flask
from .models import db
from .views import api_bp
from .models import Student


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
    db.init_app(app)
    app.register_blueprint(api_bp, url_prefix='/api')
    with app.app_context():
        db.create_all()  # Create tables based on the model
    return app
