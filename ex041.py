# Challenge 041

""" Ask the user to enter their name and a number. If the number is less than 10, then display
their name that number of times; otherwise display the message "Too high" three times. """

name = input('Enter your name:\n>> ')
number = int(input('Enter a number:\n>> '))

if number < 10:
    for i in range(0, number):
        print(number)

else:
    for i in range(1, 4):
        print("Too high")
