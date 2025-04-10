# Inventory Management System

A full-stack web application for managing inventory, sales, and stores with user authentication and role-based access control.

## Features

- User Authentication

  - Regular email/password login
  - Social authentication (Google, Facebook)
  - JWT-based authentication
  - Role-based access control (Admin, Super Admin)

- User Management

  - User registration with role selection
  - Profile management
  - Password reset functionality

- Inventory Management

  - Track inventory items
  - Stock management
  - Item categorization

- Sales Management

  - Record sales transactions
  - Track payment methods
  - Sales history and reporting

- Store Management
  - Multiple store support
  - Store-specific inventory
  - Store performance metrics

## Tech Stack

### Backend

- Python 3.13
- Django
- Django REST Framework
- SimpleJWT for authentication
- django-allauth for social authentication
- SQLite database (can be configured for PostgreSQL)

### Frontend

- React
- TypeScript
- Material-UI (MUI)
- React Router
- Axios for API calls

## Prerequisites

- Python 3.13 or higher
- Node.js 14 or higher
- npm or yarn

## Installation

### Backend Setup

1. Clone the repository:

```bash
git clone <repository-url>
cd remote_peak
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install backend dependencies:

```bash
cd backend
pip install -r requirements.txt
```

4. Apply database migrations:

```bash
python manage.py migrate
```

5. Create a superuser:

```bash
python manage.py createsuperuser
```

6. Configure social authentication:
   - Go to Django admin (http://localhost:8000/admin)
   - Add a new Site object with domain "localhost:8000"
   - Configure OAuth credentials in settings.py:
     - Google: Get credentials from Google Cloud Console
     - Facebook: Get credentials from Facebook Developers

### Frontend Setup

1. Install frontend dependencies:

```bash
cd frontend
npm install
```

2. Configure environment variables:
   - Create a .env file in the frontend directory
   - Add necessary environment variables

## Running the Application

### Start the Backend Server

```bash
cd backend
python manage.py runserver
```

The backend will be available at http://localhost:8000

### Start the Frontend Development Server

```bash
cd frontend
npm start
```

The frontend will be available at http://localhost:3000

## API Documentation

### Authentication Endpoints

- POST /api/token/

  - Get JWT tokens
  - Body: { username, password }
  - Returns: { access, refresh }

- POST /api/token/refresh/

  - Refresh access token
  - Body: { refresh }
  - Returns: { access }

- POST /accounts/google/login/

  - Google OAuth login
  - Redirects to Google authentication

- POST /accounts/facebook/login/
  - Facebook OAuth login
  - Redirects to Facebook authentication

### User Endpoints

- GET /api/users/me/

  - Get current user details
  - Requires: Authentication

- POST /api/users/
  - Register new user
  - Body: { username, email, password, role, etc. }

### Store Endpoints

- GET /api/stores/
  - List all stores
  - Requires: Authentication

### Sales Endpoints

- GET /api/sales/
  - List all sales
  - Requires: Authentication

### Inventory Endpoints

- GET /api/inventory/
  - List all inventory items
  - Requires: Authentication

## Role-Based Access

- Super Admin

  - Full access to all features
  - User management
  - System settings

- Admin
  - Store management
  - Inventory management
  - Sales management
  - Limited user management

## Security Features

- JWT Authentication
- CORS protection
- Password hashing
- Social authentication security
- Role-based access control
- Token blacklisting

## Development

### Code Structure

```
remote_peak/
├── backend/
│   ├── core/           # Project settings
│   ├── users/          # User management
│   ├── stores/         # Store management
│   ├── sales/          # Sales management
│   ├── inventory/      # Inventory management
│   └── requirements.txt
└── frontend/
    ├── src/
    │   ├── components/ # Reusable components
    │   ├── pages/      # Page components
    │   ├── services/   # API services
    │   ├── contexts/   # React contexts
    │   └── types/      # TypeScript types
    └── package.json
```

### Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please open an issue in the repository or contact the development team.
