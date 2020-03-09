# https://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/
from sqlite3 import *

# Create connection to the database file
def create_connection( db_file ):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect( db_file )
    except Error as e:
        print( e )
 
    return conn




def checkUsernameExists( conn, username ):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT user.name FROM users WHERE username=?", ( username, ))
 
    userUsername = cur.fetchall()
 
    if( userUsername == username ):
        return true
    else:
        return false


def checkPasswordExists( conn, password ):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT user.password FROM users WHERE password=?", ( password, ))
 
    userPassword = cur.fetchall()
 
    if( userPassword == password ):
        return true
    else:
        return false


def addUser( conn, username, password ):
    """
    if making a new user, add them to the database
    """
    