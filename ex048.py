# Challenge 048

""" Ask for the name of somebody the user wants to invite to a party. After this, display the message
"[name] has now been invited" and add 1 to the count. Then ask if they want to invite anyone else to the
party and then display how many people they have coming to the party. """

count = 0 
answer = "y"

while answer == "y":

    name = input('Enter a name of somebody you want to invite to a party:\n>> ').title()
    print(f'{name} has now been invited.')
    count += 1
    answer = input('Do you want to invite anyone else? (y/n)\n>> ').lower()

print(f'You inveted {count} people to your party.')

        