# Inventory Management System

## Description

This project is an Inventory Management System built with Django REST Framework. It allows users to manage products, stores, and orders efficiently. The system supports role-based access control (RBAC) with Super Admin and Admin roles.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AY-10/inventryy.git
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

