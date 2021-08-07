import os
from Password_Picker import *
import time as t

new = None
logpath = './logPasswords.txt'
passpath = './'

while newAcc := input('Do you have an account? (y/n): ').lower() not in ['y', 'n']:
    pass

if newAcc == 'y':
    pass
else:
    print('Ok, lets create a new one.')
    t.sleep(0.1)
    loguser = input('What do you want your username to be?: ')
    # if username is already existing print its already taken
    while new not in ['y', 'n']:
        new = input('Do you want to generate a random password?').lower()
    if new == 'y':
        generate()
        logpass = randpass
    else:
        logpass = print('What do you want your password to be?: ')
    

user = input('Enter your username: ')
passw = input('Enter your password: ')

start = input('Do you want to see your password, or create a new one?')