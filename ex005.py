# Challenge 005

""" Ask the user to enter three numbers. Add together the first two numbers and then multiply this total by
the third. Display the answer as """

# The answer is [answer].

number_1 = int(input("Please type a number:\n>> "))
number_2 = int(input("Another number:\n>> "))
number_3 = int(input("One more number:\n>> "))

total = (number_1 + number_2) * number_3

print(f"The answer is {total}.")

