# Challenge 039

""" Ask the user to enter a number between 1 and 12 and then display the times table or that number. """

number = int(input('Enter a number between 1 and 12:\n >>'))

for i in range(1, 13):
    print(f'{i} X {number} = {i * number}')
