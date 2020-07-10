# Challenge 047 

""" Ask the user to enter a number and then enter another number. Add these two numbers together and then
ask if they want to add another number. If they enter "y", ask them to enter another number and keep
adding numbers until they do not answer "y". Once the loop has stopped, display the total. """

number_1 = int(input('Enter a number:\n>> '))

total = number_1

answer = 'y'

while answer == 'y':
    number_2 = int(input('Enter another number:\n>> '))
    total += number_2
    answer = input('Do your want top enter another number? [y/n]\n>> ').lower()

print(f'The total is {total}')

