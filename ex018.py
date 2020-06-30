# Challenge 018

""" Ask the user to enter a number. If it is under 10, display the message "Too low", if it their
number is between 10 and 20, display "Correct", otherwise display "Too high". """

number = int(input('Enter a number:\n>> '))

if number > 20:
    print('Too high.')
if number < 10:
    print('Too low.')
else:
    print('Correct.')
    