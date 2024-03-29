import sqlite3
from sqlite3 import Error
from getpass import getpass #hidden input function
from helper import *
from sqlBackEnd import *

class Handler():
    def __init__(self):
        self.prompt ="-->"
        self.email=""
        self.selecteduser=""
        self.selectedproduct=""
        self.selectedsale=""
        self.conn = ""
        

    def selectLoginOption(self):
        while 1:
            clear()
            databasefilename = input("Please input name of database file: ")
            self.conn = create_connection(databasefilename)
            clear()
            print("Welcome! Please select your login options")
            print("1. Log in: (Already have an account)")
            print("2. Sign up: (Create new account)")
            print("3. Quit")
            signup=input(self.prompt)
            if (signup== "1"):
                self.logIn()
                self.mainMenu()
                return
            elif (signup=="2"):
                self.signUp()
                self.mainMenu()
                return
            elif(signup=="3"):
                return
            else:
                getpass("Invalid command. Press enter to try again")

    # log in by checking credentials
    def logIn(self):
        loggedincorrectly = False
        while not loggedincorrectly:
            clear()
            print("Log In:")
            print("Enter 9 at any time to go back to main menu")
            print("Please enter your email:")

            email = input(self.prompt)
            email = email.lower()
            if(email == "9"):
                self.selectLoginOption()
                return

            print("Please enter your password:")
            pwd = getpass(self.prompt)
            if(pwd == "9"):
                self.selectLoginOption()
                return

            loggedincorrectly = logMeIn(self.conn,email,pwd)
            if loggedincorrectly:
                self.email = email
                loggedincorrectly =True
            else:
                print("Sorry, wrong email or password")
                getpass("Press enter to try again")

    # create new account, make sure email is unique
    # automatically log in 
    def signUp(self):
        signedupcorrectly = False
        while not signedupcorrectly:
            clear()
            pwd=""
            print("Sign Up:")
            print("Enter 9 at any time to go back to main menu")
            print("Please enter your new email:")
            ans=input(self.prompt)

            if(ans == "9"):
                self.selectLoginOption()
                return
            signedupcorrectly = not checkEmailExists(self.conn,ans)
            if signedupcorrectly:
                self.email = ans
                email = self.email

                pwd = getpass("Please enter your new password:")
                if pwd=="9":
                    self.selectLoginOption()
                    return

                name = input("Please enter your name: ")
                if name=="9":
                    self.selectLoginOption()
                    return
                gender = input("please enter your gender: ")
                if gender=="9":
                    self.selectLoginOption()
                    return
                city = input ("Please enter your city: ")
                if city=="9":
                    self.selectLoginOption()
                    return
                addUser(self.conn, email, name, pwd, city, gender)
            else:
                print("Sorry, that email is already being used")
                getpass("Press enter to try again")

    # main loop, gives user access to all the functionalities
    # asks for input and redirects to other methods
    def mainMenu(self):
        while(1):
            clear()
            print("You are logged in as email: "+self.email)
            print("\nMain Menu. \nEnter the number of action to perform")
            print("1. List Products: List all products in active sales")
            print("2. Search for Sales: Use a keyword to search specific sales")
            print("3. Post a Sale: Create your own sale")
            print("4. Search for Users: Use a keyword to search for users")
            print("5. Log Out")
            print("6. Quit")

            selected=input(self.prompt)

            if (selected=="1"):
                self.listProducts()
                #no return needed because after listproducts, we want the user to come
                #back to main menu
            elif (selected =="2"):
                self.searchSales()
            elif (selected=="3"):
                self.postSale()
            elif (selected =="4"):
                self.searchUsers()
            elif (selected =="5"):
                print("Are you sure you want to log out? Y/N")
                sure = input(self.prompt)
                if (sure =="y" or sure =="Y"):
                    self.selectLoginOption()
                    # do not remove this return
                    return
            elif (selected == "6"):
                print("Are you sure you want to quit? Y/N")
                sure = input(self.prompt)
                if (sure =="y" or sure =="Y"):
                    #do not remove this return
                    return
            else:
                    getpass("Invalid command. Press enter to try again")

    # useful function, can be expanded if we want to show more info about the user
    def clearandBasicInfo(self):
        clear()
        print("You are logged in as Username: "+self.email)
        print("Enter 9 at any time to go back to Main Menu\n")
        return

    #shows all products and promts user to choose what to do next
    def listProducts(self):
        self.clearandBasicInfo()
        print("All Available Products:")

        listAllProductsWithSales( self.conn )
        

        # TODO query the db for all products functionality 1
        print("Enter the number of action to perform")
        print("1. Select product")
        print("2. Select sale")
        action=""
        while (action==""):
            action = input(self.prompt)
            if (action =="9"):
                return
            elif(action=="1"):
                self.selectProduct()
                return
            elif(action=="2"):
                self.selectSale()
                return
            else:
                action =""
                getpass("Invalid command. Press enter to try again.")
        
    # promts user to select a product based on its pid
    def selectProduct(self):
        pid=""
        while(pid==""):
            print("Enter the pid of the product you want to select ")
            pid = input(self.prompt)
            if (pid=="9"):
                return

            #TODO write a function that returns a valid pid for the product
            # or returns an empty string in case no product is found
            # replace the following line  
            # pid = function(self.conn, pid)


            self.selectedproduct = pid

        self.clearandBasicInfo()
        print("Displaying information for Product ID: " +self.selectedproduct)

        showProductInfo( self.conn, self.selectedproduct )

        print("\nEnter the number of action to perform")
        print("1. Write a review on this product")
        print("2. List all active sales using this product")
        print("3. List all current product reviews of this product")
        action=""
        while(action==""):
            action = input(self.prompt)
            if (action =="9"):
                return
            elif(action=="1"):
                validrtext = False
                while not validrtext:
                    rtext = ""
                    rtext = input( "Please input your product review text (20 characters or less)" )
                    if len( rtext ) <= 20:
                        validrtext = True
                    else:
                        print( "Review too long, please try again" )
            # later can put an if thing saying pls try again
                rating = float(input( "Please input your rating (1-5)"))
                addProductReview( self.conn, rtext, rating, self.email, self.selectedproduct )
                return
            elif(action=="2"):
                self.listProductSales()
                return
            elif (action=="3"):
                listProductReviews( self.conn, self.selectedproduct )
                return
            else:
                action =""
                getpass("Invalid command. Press enter to try again.")
    ###i believe we dont even use this yet our review writing works
    def writeProductReview(self):
        self.clearandBasicInfo()
        getpass("not implemented yet")
    
    def listProductSales(self):
        self.clearandBasicInfo()
        listActiveSalesOfProd(self.conn, self.selectedproduct)


    def listProductReviews(self):
        self.clearandBasicInfo()
        getpass("not implemented yet")


    def searchSales(self):
        while(1):
            self.clearandBasicInfo()
            print("Search for Sales:")
            print("\nEnter keyword(s) separated by spaces to search for matching sales")
            keyword = "%" + input(self.prompt) + "%"

            if(keyword=="9"):
                return
            else:
                searchSale(self.conn, keyword)
            # try:
            #     #TODO query here
            #     searchSale(self.conn, keyword)
            #     #select matching sales
            # except Error as e:
            #     #other error
            #     return

            print("Enter the number of action to perform")
            print("1. Select sales")
            print("2. Search again")

            action=""
            while(action == ""):
                action = input(self.prompt)
                if(action=="9"):
                    return
                elif(action=="1"):
                    self.selectSale()
                    return
                elif(action=="2"):
                    action = "whatever"
                else:
                    action =""
                    getpass("Invalid command. Press enter to try again.")

    def selectSale(self):
        selectedvalid = False
        while not selectedvalid:
            print("Please enter the sid of the sale you want to select")
            sale = input(self.prompt)
            if(sale=="9"):
                return
            
            try:
                pass
                #TODO query here
                #select valid sale
            except IntegrityError: 
                print ("Invalid sale")
                getpass("Press enter to try again.")
                continue
            except Error as e:
                #other error
                return
            self.selectedsale = sale
            selectedvalid=True
        self.showSale()

    def showSale(self):
        self.clearandBasicInfo()
        print("Displaying information for sale: "+ self.selectedsale)
        print("\nEnter the number of action to perform")
        print("1. Place a bid on this sale")
        print("2. List all active sales of this seller")
        print("3. List all current reviews of this seller")
        print("4. Display information for this seller")
        action=""
        while(action==""):
            action = input(self.prompt)
            if (action =="9"):
                return
            elif(action=="1"):
                self.placeBid()
                return
            elif(action=="2"):
                self.selecteduser="lister of" +self.selectedsale
                self.listUserSales()
                return
            elif (action=="3"):
                self.selecteduser="lister of" +self.selectedsale
                self.listUserReviews()
                return
            elif (action=="4"):
                self.selecteduser="lister of" +self.selectedsale
                self.showUser()
                return
            else:
                action =""
                getpass("Invalid command. Press enter to try again.")

    def postSale(self):
        self.clearandBasicInfo()
        #get pid
        while 1:
            print("Enter the PID of product (optional):")
            pid = input(self.prompt)

            if pid == "":
                pid = None
                break
            elif pid =="9":
                return
            elif not checkProductExists(self.conn,pid):
                getpass("Product does not exist. press enter to try again")
            else:
                break
        #get end date
        while 1:
            print("Please enter the number of days you would like this sale to go on for")
            edate = input(self.prompt)
            # in this case it won't be possible to go back to menu using 9, since it could be 
            # a valid input for end date
            if (edate.isdigit() and edate != "0"):
                break
            else:
                getpass("Please enter a positive number. Press enter to try again")
        #get description
        while 1:
            print("What is the description of the item?")
            descr = input(self.prompt)
            if descr=="9":
                return
            if descr == "":
                getpass("Please enter a non-empty description")
            else:
                break
        # get condition
        while 1:
            print("What is the condition of the item?")
            cond = input(self.prompt)
            if cond=="9":
                return
            if cond == "":
                getpass("Please enter a non-empty condition")
            else:
                break
        while 1:
            print("(Optional) Enter the reserved price")
            rprice = input(self.prompt)
            # in this case it won't be possible to go back to menu using 9, since it could be 
            # a valid input for reserved price
            if rprice== "":
                rprice = "0"
            if rprice.isdigit():
                break
            else:
                getpass("Please enter a positive number. Press enter to try again")
        #randomly generate sale id
        while 1:
            sid = str(randomKey())
            #check we accidentally didnt generate something that already exists
            if not checkSaleExists(self.conn,sid):
                break
        salePoster(self.conn, sid, self.email, pid, edate, descr, cond, rprice)
        getpass("Sale posted successfully, press enter to see sale")
        self.selectedsale = sid
        self.showSale()

    def searchUsers(self):
        while(1):
            self.clearandBasicInfo()
            print("Search for Users:")
            print("\nEnter a keyword to search for matching users")
            keyword = input(self.prompt)

            if(keyword=="9"):
                return

            try:
                # TODO query that selects all matching email, name or city, use the LIKE 
                # function in the query. Then print everything that is a match

                searchUsers( self.conn, keyword )

                #select matching users
            except Error as e:
                getpass(e)
                #other error
                return

            print("Enter the number of action to perform")
            print("1. Select user")
            print("2. Search again")

            action=""
            while(action == ""):
                action = input(self.prompt)
                if(action=="9"):
                    return
                elif(action=="1"):
                    self.selectUser()
                    return
                elif(action=="2"):
                    action="whatever"
                else:
                    action =""
                    getpass("Invalid command. Press enter to try again.")

    
    def selectUser(self):
        selectedvalid = False
        while not selectedvalid:
            print("Please enter the email of the user you want to select")
            email = input(self.prompt)
            if(email=="9"):
                return
            
            try:
                pass
                #TODO query here
                #select valid email
                useremail = selectOneUser( self.conn, email )

            except IntegrityError: 
                print ("Invalid email")
                getpass("Press enter to try again.")
                continue
            except Error as e:
                #other error
                return
            self.selecteduser = useremail
            selectedvalid=True
        self.showUser()
        

    def showUser(self):
        self.clearandBasicInfo()
        print("Displaying information for email: "+ self.selecteduser)
        showUserInfo( self.conn, self.selecteduser )
        print("\nEnter the number of action to perform")
        print("1. Write a review on this user")
        print("2. List all active sales of this user")
        print("3. List all current reviews of this user")
        action = ""
        while (action==""):
            action = input(self.prompt)
        
            if (action =="9"):
                return
            elif(action=="1"):
                self.writeUserReview()
                return
            elif(action=="2"):
                self.listUserSales()
                return
            elif (action=="3"):
                self.listUserReviews()
                return
            else:
                action =""
                getpass("Invalid command. Press enter to try again.")


    def writeUserReview(self):
        self.clearandBasicInfo()
        # getpass("not implemented yet")
        validrtext = False
        while not validrtext:
            rtext = ""
            rtext = input( "Please input your review text (20 characters or less)" )
            if len( rtext ) <= 20:
                validrtext = True
            else:
                print( "Review too long, please try again" )
            # later can put an if thing saying pls try again
        rating = float(input( "Please input your rating (1-5)"))
        addUserReview( self.conn, rtext, rating, self.email, self.selecteduser )

        pass
    
    def listUserSales(self):
        self.clearandBasicInfo()
        listSalesOfSelectedUser( self.conn, self.selecteduser )
        getpass("\nPress enter go to back to main menu")
        return

        
    def listUserReviews(self):
        self.clearandBasicInfo()
        listReviewsOfSelectedUser( self.conn, self.selecteduser )
        getpass("\nPress enter go to back to main menu")
        return


    def placeBid(self):
        self.clearandBasicInfo()
        print("How much would you like to bid?:")
        amount = input(self.prompt)
        sid = self.selectedsale
        bidder = self.email
        bdate = datetime.now()
       #randomly generate bid id
        while 1:
            bid = str(randomKey())
            #check we accidentally didnt generate something that already exists
            if not checkBidExists(self.conn,bid):
                break
        addNewBid(self.conn, bid, bidder, sid, bdate, amount)
        return
