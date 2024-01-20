import os
import logging
import psycopg2
from dotenv import load_dotenv
from psycopg2 import sql
# from src.common.user import User
# from src.common.cocktail import Cocktail
from user import User
from cocktail import Cocktail

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
                print(user_data, " here")
                user_values = {
                    'name': user_data.name,
                    'age': user_data.age,
                    'last_drink': user_data.last_drink,
                    'occasion': user_data.occasion,
                    'sour': user_data.sour,
                    'sweet': user_data.sweet,
                    'cream': user_data.cream,
                    'bitter': user_data.bitter,
                    'water': user_data.water,
                    'herbal': user_data.herbal,
                    'egg': user_data.egg,
                    'salty': user_data.salty,
                    'spicy': user_data.spicy
                }
                insert_query = sql.SQL("""
                    INSERT INTO Users ({columns})
                    VALUES ({values})
                    RETURNING id
                """).format(
                    columns=sql.SQL(', ').join(map(sql.Identifier, user_values.keys())),
                    values=sql.SQL(', ').join(map(sql.Literal, user_values.values()))
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
                    return User(*user_data)
                else:
                    print(f"User with ID {user_id} not found.")
                    return None
            except Exception as e:
                print(f"[Error] ~ Fetching user data: {e}")


def get_user_by_name(name):
    """Fetches user data by name from the database."""
    if os.getenv('CONTROL_GROUP').lower() == 'true':
        print("CONTROL GROUP")
        return None  
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
                return user_data
            except Exception as e:
                print(f"[Error] ~ Fetching all user data: {e}")                

def update_user_data(user_id, user_data):
    """Updates user data in the database."""
    with psycopg2.connect(**get_connection_params()) as connection:
        with connection.cursor() as cursor:
            try:
                user_values = {
                    'age': user_data.age,
                    'last_drink': user_data.last_drink,
                    'occasion': user_data.occasion,
                    'sour': user_data.sour,
                    'sweet': user_data.sweet,
                    'cream': user_data.cream,
                    'bitter': user_data.bitter,
                    'water': user_data.water,
                    'herbal': user_data.herbal,
                    'egg': user_data.egg,
                    'salty': user_data.salty,
                    'spicy': user_data.spicy
                }

                update_query = sql.SQL("""
                    UPDATE Users
                    SET ({columns}) = ({values})
                    WHERE id = {user_id}
                """).format(
                    columns=sql.SQL(', ').join(map(sql.Identifier, user_values.keys())),
                    values=sql.SQL(', ').join(map(sql.Literal, user_values.values())),
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


def get_drinks_based_on_user(user_data, max_length=5): 
    with psycopg2.connect(**get_connection_params()) as connection:
        with connection.cursor() as cursor:
            try:
                select_query = sql.SQL("""
                    SELECT *
                    FROM cocktail_data
                    WHERE sour = {sour}
                    AND sweet = {sweet}
                    AND cream = {cream}
                    AND bitter = {bitter}
                    AND water = {water}
                    AND herbal = {herbal}
                    AND egg = {egg}
                    AND salty = {salty}
                    AND spicy = {spicy}
                """).format(
                    sour=sql.Literal(user_data.sour),
                    sweet=sql.Literal(user_data.sweet),
                    cream=sql.Literal(user_data.cream),
                    bitter=sql.Literal(user_data.bitter),
                    water=sql.Literal(user_data.water),
                    herbal=sql.Literal(user_data.herbal),
                    egg=sql.Literal(user_data.egg),
                    salty=sql.Literal(user_data.salty),
                    spicy=sql.Literal(user_data.spicy)
                )
                cursor.execute(select_query)

                results = cursor.fetchall()
                cocktails = []
                for result in results:
                    cocktail = Cocktail(*result)
                    cocktails.append(cocktail)

                return cocktails[:max_length]
            except Exception as e:
                print(f"[Error] ~ getting all similar cocktails: {e}")
    

def change_flavour_profile(user_id, flavor, value):
    """Updates user data in the database."""
    with psycopg2.connect(**get_connection_params()) as connection:
        with connection.cursor() as cursor:
            try:
                update_query = sql.SQL("""
                    UPDATE Users
                    SET {flavour} = {value}
                    WHERE id = {user_id}
                """).format(
                    flavour=sql.Identifier(flavor),
                    value=sql.Literal(value),
                    user_id=sql.Literal(user_id)
                )
                cursor.execute(update_query)
                connection.commit()
                print(f"User data updated: {flavor} {value}")
            except Exception as e:
                print(f"[Error] ~ Updating user data: {e}")


def get_random_cocktail():
    """Fetches a random cocktail from the database."""
    with psycopg2.connect(**get_connection_params()) as connection:
        with connection.cursor() as cursor:
            try:
                select_query = sql.SQL("""
                    SELECT *
                    FROM cocktail_data
                    ORDER BY RANDOM()
                    LIMIT 1
                """)
                cursor.execute(select_query)
                results = cursor.fetchone()
                return Cocktail(*results)
            except Exception as e:
                print(f"[Error] ~ getting random cocktail: {e}")


if __name__ == "__main__":
    get_user_by_name('Nicky')
    # change_flavour_profile(1, "sour", True)
    # # Example usage:
    # user_data = {
    #     'id': None,
    #     'name': 'John',
    #     'age': 25,
    #     # 'visit': 3,
    #     'last_drink': 'CocktailXYZ',
    #     'occasion': 'birthday',
    #     'sour': True,
    #     'sweet': False,
    #     'cream': True,
    #     'bitter': False,  
    #     'water': False,
    #     'herbal': False,
    #     'egg': False,
    #     'salty': False,
    #     'spicy': False
    # }


    # user_instance = User(**user_data)
    # insert_user_data(user_instance)
    # print(get_drink_based_on_user(user_instance))
    # user_instance.set_age(26)
    # user_instance.set_last_drink("CocktailABC")
    # user_instance.set_occasion("wedding")
    # user_instance.set_sweet(False)
    # user_instance.set_sour(True)

    # update_user_data(user_instance)
    # get_all_cocktails()
    # load_data_from_csv()

