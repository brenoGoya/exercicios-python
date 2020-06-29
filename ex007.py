# Challenge 007

""" Ask the user for their name and their age. Add 1 to their age and display the output """

# [Name] next birthday you will be [new age].

name = input("What is your name?\n>>")
age = int(input("What is your age?\n>>"))

new_age = age + 1

print(f'{name} next birthday you be {new_age}.')
