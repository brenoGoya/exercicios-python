# Challenge 038

""" Change the program 037 to also ask for a number. Display their name (one letter at a time on each
line) and repeat this for the number of times they entered. """

name = input('Enter your name:\n>> ')
number = int(input('Enter a number:\n>> '))

for x in range(0, number):
    for i in name:
        print(i)
