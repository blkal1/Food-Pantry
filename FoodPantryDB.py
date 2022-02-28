import sqlite3
from sqlite3 import Connection, Error


CREATE_FOOD_PANTRY_MANAGER_TABLE = 'CREATE TABLE IF NOT EXISTS Food_Pantry_Manager (product_id INTERGER PRIMARY KEY,  product_name TEXT, quantity_number INTEGER, expiration_date, date_time, house_rating INTEGER ); '


INSERT_FOOD_PANTRY = 'INSERT INTO Food_Pantry_Manager ( product_name, quantity_number, expiration_date, house_rating) VALUES (?,?,?,?);'

GET_ALL_PANTRY = 'SELECT * from Food_Pantry_Manager;'

GET_ALL_PANTRY_BY_NAME = 'SELECT * FROM Food_Pantry_Manager WHERE product_name = ?;'

GET_ALL_PANTRY_BY_DATE = 'SELECT * FROM Food_Pantry_Manager WHERE expiration_date = ?;'

GET_FAV_FOOD = '''
SELECT * from Food_Pantry_Manager
WHERE rating = ?
LIMIT 1;
'''



Connection == sqlite3.connect('pantry.db')

def create_table(connection):
      with connection:
            connection.execute(CREATE_FOOD_PANTRY_MANAGER_TABLE)

def add_food_pantry(connection, product_name, quantity_number, expiration_date, house_rating ):
      with connection:
            connection.execute(INSERT_FOOD_PANTRY, (product_name, quantity_number, expiration_date, house_rating))


def get_all_pantry(connection):
      with connection:
            connection.execute(GET_ALL_PANTRY)

def get_all_pantry_by_name(connection, product_name):
      with connection:
            return connection.execute(GET_ALL_PANTRY_BY_NAME, (product_name, )).fetchall()

def get_all_pantry_by_expiration_date(connection, expiration_date):
      with connection:
            return connection.execute(GET_ALL_PANTRY_BY_NAME, (expiration_date, )).fetchall()

def get_fav_food(connection, house_rating):
      with connection:
            return connection.execute(GET_FAV_FOOD, (house_rating, )).fetchall()
      

