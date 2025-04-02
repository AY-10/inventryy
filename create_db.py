from psycopg2 import sql
day2import psycopg2

# Database connection parameters
conn_params = {
    'dbname': 'postgres',  # Connect to the default database
    'user': 'postgres',
    'password': 'anurag',
    'host': 'localhost',
    'port': '5432'
}

# Create a new database


def create_database(db_name):
    try:
        # Connect to the PostgreSQL server
        conn = psycopg2.connect(**conn_params)
        conn.autocommit = True  # Enable autocommit mode
        cursor = conn.cursor()

        # Create the database
        cursor.execute(sql.SQL("CREATE DATABASE {}").format(
            sql.Identifier(db_name)))
        print(f"Database '{db_name}' created successfully.")

    except Exception as e:
        print(f"Error creating database: {e}")
    finally:
        cursor.close()
        conn.close()


# Create the 'inventory_db' database
create_database('inventory_db')
