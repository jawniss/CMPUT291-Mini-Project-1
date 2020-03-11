# https://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/
import sqlite3
from sqlite3 import *
from datetime import datetime

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

def logMeIn(conn, email, pwd):
    inputs = (email, pwd, )
    cur = conn.cursor()
    cur.execute("SELECT * FROM Users WHERE email = ? and pwd = ?;", inputs)
    results = cur.fetchall()
    #if we found nothing matching email/pwd, return false
    if len(results) == 0:
        return False
    else:
        return True




def checkEmailExists( conn, name ):
    """
    check if email already exists
    :param conn: the Connection object
    :param name: the name to check for
    :return: whether the name already exists or not
    """
    name = (name, )
    cur = conn.cursor()
    cur.execute("SELECT users.email FROM users WHERE email=?;", name)

    if(len(cur.fetchall()) == 0):
        return False

    email = cur.fetchall()[0]
 
    if( name == email ):
        return True
    else:
        return False


def addUser(conn, email, name, pwd, city, gender):
    """
    if user doesn't exist, add them to the database
    """
    inputs = (email, name, pwd, city, gender, )
    cur = conn.cursor()
    cur.execute("insert into users values (?, ?, ?, ?, ?);", inputs)
    conn.commit()
    return
    # return cur.lastrowid      not sure why do this part, think extra


def listAllProductsWithSales( conn ):
    currentdate = datetime.now()
    cur = conn.cursor()
    cur.execute("select sid, lister, s.pid, edate, s.descr, cond, rprice from sales s left outer join products p on s.pid = p.pid and (s.descr like ? OR p.descr like ?);", keyword)
    conn.commit()
    result = cur.fetchall()
    for row in result:
        print(row)


def searchSale(conn, keyword):
    keyword = (keyword,keyword, )
    cur = conn.cursor()
    cur.execute("select sid, lister, s.pid, edate, s.descr, cond, rprice from sales s left outer join products p on s.pid = p.pid and (s.descr like ? OR p.descr like ?);", keyword)
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


def checkUsernameExists(conn, email ):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    email = (email, )
    cur = conn.cursor()
    cur.execute("SELECT email FROM users WHERE email=?;", email)
 
    existingEmail = cur.fetchall()
 
    if( email == existingEmail ):
        return True
    else:
        return False


def searchUsers( conn, keyword ):
    tempkeyword = '%' + keyword + '%'
    keyword = ( tempkeyword, tempkeyword, )

    cur = conn.cursor()
    cur.execute( "SELECT email, name, city FROM users WHERE (name LIKE ? OR email LIKE ?);", keyword )
    conn.commit()
    result = cur.fetchall()
    for row in result:
        print(row)
    return 


def selectOneUser( conn, email ):
    tempemail = '%' + email + '%'
    email = ( tempemail, )
    cur = conn.cursor()
    cur.execute( "SELECT email FROM users WHERE (email LIKE ?);", email )    
    conn.commit()

    selecteduser = cur.fetchall()
    emailtuple = selecteduser[0]
    stringofusername = ''.join( emailtuple )
    
    return stringofusername


def showUserInfo( conn, useremail ):
    tempemail = '%' + useremail + '%'
    useremail = ( tempemail, )
    cur = conn.cursor()
    cur.execute( "SELECT * FROM users WHERE (email LIKE ?);", useremail )    
    conn.commit()
    result = cur.fetchall()
    for row in result:
        print(row)

    return


def addUserReview( conn, rtext, rating, reviewer, reviewee ):
    rdate = datetime.today().strftime('%Y-%m-%d')
    inputs = ( reviewer, reviewee, rating, rtext, rdate )
    cur = conn.cursor()
    cur.execute("insert into reviews values (?, ?, ?, ?, ?);", inputs)
    conn.commit()

    return


def listSalesOfSelectedUser( conn, selecteduser ):
    # need to change to follow point 3
    currentdate = datetime.now()

    email = '%' + selecteduser + '%'
    inputs = ( email, currentdate )
    cur = conn.cursor()
    cur.execute( "SELECT * FROM sales WHERE (lister LIKE ? AND CAST(strftime('%s', ?)  AS  integer) <= CAST(strftime('%s', edate)  AS  integer) );", inputs )    
    conn.commit()
    result = cur.fetchall()
    for row in result:
        print(row)