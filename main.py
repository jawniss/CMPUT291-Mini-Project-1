from getpass import getpass #hidden input function
import sqlite3
from sqlite3 import Error
from helper.py import *
from funcs.py import *

if __name__="__main__":
    print("welcome to our miniproject\n")

    handler = Handler()
    handler.selectLoginOption()
