# Challenge 008

""" Ask for the total price of the bill, then ask how many diners there are. Divide the total bill 
by the number of diners and show how much each person must pay. """

total_bill = float(input("What is the total cost of the bill?\n>> "))
total_people = float(input("How many people are there?\n>> "))
total_each = total_bill/total_people

print(f'Each person should pay R$ {total_each:.2f}')