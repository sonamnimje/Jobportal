from app import create_app, db
from app.models import User

app = create_app()

def create_employer():
    with app.app_context():
        # Check if employer already exists
        existing_employer = User.query.filter_by(email='employer@example.com').first()
        if existing_employer:
            print("Employer account already exists!")
            return

        # Create new employer
        employer = User(
            username='TechCorp',
            email='employer@example.com',
            is_employer=True,
            company_name='Tech Corporation'
        )
        employer.set_password('employer123')  # Set a secure password

        try:
            db.session.add(employer)
            db.session.commit()
            print("Employer account created successfully!")
            print("Email: employer@example.com")
            print("Password: employer123")
        except Exception as e:
            db.session.rollback()
            print(f"Error creating employer account: {str(e)}")

if __name__ == '__main__':
    create_employer() 