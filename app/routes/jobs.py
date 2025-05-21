from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import login_required, current_user
from app.models import Job, Application
from app import db
from datetime import datetime

bp = Blueprint('jobs', __name__)

@bp.route('/jobs/new', methods=['GET', 'POST'])
@login_required
def post_job():
    if not current_user.is_employer:
        flash('Only employers can post jobs')
        return redirect(url_for('main.index'))
    
    if request.method == 'POST':
        job = Job(
            title=request.form['title'],
            description=request.form['description'],
            requirements=request.form['requirements'],
            location=request.form['location'],
            salary_range=request.form['salary_range'],
            job_type=request.form['job_type'],
            employer_id=current_user.id
        )
        db.session.add(job)
        db.session.commit()
        flash('Job posted successfully!')
        return redirect(url_for('jobs.view_job', job_id=job.id))
    
    return render_template('jobs/post.html')

@bp.route('/jobs/<int:job_id>')
def view_job(job_id):
    job = Job.query.get_or_404(job_id)
    return render_template('jobs/view.html', job=job)

@bp.route('/jobs/<int:job_id>/apply', methods=['GET', 'POST'])
@login_required
def apply_job(job_id):
    if current_user.is_employer:
        flash('Employers cannot apply for jobs')
        return redirect(url_for('jobs.view_job', job_id=job_id))
    
    job = Job.query.get_or_404(job_id)
    
    # Check if already applied
    existing_application = Application.query.filter_by(
        job_id=job_id,
        applicant_id=current_user.id
    ).first()
    
    if existing_application:
        flash('You have already applied for this job')
        return redirect(url_for('jobs.view_job', job_id=job_id))
    
    if request.method == 'POST':
        application = Application(
            job_id=job_id,
            applicant_id=current_user.id,
            cover_letter=request.form['cover_letter'],
            resume_url=request.form['resume_url']
        )
        db.session.add(application)
        db.session.commit()
        flash('Application submitted successfully!')
        return redirect(url_for('jobs.view_job', job_id=job_id))
    
    return render_template('jobs/apply.html', job=job)

@bp.route('/jobs/my-jobs')
@login_required
def my_jobs():
    if current_user.is_employer:
        jobs = Job.query.filter_by(employer_id=current_user.id).all()
        return render_template('jobs/my_jobs.html', jobs=jobs)
    else:
        applications = Application.query.filter_by(applicant_id=current_user.id).all()
        return render_template('jobs/my_applications.html', applications=applications) 