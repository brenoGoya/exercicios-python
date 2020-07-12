# Challenge 055

""" Randomly choose a number between 1 and 5. Ask the user to pick a number. If they guess correctly, display the message "Well done", 
otherwise tell them if they are too high or too low and ask them to pick a second number. If they guess correctly on their second guess,
display "Correct", otherwise display "You lose". """ 

from random import randint

computer_number = randint(1, 5)

user_number = int(input('Enter a number between 1 and 5:\n>> '))

if user_number == computer_number:
    print("Well done")

else:
    if user_number > computer_number:
        print("Too high")

    elif user_number < computer_number:
        print("To low")

    user_number = int(input("Try again another number between 1 and 5:\n>> "))

if user_number == computer_number:
    print('Correct')
else: 
    print('You lose')
