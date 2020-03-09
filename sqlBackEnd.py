# https://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/
import sqlite3
from sqlite3 import Error


# Create connection to the database file
# followed this tutorial https://www.sqlitetutorial.net/sqlite-python/creating-database/
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


def addUser( conn, newUsername, newPassword ):
    """
    if user doens't exists, add them to the database
    """
    sql = ''' INSERT INTO users( username, password )
              VALUES( ?, ? ) '''

    if( checkUsernameExists( conn, newUsername ) == false and checkPasswordExists( conn, newPassword ) == false ):
        cur = conn.cursor()
        cur.execute( sql, newUsername, newPassword )
    # return cur.lastrowid      not sure why do this part, think extra










"""
def main():
    database = "C:\sqlite\db\pythonsqlite.db"
 
    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new project
        project = ('Cool App with SQLite & Python', '2015-01-01', '2015-01-30');
        project_id = create_project(conn, project)
 
        # tasks
        task_1 = ('Analyze the requirements of the app', 1, 1, project_id, '2015-01-01', '2015-01-02')
        task_2 = ('Confirm with user about the top requirements', 1, 1, project_id, '2015-01-03', '2015-01-05')
 
        # create tasks
        create_task(conn, task_1)
        create_task(conn, task_2)
 
 
if __name__ == '__main__':
    main()

"""