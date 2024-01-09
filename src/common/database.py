import os
from dotenv import load_dotenv
import psycopg2
from psycopg2 import sql

# Load environment variables from the .env file
load_dotenv()

def get_connection_params():
    return {
        'dbname': os.getenv('DB_NAME'),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'host': os.getenv('DB_HOST'),
        'port': os.getenv('DB_PORT')
    }

def insert_user_data(user_data, connection_params):
    try:
        connection = psycopg2.connect(**connection_params)
        cursor = connection.cursor()

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

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def get_user_by_id(user_id, connection_params):
    try:
        connection = psycopg2.connect(**connection_params)
        cursor = connection.cursor()

        select_query = sql.SQL("""
            SELECT * FROM Users WHERE id = {user_id}
        """).format(user_id=sql.Literal(user_id))

        cursor.execute(select_query)
        user_data = cursor.fetchone()

        if user_data:
            print(f"User found: {user_data}")
        else:
            print(f"User with ID {user_id} not found.")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

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
    user_id_to_get = 1
    # insert_user_data(user_data, connection_params)

    connection_params = get_connection_params()
    get_user_by_id(user_id_to_get, connection_params)

### TESTING

