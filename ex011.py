# Challenge 011

""" Ask the user to enter a number over 100 and then enter a number under 10 and tell them how many
times the smaller number goes into the larger number in a user-friendly format. """

larger_number = int(input('Enter a number over 100:\n>> '))
smaller_number = int(input('Enter a number under 10:\n>> '))

answer = larger_number // smaller_number

print(f'{smaller_number}, goes into {larger_number} {answer} times.')
