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
        loginselected = False
        while not loginselected:
            clear()
            print("Welcome! Please select your login options")
            print("1. Log in: (Already have an account)")
            print("2. Sign up: (Create new account)")
            print("3. Quit")
            signup=input("-->")
            if (signup== "1"):
                self.logIn()
                return
            if (signup=="2"):
                self.signUp()
                return
            if(signup=="3"):
                return

    # log in by checking credentials
    def logIn(self):
        loggedincorrectly = False
        while not loggedincorrectly:
            clear()
            print("Log In:\nPlease enter your username:")
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

    # create new account, make sure username is unique
    # automatically log in 
    def signUp(self):
        signedupcorrectly = False
        while not signedupcorrectly:
            clear()
            password=""
            print("Sign Up:")
            print("Enter b/B to go back to main menu")
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

            password = input("Please enter your new password:")