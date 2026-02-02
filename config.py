import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'mysecretkey123'  # Used for sessions and CSRF
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'instance/paper_portal.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # Max upload size = 16 MB
    
    ALLOWED_EXTENSIONS = {'pdf', 'docx', 'txt'}