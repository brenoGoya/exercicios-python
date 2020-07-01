# Challenge 002

""" Ask for the user's first name and then ask for their surname and display the output message """

# Hello [First Name] [Surname].

first_name = input("What's your first name?\n>> ").capitalize()

surname = input("Please type your surname:\n>> ").capitalize()

print(f'Hello, {first_name} {surname}.')
