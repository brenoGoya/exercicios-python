# Challenge 009

""" Write a program that will ask for a number of days and then will show how many hours, minutes
and seconds are in that number of days. """

number_days = int(input("Type the number of days:\n>> "))

hours = number_days * 24
minutes = hours * 60
seconds = minutes * 60

print(f'In {number_days} days, there are {hours} hours, {minutes} minutes and {seconds} seconds.')
