import sqlite3
from sqlite3 import Connection, Error

Connection == sqlite3.connect('pantry.db')
c = Connection.cursor()

def create_table():
      c.execute('CREATE TABLE IF NOT EXISTS ')