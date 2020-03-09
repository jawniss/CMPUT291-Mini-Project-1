import sqlite3
from sqlite3 import Error
from getpass import getpass #hidden input function
from helper import *

class Handler():
    def __init__(self):
        username=""
        conn = create_connection("miniproject.db")
    def selectLoginOption():
        loginselected = False
        while not loginselected:
            clear()
            print("Welcome! Please select your login options\n")
            print("1. Log in: (Already have an account)\n")
            print("2. Sign up: (Create new account)\n")
            input(signup)
            if (signup== "1"):
                logIn()
                return
            if (signup=="2"):
                signUp()
                return

    # log in by checking credentials
    def logIn():
        clear()
        print("Log In:\nPlease enter your username:")
        input(self.username)
        sql = "SELECT username FROM users WHERE username = ?"
        try:
            #check if username exists
        except Error as e:
            # couldnt check error

    # create new account, make sure username is unique
    # automatically log in 
    def signUp():
        signedupcorrectly = False
        while not signedupcorrectly:
            clear()
            password=""
            print("Sign Up:")
            print("Enter b/B to go back to main menu")
            ans=input("Please enter your new username: ")

            if(ans == "b" or ans == "B"):
                self.selectLoginOption()
                return

            sql = "SELECT username FROM users WHERE username = ?"
            try:
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