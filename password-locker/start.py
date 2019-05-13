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
    if one == "1":
      print("Welcome to password-locker.Would you like to sign up/log in")
      print("Press 1 = sign up / Press 2 = log in / Press 3 = exit")
      logorsign = input()
      if logorsign == "1":  
        print("Awesome!Please enter your preffered username.")
        username = input()
        print("Enter a preffered password.")
        password1 = getpass.getpass("password:")
        print("Confirm your password please.")
        password2 = getpass.getpass("password:")
        if password1 == password2:
          print("New user: " + username + " created.")
          print("*****Choose log in this time.*****")
          save_user(create_user(username,password1)) 
          austin1()
        else:
          print("Sorry passwords don't match.")  
          mitch1()
      elif logorsign == "2":
        print("Enter your username.")
        username = input()
        print("Enter your password.")
        password3 = getpass.getpass("password:") 
        