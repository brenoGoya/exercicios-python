# Challenge 044

""" Ask how many people the user wants to invite to a party. If they enter a number below 10, ask for the names
and after each name display "[name] has been invited". If they enter a number wich is 10 or higher, display the 
message "Too many people"."""

number_invite = int(input('How many people do you want to invite?\n>> '))
if number_invite < 10:
     for i in range(0, number_invite):
         name = input('Enter the name the name:\n>> ')
         print(f'{name} has been invited.')
else:
    print('Too many people')
