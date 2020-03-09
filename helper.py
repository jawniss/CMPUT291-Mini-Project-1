# this file contains helper functions for the
# better performance of the project

import sqlite3
from sqlite3 import Error

# import only system from os 
from os import system, name 
# import sleep to show output for some time period 
from time import sleep 

# clear function taken from https://www.geeksforgeeks.org/clear-screen-python/
# define our clear function 
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

# followed this tutorial https://www.sqlitetutorial.net/sqlite-python/creating-database/
def create_connection(db_file):
    # create a database connection to a SQLite database 
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn