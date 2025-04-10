import os
import subprocess
import sys
from pathlib import Path


def create_django_project():
    # Create backend directory
    os.makedirs('backend', exist_ok=True)
    os.chdir('backend')

    # Create virtual environment
    subprocess.run([sys.executable, '-m', 'venv', 'venv'])

    # Determine the activation script based on OS
    if sys.platform == 'win32':
        activate_script = 'venv\\Scripts\\activate'
    else:
        activate_script = 'source venv/bin/activate'

    # Install requirements
    subprocess.run(
        f'{activate_script} && pip install -r ../requirements.txt', shell=True)

    # Create Django project
    subprocess.run(
        f'{activate_script} && django-admin startproject core .', shell=True)

    # Create apps
    apps = ['users', 'inventory', 'stores', 'api']
    for app in apps:
        subprocess.run(
            f'{activate_script} && python manage.py startapp {app}', shell=True)

    # Create .env file
    env_content = """DEBUG=True
SECRET_KEY=your-secret-key-here
DB_NAME=inventory_db
DB_USER=postgres
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=5432
"""
    with open('.env', 'w') as f:
        f.write(env_content)

    # Update settings.py
    settings_path = Path('core/settings.py')
    with open(settings_path, 'r') as f:
        settings_content = f.read()

    # Add installed apps
    installed_apps = """
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third party apps
    'rest_framework',
    'corsheaders',
    'rest_framework_simplejwt.token_blacklist',
    
    # Local apps
    'users',
    'inventory',
    'stores',
    'api',
]
"""
    settings_content = settings_content.replace(
        "INSTALLED_APPS = [",
        installed_apps
    )

    # Add REST Framework settings
    rest_framework_settings = """
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

# JWT Settings
from datetime import timedelta
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
}

# CORS Settings
CORS_ALLOW_ALL_ORIGINS = True  # Only for development
CORS_ALLOW_CREDENTIALS = True

# Database Settings
import os
from dotenv import load_dotenv
load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}
"""
    settings_content = settings_content.replace(
        "# SECURITY WARNING: don't run with debug turned on in production!",
        rest_framework_settings +
        "\n# SECURITY WARNING: don't run with debug turned on in production!"
    )

    with open(settings_path, 'w') as f:
        f.write(settings_content)

    print("Django project setup completed successfully!")
    print("\nNext steps:")
    print("1. Create PostgreSQL database: createdb inventory_db")
    print("2. Update .env file with your database credentials")
    print("3. Run migrations: python manage.py makemigrations && python manage.py migrate")
    print("4. Create superuser: python manage.py createsuperuser")
    print("5. Run the development server: python manage.py runserver")


if __name__ == '__main__':
    create_django_project()
