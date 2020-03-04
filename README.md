# CMPUT291-MiniProj1

To do list:

  -- LIST PRODUCTS:
    - list prods with sales
    - list product id, description, number of reviews, avg rating, number of active sales of product
    - sale is active if sale end date not passed
    - sort result in desc order of num active sales (prod w/ most sales on top)
    
    - user should be able to select a prod from the listing and
        - write a review: review text and rating (1-5)
        - program should automatically:
          - assign unique review id
          - review date set to current date + time
          - user recorded as reviwer
        - list all reviews of product
        - list all active sales associated with product
          - ordered based on remaining time of sale (sales ending soonest on top)
          
  -- SEARCH FOR SALES:
  
    - user enters 1 or more keywords, system retrieves all active sales w/ at least one keyword in sales description or product description (if the sale associated with a product)
    - order results in descending order of number distinct search keywords that appear in either description
    
  -- LIST PRODUCTS/SEARCH FOR SALES FOLLOW UP:
  
    - listings in list prods and saerch for sales should include for each sale:
      - sale description
      - max bid (if there's bid) or reserved price (if no bids exist)
      - number of days, hours and minutes until sale expires
      
      - from result user should be able to select a sale and see more details
        - email of lister
        - rating of lister (number of reviews and average rating)
        - sale description
        - sale end date and time 
        - condition
        - max bid or reserved price (if no bid)
        - if sale associated to a product, result will also include product description and prod rating (number of reviews and average rating if available or text that prod not reviewed)
        
    - Following actions possible after a sale selected:
      - place bid on sale (enter an amount, application should record bid into database)
        - bid id should be unique number
        - bidder = current user
        - sid = sid of sale
        - bdate = current system time and date
        - bid amount must be > current biggest bid otherwise reject bid
        - user can have multiple bids on same sale
      
      // 3b
      - list all active sales of seller
        - result ordered on remaining time of sale (expire earlier on top)
        
      // 3c
      - list all reviews of seller
      
  -- POST A SALE:
  
    - prompted for product id
    - sale end date and time
    - sale description, condition, reserved price
    - product id and reserved price optional, can be blank
    - when data is entered, proper data should be stored into database w/ unique sale id assigned to sale
      - lister set to current user
      - end date must be in future (valid)
  
  -- SEARCH FOR USERS:
  
    - user enters keyword, system retrieves all user profiles (including email, name, city) that have keyword in name or email
    - from results, can select user and perform actions:
    
      - write review
        - review text and rating (1-5 inclusive)
        - review date, reviewer, reviewee filled automatically by application
        
      - list all active listings of user
        - same format as 3b
        
      - list all reviews of user
        - same format as 3c
        
        
String matching. Except the password which is case-sensitive, all other string matches (including user name, email, etc.) are case-insensitive. This means jonathan will match Jonathan, JONATHAN, and jonathaN, and you cannot make any assumption on the case of the strings in the database. The database can have strings in uppercase, lowercase or any mixed format.

Error checking. Every good programmer should do some basic error checking to make sure the data entered is correct. We cannot say how much error checking you should or should not do, or detail out all possible checkings. However, we can say that we won't be trying to break down your system but your system also should not break down when the user makes a mistake.

Groups of size 3 must counter SQL injection attacks and make the password non-visible at the time of typing.
