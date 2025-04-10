# Remote Peak Frontend

This is the frontend application for the Remote Peak Inventory Management System, built with React, TypeScript, and Material-UI.

## 🚀 Features

- Modern React with TypeScript
- Material-UI v5 components
- JWT authentication
- Protected routes
- Responsive design
- User management
- Dashboard with analytics
- Store management
- Inventory tracking

## 🛠 Tech Stack

- React 18
- TypeScript
- React Router v6
- Material-UI v5
- Axios
- Context API
- JWT Authentication

## 📋 Prerequisites

- Node.js 14+
- npm or yarn

## 🔧 Installation & Setup

1. **Install dependencies**

```bash
npm install
```

2. **Environment Configuration**
   Create a `.env` file in the frontend directory:

```env
REACT_APP_API_URL=http://localhost:8000/api
```

3. **Start Development Server**

```bash
npm start
```

## 📚 Project Structure

```
frontend/
├── src/
│   ├── components/     # Reusable components
│   │   ├── Layout/    # Layout components
│   │   ├── Auth/      # Authentication components
│   │   └── Common/    # Common UI components
│   ├── contexts/      # React contexts
│   │   └── AuthContext.tsx
│   ├── pages/         # Page components
│   │   ├── Login.tsx
│   │   ├── Register.tsx
│   │   ├── Dashboard.tsx
│   │   └── UserManagement.tsx
│   ├── services/      # API services
│   │   └── api.ts
│   ├── types/         # TypeScript types
│   │   └── auth.ts
│   └── utils/         # Utility functions
└── public/            # Static files
```

## 🔐 Authentication

The application uses JWT-based authentication with the following flow:

1. User logs in with credentials
2. Server returns access and refresh tokens
3. Tokens are stored in localStorage
4. Access token is used for API requests
5. Refresh token is used to get new access tokens

## 📝 Component Documentation

### Pages

#### Login

- Path: `/login`
- Features:
  - User authentication
  - Error handling
  - Remember me option
  - Password reset link

#### Register

- Path: `/register`
- Features:
  - User registration
  - Form validation
  - Role selection
  - Error handling

#### Dashboard

- Path: `/dashboard`
- Features:
  - Overview statistics
  - Recent activities
  - Quick actions
  - Charts and graphs

#### User Management

- Path: `/users`
- Features:
  - User list
  - User creation
  - User editing
  - User deletion
  - Role management

### Components

#### Layout

- `Sidebar`: Navigation menu
- `Header`: Top navigation bar
- `Footer`: Page footer

#### Auth

- `LoginForm`: Login form component
- `RegisterForm`: Registration form component
- `ProtectedRoute`: Route protection component

#### Common

- `LoadingSpinner`: Loading indicator
- `ErrorAlert`: Error message display
- `ConfirmDialog`: Confirmation dialog

## 🧪 Testing

```bash
# Run tests
npm test

# Run tests with coverage
npm test -- --coverage
```

## 📦 Dependencies

### Core

- `react`: UI library
- `react-dom`: React DOM
- `react-router-dom`: Routing
- `@mui/material`: UI components
- `@mui/icons-material`: Icons
- `axios`: HTTP client

### Development

- `typescript`: TypeScript
- `@types/react`: React types
- `@types/node`: Node.js types
- `@testing-library/react`: Testing utilities
- `@testing-library/jest-dom`: Testing utilities

## 🔍 Code Quality

- ESLint for linting
- Prettier for formatting
- TypeScript for type checking

## 🚀 Deployment

1. **Build the application**

```bash
npm run build
```

2. **Deploy the build folder**
   The `build` folder contains the production-ready application.

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📄 License

This project is licensed under the MIT License.
