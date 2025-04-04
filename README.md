# Inventory Management System

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
   git clone <repository-url>
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

