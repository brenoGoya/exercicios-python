# Challenge 043

""" Ask which direction the user wants to count (up or down). If they select up, then ask them for the top number
and then count from 1 to that number. If they select down, ask them to enter a number below 20 and then count down
from 20 to that number. If they entered something other than up or down, diplay the message "I don't understand"."""

user_direction = input('Do you want to count up or down?\n>> ').lower()

if user_direction == 'up':
    top_number = int(input('Enter the top number:\n>> '))
    for i in range(1, top_number + 1):
        print(i)

if user_direction == 'down':
    below_number = int(input('Enter a number below 20:\n>> '))
    for i in range(20, below_number -1, -1):
        print(i)
        
else:
    print("I don't understand.")

