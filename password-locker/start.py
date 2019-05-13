import getpass
import random
import string
from user import User
from credentials import Credentials

def create_user(username,password1):
    '''
    Function to create new user
    '''
    new_user = User(username,password1)
    return new_user

def create_credentials(account_name,password):
    '''
    Function to create new account
    '''
    new_credentials = User(account_name,password)
    return new_credentials 

def save_user(user):
    '''
    function to save user
    '''
    user.save_user()
 
def save_credentials(self):
    '''
    save_user method to save new users into the list
    '''
    Credentials.credentials_list.append(self)

def check_existing_user(password):
    '''
    function to check that enable login authentification
    '''
    return User.user_exist(password)

def find_account(password):
    '''
    function to find account by its name
    '''
    return User.find_account(password)

def delete_credentials(self):
    '''
    delete method to delete saved information from the list
    '''
    Credentials.credentials_list.remove(self)

def display_credentials():
    '''
    method that returns the user list
    '''
    return User.display_users()

def austin():
  print("The password-locker.")
def austin1():  
  print("Would you like to continue? (yes/no)")
  answer = input() 
  if answer == "yes":
    print("Okay.Press 1 to continue.")
    one = input()
   