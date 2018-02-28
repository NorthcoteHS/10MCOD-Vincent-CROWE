"""
program: cipher
name: Vincent
Objective: Create a randomised encryption
"""
from random import randint #for randomised numbers
dec = input ('what do you want to encrypt ')
encode = dec
for dec in encode: #for loop
    dec = ord(dec)
    dec = (randint(65, 122)) #turns dec into a random number
    print ((chr(dec)), end='') #turns the number into a letter and prints it on one line
