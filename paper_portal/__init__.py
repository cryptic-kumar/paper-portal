import os
from flask import Flask
from .extensions import db, login_manager
from .auth.routes import auth_bp
from .publisher.routes import publisher_bp
from .recommender.routes import recommender_bp
from .admin.routes import admin_bp

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key'   # change this
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///paper_portal.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # File upload folder
    app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'uploads')

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(publisher_bp, url_prefix='/publisher')
    app.register_blueprint(recommender_bp, url_prefix='/recommender')
    app.register_blueprint(admin_bp, url_prefix='/admin')

    return app
