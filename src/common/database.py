import os
import logging
import psycopg2
from dotenv import load_dotenv
from psycopg2 import sql
from src.common.user import User
from src.common.cocktail import Cocktail


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
                    INSERT INTO Users (name, age, last_drink, occasion, sweet, sour, spicy, fruity, savory, hot, frozen, refreshing)
                    VALUES ({name}, {age}, {last_drink}, {occasion}, {sweet}, {sour}, {spicy}, {fruity}, {savory}, {hot}, {frozen}, {refreshing})
                    RETURNING id
                """).format(
                    name=sql.Literal(user_data.name),
                    age=sql.Literal(user_data.age),
                    # visit=sql.Literal(user_data.visit),
                    last_drink=sql.Literal(user_data.last_drink),
                    occasion=sql.Literal(user_data.occasion),
                    sweet=sql.Literal(user_data.sweet),
                    sour=sql.Literal(user_data.sour),
                    spicy=sql.Literal(user_data.spicy),
                    # bitter=sql.Literal(user_data.bitter),
                    fruity=sql.Literal(user_data.fruity),
                    savory=sql.Literal(user_data.savory),
                    hot=sql.Literal(user_data.hot),
                    frozen=sql.Literal(user_data.frozen),
                    refreshing=sql.Literal(user_data.refreshing)
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


def get_user_by_name(name):
    """Fetches user data by name from the database."""
    with psycopg2.connect(**get_connection_params()) as connection:
        with connection.cursor() as cursor:
            try:
                select_query = sql.SQL("""
                    SELECT * FROM Users WHERE name = {name}
                """).format(name=sql.Literal(name))
                
                cursor.execute(select_query, (name,))
                user_data = cursor.fetchone()
                print(user_data)
                if user_data:
                    return User(*user_data)
                else:
                    return None
            except Exception as e:
                print(f"[Error] ~ Fetching user data: {e}")

def get_all_users():
    """Fetches user data by name from the database."""
    with psycopg2.connect(**get_connection_params()) as connection:
        with connection.cursor() as cursor:
            try:
                select_query = sql.SQL("""
                    SELECT * FROM Users
                """)
                
                cursor.execute(select_query)
                user_data = cursor.fetchall()
                print(user_data)
                if user_data:
                    return User(*user_data)
                else:
                    return None
            except Exception as e:
                print(f"[Error] ~ Fetching user data: {e}")                

def update_user_data(user_id, user_data):
    """Updates user data in the database."""
    with psycopg2.connect(**get_connection_params()) as connection:
        with connection.cursor() as cursor:
            try:
                print(user_id)
                update_query = sql.SQL("""
                    UPDATE Users
                    SET age = {age},
                        last_drink = {last_drink},
                        occasion = {occasion},
                        sweet = {sweet},
                        sour = {sour},
                        spicy = {spicy},
                        fruity = {fruity},
                        savory = {savory},
                        hot = {hot},
                        frozen = {frozen},
                        refreshing = {refreshing}
                    WHERE id = {user_id}
                """).format(
                    age=sql.Literal(user_data.age),
                    # visit=sql.Literal(user_data.visit),
                    last_drink=sql.Literal(user_data.last_drink),
                    occasion=sql.Literal(user_data.occasion),
                    sweet=sql.Literal(user_data.sweet),
                    sour=sql.Literal(user_data.sour),
                    spicy=sql.Literal(user_data.spicy),
                    # bitter=sql.Literal(user_data.bitter),
                    fruity=sql.Literal(user_data.fruity),
                    savory=sql.Literal(user_data.savory),
                    hot=sql.Literal(user_data.hot),
                    frozen=sql.Literal(user_data.frozen),
                    refreshing=sql.Literal(user_data.refreshing),
                    user_id=sql.Literal(user_id)
                )
                cursor.execute(update_query)
                connection.commit()
                print(f"User data updated: {user_data}")
            except Exception as e:
                print(f"[Error] ~ Updating user data: {e}")


def get_all_cocktails():
    """Fetches all cocktails from the database."""
    with psycopg2.connect(**get_connection_params()) as connection:
        with connection.cursor() as cursor:
            try:
                select_query = sql.SQL("""
                    SELECT *
                    FROM cocktail_data
                """)
                cursor.execute(select_query)
                results = cursor.fetchall()
                print("Here are all cocktails:")
                for i in range(0, 10):
                    print(results[i])
            except Exception as e:
                print(f"[Error] ~ getting all cocktails: {e}")

def get_drink_by_cocktail(cocktail):
    """Fetches all ingredients from a cocktail from the database."""
    with psycopg2.connect(**get_connection_params()) as connection:
        with connection.cursor() as cursor:
            try:
                select_query = sql.SQL("""
                    SELECT *
                    FROM cocktail_data
                    WHERE drink = {cocktail}
                """).format(cocktail=sql.Literal(cocktail))
                cursor.execute(select_query)
                results = cursor.fetchone()
                return Cocktail(*results)
            except Exception as e:
                print(f"[Error] ~ getting all ingredients: {e}")


if __name__ == "__main__":
    # Example usage:
    user_data = {
        'id': None,
        'name': 'John',
        'age': 25,
        # 'visit': 3,
        'last_drink': 'CocktailXYZ',
        'occasion': 'birthday',
        'sweet': True,
        'sour': False,
        'spicy': False,
        # 'bitter': False,
        'fruity': False,
        'savory': False,
        'hot': False,
        'frozen': False,
        'refreshing': False
    }
    user_instance = User(**user_data)
    # insert_user_data(user_instance)
    print(get_user_by_name("Nikki"))
    # user_instance.set_age(26)
    # user_instance.set_last_drink("CocktailABC")
    # user_instance.set_occasion("wedding")
    # user_instance.set_sweet(False)
    # user_instance.set_sour(True)

    # update_user_data(user_instance)
    # get_all_cocktails()
    # load_data_from_csv()

