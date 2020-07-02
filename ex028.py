# Challenge 028

""" Update program 027 so that will display the answer to two decimal places. """

number = float(input('Enter a number with lots of decimal places:\n>> '))

print(round(number, 2))

# Another way to display the answer to two decimal places.

print(f'{number:.2f}')
