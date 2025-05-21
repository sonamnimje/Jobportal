from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login_manager

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    is_employer = db.Column(db.Boolean, default=False)
    company_name = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    jobs_posted = db.relationship('Job', backref='employer', lazy='dynamic')
    applications = db.relationship('Application', backref='applicant', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    requirements = db.Column(db.Text)
    location = db.Column(db.String(100))
    salary_range = db.Column(db.String(50))
    job_type = db.Column(db.String(50))  # Full-time, Part-time, Contract, etc.
    posted_date = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)
    
    # Foreign Keys
    employer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    # Relationships
    applications = db.relationship('Application', backref='job', lazy='dynamic')

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cover_letter = db.Column(db.Text)
    resume_url = db.Column(db.String(200))
    status = db.Column(db.String(20), default='pending')  # pending, accepted, rejected
    applied_date = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Foreign Keys
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=False)
    applicant_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id)) 