# Job Portal Website

A modern, responsive job portal website built with Flask that connects employers with job seekers. The platform allows employers to post job listings and manage applications, while job seekers can search for jobs, apply to positions, and manage their applications.

## Features

### For Job Seekers
- User registration and authentication
- Browse and search jobs by title, location, and category
- Apply to jobs directly through the platform
- View job details including salary ranges in INR
- Modern and responsive UI with card-based job listings

### For Employers
- Employer registration and authentication
- Post job listings with detailed requirements
- Manage job postings (edit, delete, deactivate)
- View and manage job applications
- Company profile management

### Technical Features
- Secure user authentication with Flask-Login
- Database management with Flask-SQLAlchemy
- Form handling with Flask-WTF
- Modern UI with Bootstrap 5
- Responsive design for all devices
- Clean and organized code structure

## Tech Stack

- Backend: Flask (Python)
- Database: SQLite
- Frontend: HTML5, CSS3, Bootstrap 5
- Forms: Flask-WTF
- Authentication: Flask-Login
- Database ORM: Flask-SQLAlchemy
- Migrations: Flask-Migrate

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/yourusername/jobportal.git
cd jobportal
```

2. Create and activate virtual environment:
```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
- Unix/MacOS:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the root directory with the following variables:
```
FLASK_APP=app
FLASK_ENV=development
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///jobportal.db
```

5. Initialize the database:
```bash
flask db init
flask db migrate
flask db upgrade
```

6. Run the application:
```bash
flask run
```

The application will be available at `http://localhost:5000`

## Project Structure

```
jobportal/
├── app/
│   ├── __init__.py
│   ├── models/
│   ├── routes/
│   ├── static/
│   └── templates/
├── migrations/
├── .env
├── config.py
├── requirements.txt
└── README.md
``` 
