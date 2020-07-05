# Challenge 042

""" Set a variable called total as 0. Ask to the user to enter five numbers and after each input ask them
if they want that number included. If they do, then add the number to the total. If they do not want it
included, don't add it to the total. After they have entered all five numbers, display the total. """

total = 0

for i in range(0, 5):
    number = int(input('Enter a number:\n>> '))
    answer = input('Do you want to add this number? (y/n)\n>> ').lower()
    if answer == 'y':
        total += number
        print(total)

