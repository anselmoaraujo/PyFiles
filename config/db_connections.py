import os
import pyodbc
import psycopg2
from dotenv import load_dotenv

# Load environment variables from the .env file in the project root
load_dotenv()


def get_postgres_connection():
    """
    Establishes a connection to the PostgreSQL database using prefixed environment variables.

    Returns:
        psycopg2.connection: A connection object to the PostgreSQL database.
        Returns None if connection fails or variables are not set.
    """
    try:
        conn = psycopg2.connect(
            host=os.getenv("PG_DB_HOST"),
            port=os.getenv("PG_DB_PORT"),
            dbname=os.getenv("PG_DB_NAME"),
            user=os.getenv("PG_DB_USER"),
            password=os.getenv("PG_DB_PASSWORD")
        )
        print("Successfully connected to PostgreSQL.")
        return conn
    except (psycopg2.Error, TypeError) as e:
        print(f"Error connecting to PostgreSQL: {e}")
        return None


def get_mssql_connection():
    """
    Establishes a connection to the SQL Server database using prefixed environment variables.

    Returns:
        pyodbc.Connection: A connection object to the SQL Server database.
        Returns None if connection fails or variables are not set.
    """
    try:
        conn_str = (
            f'DRIVER={{{os.getenv(what )}}};'
            f'SERVER={os.getenv("MSSQL_DB_HOST")};'
            f'DATABASE={os.getenv("MSSQL_DB_NAME")};'
            f'UID={os.getenv("MSSQL_DB_USER")};'
            f'PWD={os.getenv("MSSQL_DB_PASSWORD")};'
        )
        conn = pyodbc.connect(conn_str)
        print("Successfully connected to SQL Server.")
        return conn
    except (pyodbc.Error, TypeError) as e:
        print(f"Error connecting to SQL Server: {e}")
        return None

# Example of how you might use these functions in another script:
# from db_connections import get_postgres_connection, get_mssql_connection
# pg_conn = get_postgres_connection()
# mssql_conn = get_mssql_connection()
