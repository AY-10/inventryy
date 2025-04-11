# Inventryy - Inventory Management System

A full-stack inventory management system built with Django and React.

## Features

- User Authentication (JWT + Social Auth)
- Auth0 Integration
- Role-based Access Control
- Inventory Management
- Store Management
- Sales Tracking
- Real-time Dashboard
- Enhanced User Management Interface
- Role-specific Dashboard Views

## Tech Stack

### Backend

- Django 4.2
- Django REST Framework
- PostgreSQL
- JWT Authentication
- Social Authentication (Google, Facebook)

### Frontend

- React 18
- TypeScript
- Material-UI
- Redux Toolkit
- React Router

## Latest Updates (April 11, 2025)

### Authentication Improvements

- Implemented JWT token-based authentication
- Added token refresh mechanism
- Integrated token blacklisting for secure logout
- Enhanced error handling for authentication failures

### User Interface Enhancements

- Created role-specific dashboard views (Admin and Super Admin)
- Implemented user management interface with CRUD operations
- Added statistics cards for user metrics
- Improved navigation with tabbed interface

### Security Updates

- Added proper token validation
- Implemented secure password handling
- Enhanced role-based access control
- Added session management

## Getting Started

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Start the development server:
   ```bash
   python manage.py runserver
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm start
   ```

## Environment Variables

### Backend (.env)

```
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
FACEBOOK_APP_ID=your-facebook-app-id
FACEBOOK_APP_SECRET=your-facebook-app-secret

# Auth0 Settings
AUTH0_DOMAIN=your-auth0-domain.auth0.com
AUTH0_CLIENT_ID=your-auth0-client-id
AUTH0_CLIENT_SECRET=your-auth0-client-secret
AUTH0_CALLBACK_URL=http://localhost:3000/callback
AUTH0_AUDIENCE=https://your-api-identifier

# JWT Settings
JWT_ACCESS_TOKEN_LIFETIME=60  # minutes
JWT_REFRESH_TOKEN_LIFETIME=1  # days
```

### Frontend (.env)

```
REACT_APP_API_URL=http://localhost:8000/api
REACT_APP_AUTH0_DOMAIN=your-auth0-domain.auth0.com
REACT_APP_AUTH0_CLIENT_ID=your-auth0-client-id
REACT_APP_AUTH0_AUDIENCE=https://your-api-identifier
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Auth0 Setup

1. Create an Auth0 account at [https://auth0.com/](https://auth0.com/)
2. Create a new application (Single Page Application)
3. Configure the following settings in your Auth0 application:
   - Allowed Callback URLs: `http://localhost:3000/callback`
   - Allowed Logout URLs: `http://localhost:3000`
   - Allowed Web Origins: `http://localhost:3000`
4. Create an API in Auth0:
   - Name: `Inventory Management API`
   - Identifier: `https://your-api-identifier`
   - Signing Algorithm: `RS256`
5. Update the `.env` files with your Auth0 credentials
