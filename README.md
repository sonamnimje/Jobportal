# Job Portal Website

A modern job portal website built with Flask that allows users to post jobs, search for jobs, and apply for positions.

## Features

- User authentication (signup, login, logout)
- Job posting and management
- Job search and filtering
- Job applications
- User profiles
- Admin dashboard

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows:
```bash
venv\Scripts\activate
```
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