import os
import logging
import psycopg2
from dotenv import load_dotenv
from psycopg2 import sql


# Load environment variables from the .env file
if not load_dotenv():
    print("Failed to load environment variables from .env file.")
    exit(1)


def get_connection_params():
    return {
        'dbname': os.getenv('DB_NAME'),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'host': os.getenv('DB_HOST'),
        'port': os.getenv('DB_PORT')
    }


def insert_user_data(user_data):
    """Inserts user data into the database."""
    with psycopg2.connect(**get_connection_params()) as connection:
        with connection.cursor() as cursor:
            try:
                insert_query = sql.SQL("""
                    INSERT INTO Users (name, age, visit, last_drink, preferred_sweet, preferred_sour)
                    VALUES ({name}, {age}, {visit}, {last_drink}, {preferred_sweet}, {preferred_sour})
                    RETURNING id
                """).format(
                    name=sql.Literal(user_data.get('name')),
                    age=sql.Literal(user_data.get('age')),
                    visit=sql.Literal(user_data.get('visit')),
                    last_drink=sql.Literal(user_data.get('last_drink')),
                    preferred_sweet=sql.Literal(user_data.get('preferred_sweet')),
                    preferred_sour=sql.Literal(user_data.get('preferred_sour'))
                )
                
                cursor.execute(insert_query)
                user_id = cursor.fetchone()[0]
                connection.commit()
                print(f"User data inserted with ID: {user_id}")
                return user_id
            except Exception as e:
                print(f"[Error] ~ Inserting user data: {e}")


def get_user_by_id(user_id):
    """Fetches user data by ID from the database."""
    with psycopg2.connect(**get_connection_params()) as connection:
        with connection.cursor() as cursor:
            try:
                select_query = sql.SQL("""
                    SELECT * FROM Users WHERE id = {user_id}
                """).format(user_id=sql.Literal(user_id))
                
                cursor.execute(select_query, (user_id,))
                user_data = cursor.fetchone()

                if user_data:
                    print(f"User found: {user_data}")
                else:
                    print(f"User with ID {user_id} not found.")
            except Exception as e:
                print(f"[Error] ~ Fetching user data: {e}")


if __name__ == "__main__":
    # Example usage:
    user_data = {
        'name': 'John',
        'age': 25,
        'visit': 3,
        'last_drink': 'CocktailXYZ',
        'preferred_sweet': 4,
        'preferred_sour': 2
    }
    user_id_to_get = 2

    insert_user_data(user_data)
    get_user_by_id(user_id_to_get)

