# Challenge 012

""" Ask for two numbers. If the first one is larger than the second, display the second number first
and then the first number, otherwise show the first number first and then the second. """

first_number = int(input('Enter first number:\n>> '))
second_number = int(input('Enter second number:\n>> '))

if first_number > second_number:
    print(second_number, first_number)
else:
    print(first_number, second_number)
    
