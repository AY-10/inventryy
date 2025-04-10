import os
import subprocess
import sys
from pathlib import Path


def setup_database():
    # Load environment variables
    from dotenv import load_dotenv
    load_dotenv()

    # Database configuration
    db_name = os.getenv('DB_NAME')
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT')

    print("Setting up PostgreSQL database...")

    try:
        # Create database
        subprocess.run([
            'createdb',
            '-h', db_host,
            '-p', db_port,
            '-U', db_user,
            db_name
        ], check=True)
        print(f"Database '{db_name}' created successfully!")
    except subprocess.CalledProcessError as e:
        if "already exists" in str(e):
            print(f"Database '{db_name}' already exists.")
        else:
            print(f"Error creating database: {e}")
            sys.exit(1)

    # Run migrations
    print("\nRunning migrations...")
    try:
        subprocess.run(['python', 'manage.py', 'makemigrations'], check=True)
        subprocess.run(['python', 'manage.py', 'migrate'], check=True)
        print("Migrations completed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error running migrations: {e}")
        sys.exit(1)

    # Create superuser
    print("\nCreating superuser...")
    try:
        subprocess.run(['python', 'manage.py', 'createsuperuser'], check=True)
        print("Superuser created successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error creating superuser: {e}")
        sys.exit(1)


if __name__ == '__main__':
    setup_database()
