import sqlite3
from sqlite3 import Error
from getpass import getpass #hidden input function
from helper import *

class Handler():
    def __init__(self):
        self.prompt ="-->"
        self.username=""
        self.selectedUser=""
        self.conn = create_connection("miniproject.db")

    def selectLoginOption(self):
        while 1:
            clear()
            print("Welcome! Please select your login options")
            print("1. Log in: (Already have an account)")
            print("2. Sign up: (Create new account)")
            print("3. Quit")
            signup=input(self.prompt)
            if (signup== "1"):
                self.logIn()
                return
            elif (signup=="2"):
                self.signUp()
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
            print("Please enter your username:")
            ans = input(self.prompt)

            if(ans == "9"):
                self.selectLoginOption()
                return
            
            self.username = ans

            sql = "SELECT username FROM users WHERE username = ?"
            try:
                pass
                #check if username exists
            except Error as e:
                # something failed
                print(e)
                return
            
            passw = getpass("Please enter your password:")

            if(passw == "b" or passw == "B"):
                self.selectLoginOption()
                return

            try:
                pass
                #TODO query here
                #check for valid password
            except IntegrityError: 
                print ("Invalid password")
                getpass("Press enter to try again.")
                continue
            except Error as e:
                #other error
                return

            loggedincorrectly =True

    # create new account, make sure username is unique
    # automatically log in 
    def signUp(self):
        signedupcorrectly = False
        while not signedupcorrectly:
            clear()
            password=""
            print("Sign Up:")
            print("Enter 9 at any time to go back to main menu")
            print("Please enter your new username:")
            ans=input(self.prompt)

            if(ans == "9"):
                self.selectLoginOption()
                return

            self.username = ans
            sql = "SELECT username FROM users WHERE username = ?"
            try:
                pass
                #TODO query here
                #check for valid username
            except IntegrityError: 
                print ("That username already exists... ")
                getpass("Press enter to try again.")
                continue
            except Error as e:
                #other error
                return

            passw = input("Please enter your new password:")

            if(passw == "b" or passw == "B"):
                self.selectLoginOption()
                return

            try:
                pass
                #TODO query here
                #check for valid password
            except IntegrityError: 
                print ("Invalid password")
                getpass("Press enter to try again.")
                continue
            except Error as e:
                #other error
                return

            name = input("Please enter your name: ")
            gender = input("please enter your gender: ")
            city = input ("Please enter your city: ")

            try:
                pass
                #TODO query here
                #insert user
            except IntegrityError: 
                print ("Invalid password")
                getpass("Press enter to try again.\n")
                continue
            except Error as e:
                #other error
                return

            signedupcorrectly = True

    def mainMenu(self):
        while(1):
            clear()
            print("You are logged in as Username: "+self.username)
            print("Main Menu. Enter the number of action to perform")
            print("1. List Products: List all products in active sales")
            print("2. Search for Sales: Use a keyword to search specific sales")
            print("3. Post a Sale: Create your own sale")
            print("4. Search for Users: Use a keyword to search for users")
            print("5. Log Out")
            print("6. Quit")

            selected=input(self.prompt)

            if (selected=="1"):
                self.listProducts()
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
            elif (selected == "6"):
                print("Are you sure you want to quit? Y/N")
                sure = input(self.prompt)
                if (sure =="y" or sure =="Y"):
                    return
            else:
                    getpass("Invalid command. Press enter to try again")

    def clearandBasicInfo(self):
        clear()
        print("You are logged in as Username: "+self.username)
        print("Enter 9 at any time to go back to Main Menu\n")
        return

    def listProducts(self):
        self.clearandBasicInfo()
        print("not implemented yet")
        pass
    
    def searchSales(self):
        self.clearandBasicInfo()
        print("not implemented yet")

        pass

    def postSale(self):
        self.clearandBasicInfo()
        print("not implemented yet")



    def searchUsers(self):
        self.clearandBasicInfo()
        print("Search for Users:")
        print("\nEnter a keyword to search for matching users")
        keyword = input(self.prompt)

        if(keyword=="9"):
            return

        try:
            pass
            #TODO query here
            #select matching users
        except Error as e:
            #other error
            return
        
        print("TEMPORARY. IMAGINE THE MATCHING USERS HAVE BEEN DISPLAYED")

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
                action = "whatever"
            else:
                action =""
                getpass("Invalid command. Press enter to try again.")

    
    def selectUser(self):
        selectedvalid = False
        while not selectedvalid:
            print("Please enter the username of the user you want to select")
            user = input(self.prompt)
            if(user=="9"):
                return
            
            try:
                pass
                #TODO query here
                #select valid username
            except IntegrityError: 
                print ("Invalid username")
                getpass("Press enter to try again.")
                continue
            except Error as e:
                #other error
                return
            self.selecteduser = user
            selectedvalid=True

        action =""
        while action=="":
            self.clearandBasicInfo()
            print("Displaying information for username: "+ self.selecteduser)
            print("TEMPORARY. IMAGINE USER INFORMATION IS BEING DISPLAYED")
            print("\nEnter the number of action to perform")
            print("1. Write a review on this user")
            print("2. List all active sales of this user")
            print("3. List all current reviews of this user")
            action = input(self.prompt)
            if (action =="9"):
                return
            elif(action=="1"):
                self.writeReview()
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


    def writeReview(self):
        getpass("not implemented yet")
        pass
    
    def listUserSales(self):
        getpass("not implemented yet")
        pass
        
    def listUserReviews(self):
        getpass("not implemented yet")
        pass




