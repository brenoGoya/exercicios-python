# Challenge 056

""" Randomly pick a whole number between 1 and 10. Ask the user to enter a number and keep entering numbers until
they enter the number that was randomly pickerd. """

from random import randint

computer_number = randint(1, 10)

user_number = int(input('Enter a number between 1 and 10:\n>> '))

while user_number != computer_number:
    
    user_number = int(input('Wrong number, try another number:\n>> '))
