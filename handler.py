import sqlite3
from sqlite3 import Error
from getpass import getpass #hidden input function
from helper import *

class Handler():
    def __init__(self):
        self.prompt ="-->"
        self.username=""
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
            if (signup=="2"):
                self.signUp()
                return
            if(signup=="3"):
                return
            else:
                getpass("Invalid command. Press enter to try again")

    # log in by checking credentials
    def logIn(self):
        loggedincorrectly = False
        while not loggedincorrectly:
            clear()
            print("Log In:")
            print("Enter b/B at any time to go back to main menu")
            print("Please enter your username:")
            ans = input(self.prompt)

            if(ans == "b" or ans == "B"):
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
            print("Enter b/B at any time to go back to main menu")
            print("Please enter your new username:")
            ans=input(self.prompt)

            if(ans == "b" or ans == "B"):
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
        while(1)
            clear()
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
            if (selected="5"):
                print("Are you sure you want to log out? Y/N")
                sure = input(self.prompt)
                if (sure ="y" or sure =="Y"):
                    self.selectLoginOption()
            if (selected == "6"):
                print("Are you sure you want to quit? Y/N")
                sure = input(self.prompt)
                if (sure ="y" or sure =="Y"):
                    return
            else:
                    getpass("Invalid command. Press enter to try again")
    
    def listProducts():
        clear()
        pass
