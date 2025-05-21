from app import create_app, db
from app.models import User, Job
from datetime import datetime

app = create_app()

def create_sample_data():
    with app.app_context():
        # Create additional employers
        employers = [
            {
                'username': 'TechSolutions',
                'email': 'hr@techsolutions.com',
                'password': 'employer123',
                'company_name': 'Tech Solutions',
                'is_employer': True
            },
            {
                'username': 'DigitalInnovators',
                'email': 'careers@digitalinnovators.com',
                'password': 'employer123',
                'company_name': 'Digital Innovators',
                'is_employer': True
            },
            {
                'username': 'CloudTech',
                'email': 'jobs@cloudtech.com',
                'password': 'employer123',
                'company_name': 'CloudTech Solutions',
                'is_employer': True
            }
        ]

        # Add employers to database
        for employer_data in employers:
            existing_employer = User.query.filter_by(email=employer_data['email']).first()
            if not existing_employer:
                employer = User(
                    username=employer_data['username'],
                    email=employer_data['email'],
                    is_employer=True,
                    company_name=employer_data['company_name']
                )
                employer.set_password(employer_data['password'])
                db.session.add(employer)
                print(f"Added employer: {employer_data['company_name']}")

        # Additional sample jobs data in INR
        sample_jobs = [
            {
                'title': 'Senior Software Engineer',
                'description': 'Lead the development of complex software systems and mentor junior developers. Work on cutting-edge technologies and deliver high-quality solutions.',
                'requirements': '• 8+ years of software development experience\n• Strong knowledge of Python/Java\n• Experience with cloud platforms\n• Leadership skills\n• Excellent problem-solving abilities\n• Agile methodology experience',
                'location': 'Hyderabad',
                'salary_range': '₹40,00,000 - ₹55,00,000',
                'job_type': 'Full-time',
                'company': 'Tech Solutions'
            },
            {
                'title': 'Machine Learning Engineer',
                'description': 'Develop and deploy machine learning models for various business applications. Work on natural language processing and computer vision projects.',
                'requirements': '• MS/PhD in Computer Science\n• 4+ years of ML experience\n• Strong Python programming\n• Experience with TensorFlow/PyTorch\n• Data preprocessing knowledge\n• Research background',
                'location': 'Chennai',
                'salary_range': '₹30,00,000 - ₹42,00,000',
                'job_type': 'Full-time',
                'company': 'Digital Innovators'
            },
            {
                'title': 'DevOps Engineer',
                'description': 'Build and maintain CI/CD pipelines. Automate infrastructure deployment and ensure system reliability.',
                'requirements': '• 5+ years of DevOps experience\n• Strong knowledge of Docker/Kubernetes\n• AWS/Azure certifications\n• Scripting skills (Python/Shell)\n• Monitoring tools experience\n• Infrastructure automation',
                'location': 'Remote',
                'salary_range': '₹28,00,000 - ₹38,00,000',
                'job_type': 'Full-time',
                'company': 'CloudTech Solutions'
            },
            {
                'title': 'Cybersecurity Analyst',
                'description': 'Protect our systems from cyber threats. Monitor and respond to security incidents. Implement security best practices.',
                'requirements': '• 3+ years of cybersecurity experience\n• Security certifications (CEH, CISSP)\n• Knowledge of threat intelligence\n• Incident response experience\n• Network security\n• Security audits',
                'location': 'Pune',
                'salary_range': '₹22,00,000 - ₹32,00,000',
                'job_type': 'Full-time',
                'company': 'Tech Solutions'
            },
            {
                'title': 'Business Analyst',
                'description': 'Bridge the gap between business and technical teams. Gather requirements and translate them into technical specifications.',
                'requirements': '• 4+ years of BA experience\n• Strong analytical skills\n• Technical understanding\n• Communication skills\n• Problem-solving\n• Project management',
                'location': 'Hybrid - Delhi',
                'salary_range': '₹18,00,000 - ₹28,00,000',
                'job_type': 'Full-time',
                'company': 'Digital Innovators'
            },
            {
                'title': 'Quality Assurance Engineer',
                'description': 'Ensure the quality of our software products through manual and automated testing. Create and maintain test cases.',
                'requirements': '• 3+ years of QA experience\n• Knowledge of testing frameworks\n• Test automation\n• Bug tracking\n• Test planning\n• SQL knowledge',
                'location': 'Remote',
                'salary_range': '₹15,00,000 - ₹25,00,000',
                'job_type': 'Full-time',
                'company': 'CloudTech Solutions'
            }
        ]

        # Add jobs to database
        for job_data in sample_jobs:
            employer = User.query.filter_by(company_name=job_data['company']).first()
            if employer:
                job = Job(
                    title=job_data['title'],
                    description=job_data['description'],
                    requirements=job_data['requirements'],
                    location=job_data['location'],
                    salary_range=job_data['salary_range'],
                    job_type=job_data['job_type'],
                    employer_id=employer.id,
                    posted_date=datetime.utcnow(),
                    is_active=True
                )
                db.session.add(job)
                print(f"Added job: {job_data['title']} at {job_data['company']}")

        try:
            db.session.commit()
            print("Successfully added sample data!")
        except Exception as e:
            db.session.rollback()
            print(f"Error adding sample data: {str(e)}")

if __name__ == '__main__':
    create_sample_data()
