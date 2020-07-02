# Challenge 029

""" Ask the user to enter an integer that is over 500. Work out the square root of that number and
display it to two decimal places. """

from math import sqrt

number = int(input('Enter a integer number over 500:\n>> '))

print(round(sqrt(number), 2))

# Other way to solve this challenge

print(f'{sqrt(number):.2f}')