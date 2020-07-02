# Challenge 022

""" Ask the user to enter their first name and surname in lower case. Change the case to title case and
join them together. Display the finished result. """

first_name = input('Type your first name in lower case:\n>> ').title()

surname = input('Type your surname in lower case:\n>> ').title()

print(f'{first_name} {surname}')
