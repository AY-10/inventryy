# Inventory Management System

<<<<<<< HEAD
## Description

This project is an Inventory Management System built with Django REST Framework. It allows users to manage products, stores, and orders efficiently. The system supports role-based access control (RBAC) with Super Admin and Admin roles.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd inventry
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the migrations:
   ```bash
   python manage.py migrate
   ```
2. Start the development server:
   ```bash
   python manage.py runserver
   ```
3. Access the API at `http://127.0.0.1:8000/`.

## API Endpoints

- **User Registration**: `POST /api/register/`
  - Request Body:
    ```json
    {
      "username": "string",
      "password": "string",
      "email": "string"
    }
    ```
- **User Login**: `POST /api/login/`
  - Request Body:
    ```json
    {
      "username": "string",
      "password": "string"
    }
    ```
- **User Management**: `GET /api/users/` (only accessible by Super Admin)
- **Product Management**: `GET /api/products/` (accessible by Admin)
- **Store Management**: `GET /api/stores/` (accessible by Admin)

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
=======
## Overview

This project is an Inventory Management System built with Django. It allows users to manage products, stores, and orders efficiently.

## Features

- User registration and authentication
- Role-based access control
- Product management
- Store management
- Order processing

## Setup Instructions

1. Clone the repository:

   ```
   git clone https://github.com/AY-10/inventryy
   ```

2. Navigate to the project directory:

   ```
   cd backend
   ```

3. Install the required packages:

   ```
   pip install -r requirements.txt
   ```

4. Set up the database:

   - Ensure PostgreSQL is running.
   - Update the database connection parameters in `create_db.py` or set environment variables.

5. Run the migrations:

   ```
   python manage.py migrate
   ```

6. Start the development server:
   ```
   python manage.py runserver
   ```

>>>>>>> 3a73fe38b6c2970a7c98ec11baa3d112aa451c8d
