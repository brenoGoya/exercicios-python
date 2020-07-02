# Challenge 033

""" Ask the user to enter two numbers. Use whole number division to divide the first number by the second
and also work out the remainder and display the answer in a user-friendly way (e.g. if they enter 7 and 
2 display "7 divided by 2 is 3 with 1 remaining"). """

first_number = int(input('Enter a number:\n>> '))

second_number = int(input('Enter another number:\n>> '))

whole_number = first_number // second_number

remainder_number = first_number % second_number

print(f'{first_number} divided by {second_number} is {whole_number} with {remainder_number} remaining.')