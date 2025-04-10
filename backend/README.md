# Remote Peak Backend

This is the backend application for the Remote Peak Inventory Management System, built with Django and Django REST Framework.

## 🚀 Features

- Django REST Framework
- JWT Authentication
- PostgreSQL Database
- Role-based permissions
- User management
- Store management
- Inventory tracking
- API documentation

## 🛠 Tech Stack

- Django 5.0.2
- Django REST Framework 3.14.0
- PostgreSQL
- JWT Authentication
- Python-dotenv
- Django CORS Headers
- Simple JWT

## 📋 Prerequisites

- Python 3.8+
- PostgreSQL 12+
- pip

## 🔧 Installation & Setup

1. **Create and activate virtual environment**

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Unix or MacOS:
source venv/bin/activate
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Environment Configuration**
   Create a `.env` file in the backend directory:

```env
DEBUG=True
SECRET_KEY=your-secret-key
DB_NAME=inventory_db
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```

4. **Database Setup**

```bash
# Create PostgreSQL database
createdb inventory_db

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser
```

5. **Run Development Server**

```bash
python manage.py runserver
```

## 📚 Project Structure

```
backend/
├── core/                 # Main Django project
│   ├── settings.py      # Project settings
│   ├── urls.py         # Main URL configuration
│   └── wsgi.py         # WSGI configuration
├── users/              # User management app
│   ├── models.py       # User model
│   ├── views.py        # User views
│   ├── serializers.py  # User serializers
│   └── urls.py         # User URLs
├── inventory/          # Inventory management app
│   ├── models.py       # Inventory models
│   ├── views.py        # Inventory views
│   ├── serializers.py  # Inventory serializers
│   └── urls.py         # Inventory URLs
├── stores/            # Store management app
│   ├── models.py      # Store models
│   ├── views.py       # Store views
│   ├── serializers.py # Store serializers
│   └── urls.py        # Store URLs
└── api/               # API endpoints
    ├── views.py       # API views
    ├── serializers.py # API serializers
    └── urls.py        # API URLs
```

## 🔐 Authentication

The application uses JWT-based authentication with the following endpoints:

- `POST /api/token/` - Obtain JWT tokens
- `POST /api/token/refresh/` - Refresh JWT token
- `POST /api/token/blacklist/` - Blacklist JWT token

## 📝 API Documentation

### User Management

#### Endpoints

- `GET /api/users/` - List users
- `POST /api/users/` - Create user
- `GET /api/users/me/` - Get current user
- `PATCH /api/users/<id>/` - Update user
- `DELETE /api/users/<id>/` - Delete user
- `POST /api/users/change_password/` - Change password

#### Models

```python
class User(AbstractUser):
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.ADMIN
    )
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

### Store Management

#### Endpoints

- `GET /api/stores/` - List stores
- `POST /api/stores/` - Create store
- `GET /api/stores/<id>/` - Get store
- `PATCH /api/stores/<id>/` - Update store
- `DELETE /api/stores/<id>/` - Delete store

### Inventory Management

#### Endpoints

- `GET /api/inventory/` - List inventory items
- `POST /api/inventory/` - Create inventory item
- `GET /api/inventory/<id>/` - Get inventory item
- `PATCH /api/inventory/<id>/` - Update inventory item
- `DELETE /api/inventory/<id>/` - Delete inventory item

## 🔍 Code Quality

- Django's built-in code style
- Black for code formatting
- Flake8 for linting
- Pylint for code analysis

## 🧪 Testing

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test users
python manage.py test inventory
python manage.py test stores
```

## 📦 Dependencies

### Core

- `Django`: Web framework
- `djangorestframework`: REST API framework
- `djangorestframework-simplejwt`: JWT authentication
- `django-cors-headers`: CORS support
- `psycopg2-binary`: PostgreSQL adapter
- `python-dotenv`: Environment variable management

### Development

- `black`: Code formatting
- `flake8`: Linting
- `pylint`: Code analysis
- `pytest`: Testing framework
- `pytest-django`: Django test utilities

## 🚀 Deployment

1. **Set up production environment**

```bash
# Install production dependencies
pip install -r requirements.prod.txt

# Collect static files
python manage.py collectstatic

# Run migrations
python manage.py migrate
```

2. **Configure production settings**

- Update `DEBUG=False`
- Set proper `ALLOWED_HOSTS`
- Configure proper database settings
- Set up proper CORS settings

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📄 License

This project is licensed under the MIT License.
