# this file contains helper functions for the
# better performance of the project

# import only system from os 
from os import system, name 
# import sleep to show output for some time period 
from time import sleep 

# clear function taken from https://www.geeksforgeeks.org/clear-screen-python/
# define our clear function 
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
