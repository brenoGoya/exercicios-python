# Challenge 057

""" Update program 056 so that it tells the user if they are too high or too low before they pick again. """

from random import randint

computer_number = randint(1, 10)

user_number = int(input("Enter a number between 1 and 10:\n>> "))

while user_number != computer_number:
    
    user_number = int(input("Try again:\n>> "))

    if user_number == computer_number:

        break

    if user_number > computer_number:

        print("Too high")
    
    else:
        
        print("Too low")
