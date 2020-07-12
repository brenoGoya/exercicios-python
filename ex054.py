# Challenge 054

""" Randomly choose either heads or tails ('h' or 't'). Ask the user to make their choice. If their choice is the
same as the ramdomly selected value, display the message "You wim", otherwise display "Bad luck". At the end, tell
the user if the computer selected heads or tails. """

from random import choice

comupter_choice = choice(['t', 'h'])

user_choice = input("Make your choice TAILS 't' or HEADS 'h' :\n>> ")

if user_choice == comupter_choice:
    print("You win")

else:
    print("Bad luck")

if comupter_choice == 'h':
    print("It's heads")
else: 
    print("It's tails")

