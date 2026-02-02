from .extensions import db
from flask_login import UserMixin
from datetime import datetime

# -------------------
# User Model
# -------------------
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='Publisher')  # Publisher, Recommender, Admin
    
    papers = db.relationship('Paper', backref='author', lazy=True)  # relationship to Paper

    def __repr__(self):
        return f"<User {self.username} | Role: {self.role}>"

# -------------------
# Paper Model
# -------------------
class Paper(db.Model):
    __tablename__ = 'papers'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    abstract = db.Column(db.Text, nullable=False)
    filename = db.Column(db.String(200), nullable=False)  # uploaded file name
    status = db.Column(db.String(20), nullable=False, default='Submitted')  # Submitted, Accepted, Rejected
    feedback = db.Column(db.Text, nullable=True)
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # publisher who submitted

    def __repr__(self):
        return f"<Paper {self.title} | Status: {self.status}>"


# paper_portal/models.py ke end mein add karein

class RoleRequest(db.Model):
    __tablename__ = 'role_requests'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    proof_text = db.Column(db.Text, nullable=False)  # User ka proof/bio
    status = db.Column(db.String(20), default='Pending')  # Pending, Approved, Rejected
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationship taaki hum request se user ka naam nikal sakein
    user = db.relationship('User', backref='role_requests', lazy=True)

    def __repr__(self):
        return f"<RoleRequest User: {self.user_id} Status: {self.status}>"