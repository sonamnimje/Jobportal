from flask import Blueprint, render_template, request
from app.models import Job
from app import db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    jobs = Job.query.filter_by(is_active=True)\
        .order_by(Job.posted_date.desc())\
        .paginate(page=page, per_page=10)
    return render_template('index.html', jobs=jobs)

@bp.route('/search')
def search():
    query = request.args.get('q', '')
    location = request.args.get('location', '')
    job_type = request.args.get('type', '')
    
    jobs_query = Job.query.filter_by(is_active=True)
    
    if query:
        jobs_query = jobs_query.filter(Job.title.ilike(f'%{query}%'))
    if location:
        jobs_query = jobs_query.filter(Job.location.ilike(f'%{location}%'))
    if job_type:
        jobs_query = jobs_query.filter(Job.job_type == job_type)
    
    jobs = jobs_query.order_by(Job.posted_date.desc()).all()
    return render_template('search.html', jobs=jobs, query=query, location=location, job_type=job_type) 