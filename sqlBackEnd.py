# https://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/
import sqlite3
from sqlite3 import *
from datetime import *  
#test
import random

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

def checkProductExists(conn,pid):
    pid = (pid,)
    cur = conn.cursor()
    cur.execute("SELECT pid FROM products WHERE pid like ?;",pid)
    if (len(cur.fetchall())==0):
        return False
    product = cur.fetchall()[0]
    if (product == pid):
        return True
    else:
        return False

def checkSaleExists(conn,sid):
    sid = (sid,)
    cur = conn.cursor()
    cur.execute("SELECT sid FROM sales WHERE sid like ?;",sid)
    all = cur.fetchall()
    if (len(all)==0):
        return False
    sale = all[0]
    if (sale == sid):
        return True
    else:
        return False

def checkBidExists(conn,bid):
    bid = (bid,)
    cur = conn.cursor()
    cur.execute("SELECT bid FROM bids WHERE sid like ?;",bid)
    all = cur.fetchall()
    if (len(all)==0):
        return False
    sale = all[0]
    if (sale == bid):
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
    '''
    For each qualifying product, list the product id, 
    description, the number of reviews, the average rating 
    and the number of active sales associated to the product.
    '''
    currentdate = datetime.now()
    inputs = ( currentdate, )
    cur = conn.cursor()
    # cur.execute("select products.pid, products.descr, count(DISTINCT previews.pid), AVG(previews.rating) from sales, previews, products WHERE products.pid = previews.pid AND products.pid IN (SELECT sales.pid FROM sales WHERE ( CAST(strftime('%s', ?)  AS  integer) <= CAST(strftime('%s', sales.edate)  AS  integer) ));", inputs)
    cur.execute("select products.pid, products.descr, count(DISTINCT previews.pid), AVG(previews.rating) from previews left outer join products on products.pid = previews.pid AND products.pid IN (SELECT sales.pid FROM sales WHERE ( CAST(strftime('%s', ?)  AS  integer) <= CAST(strftime('%s', sales.edate)  AS  integer) ));", inputs)

    conn.commit()
    result = cur.fetchall()
    for row in result:
        print(row)
    # print(result)

    return


def addProductReview( conn, rtext, rating, reviewer, pid ):
    rdate = datetime.today().strftime('%Y-%m-%d')
    rid = random.randint(0, 10000)
    inputs = ( rid, pid, reviewer, rating, rtext, rdate, )
    cur = conn.cursor()
    cur.execute("insert into previews values (?, ?, ?, ?, ?, ?);", inputs)
    conn.commit()

    return


def showProductInfo( conn, pid ):
    tempproduct = '%' + pid + '%'
    pid = ( tempproduct, )
    cur = conn.cursor()
    cur.execute( "SELECT * FROM products WHERE (pid LIKE ?);", pid )    
    conn.commit()
    result = cur.fetchall()
    for row in result:
        print(row)

    return


def listProductReviews( conn, pid ):
    tempproduct = '%' + pid + '%'
    pid = ( tempproduct, )
    cur = conn.cursor()
    cur.execute( "SELECT * FROM previews WHERE (pid LIKE ?);", pid )    
    conn.commit()
    result = cur.fetchall()
    for row in result:
        print(row)
    
    return


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
    edate = datetime.now() + timedelta(days=int(edate))
    inputs = (sid, lister, pid, edate, descr, cond, rprice, )
    cur = conn.cursor()
    cur.execute("insert into sales values (?, ?, ?, ?, ?, ?, ?);", inputs)
    conn.commit()
    return

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
    inputs = ( reviewer, reviewee, rating, rtext, rdate, )
    cur = conn.cursor()
    cur.execute("insert into reviews values (?, ?, ?, ?, ?);", inputs)
    conn.commit()

    return

    ###finish this right now
def addNewBid( conn, bid, bidder, sid, bdate, amount ):
    inputs = (bid, bidder, sid, bdate, amount, )
    cur = conn.cursor()
    cur.execute("insert into bids values (?, ?, ?, ?, ?);", inputs)
    conn.commit()
    return


def listActiveSalesOfProd(conn, pid):
    currentdate = datetime.now()
    inputs = (pid, currentdate, )
    cur = conn.cursor()
    cur.execute("SELECT s.sid, s.lister, s.pid, s.edate, s.descr, s.cond, s.rprice FROM sales s WHERE s.pid = ? AND ( CAST(strftime('%s', ?)  AS  integer) <= CAST(strftime('%s', s.edate)  AS  integer));", inputs)
    conn.commit()
    return



def listSalesOfSelectedUser( conn, selecteduser ):
    # need to change to follow point 3
    currentdate = datetime.now()
    # timeRemaining( edate )

    email = '%' + selecteduser + '%'
    inputs = ( email, currentdate, )
    cur = conn.cursor()
    cur.execute( "SELECT descr, amount FROM sales, bids WHERE (lister LIKE ? AND CAST(strftime('%s', ?)  AS  integer) <= CAST(strftime('%s', edate)  AS  integer) AND sales.sid = bids.sid );", inputs )    
    conn.commit()
    result = cur.fetchall()
    # print(len(result))

    if len(result) == 0:
        cur.execute( "SELECT descr, rprice FROM sales WHERE (lister LIKE ? AND CAST(strftime('%s', ?)  AS  integer) <= CAST(strftime('%s', edate)  AS  integer) );", inputs )    
        conn.commit()
        result = cur.fetchall()
    for row in result:
        print(row)

    return


def listReviewsOfSelectedUser( conn, selecteduser ):
    tempemail = '%' + selecteduser + '%'
    useremail = ( tempemail, )
    cur = conn.cursor()
    cur.execute( "SELECT * FROM reviews WHERE (reviewee LIKE ?);", useremail )    
    conn.commit()
    result = cur.fetchall()
    for row in result:
        print(row)

    return