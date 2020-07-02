# Challenge 021

""" Ask the user to enter their first name and then ask them to enter their surname. Join them together
with a space between and display the name and the length of whole name. """

first_name = input('What is your name?\n>> ').title()

surname = input('What is your surname?\n>> ').title()

name = first_name + " " + surname 

print(F'{name}')

print(len(name))
