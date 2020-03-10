# https://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/
import sqlite3
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

def logMeInBro(conn, email, pwd):
    inputs = (email, pwd, )
    cur = conn.cursor()
    cur.execute("SELECT * FROM Users WHERE email = ? and pwd = ?;", inputs)
    results = cur.fetchall()
    #if we found nothing matching email/pwd, return false
    if len(results) == 0:
        return False
    else:
        return True




def checkUsernameExists( conn, name ):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    name = (name, )
    cur = conn.cursor()
    cur.execute("SELECT user.name FROM users WHERE name=?;", name)
 
    userName = cur.fetchall()
 
    if( name == userName ):
        return True
    else:
        return False

### i dont think this makes any sense to have??? unless i'm missing something
# def checkPasswordExists( conn, password ):
#     """
#     Query tasks by priority
#     :param conn: the Connection object
#     :param priority:
#     :return:
#     """
#     cur = conn.cursor()
#     cur.execute("SELECT user.password FROM users WHERE password=?", ( password, ))
 
#     userPassword = cur.fetchall()
 
#     if( userPassword == password ):
#         return true
#     else:
#         return false


def addUser(conn, email, name, pwd, city, gender):
    """
    if user doesn't exists, add them to the database
    """
    inputs = (email, name, pwd, city, gender, )
    cur = conn.cursor()
    cur.execute("insert into users values (?, ?, ?, ?, ?);", inputs)
    conn.commit()
    return
    # return cur.lastrowid      not sure why do this part, think extra

def searchSale(conn, keyword):
    keyword = (keyword,keyword, )
    cur = conn.cursor()
    cur.execute("SELECT * FROM sales s where sid in (SELECT sid FROM sales s, products p WHERE s.pid = p.pid AND (s.descr like ? OR p.descr like ?));", keyword)
    conn.commit()
    result = cur.fetchall()
    for row in result:
        print(row)
    return

def salePoster(conn, sid, lister, pid, edate, descr, cond, rprice):
    inputs = (sid, lister, pid, edate, descr, cond, rprice, )
    cur = conn.cursor()
    cur.execute("insert into sales values (?, ?, ?, ?, ?, ?, ?);", inputs)
    conn.commit()
    return


def checkUsernameExists( conn, email ):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    email = (email,)
    cur = conn.cursor()
    cur.executescript("SELECT email FROM users WHERE name=?", email)
 
    existingEmail = cur.fetchall()
 
    if( email == existingEmail ):
        return true
    else:
        return false





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