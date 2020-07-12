# Challenge 059

""" Display five colours and ask the user to pick one. If they pick the same as the program has chosen,
 say "Well done", otherwise display a witty answer wich involves the correct colour, e.g. "I bet you are
 GREEN with envy" or "You are probaly felling BLUE right now". Ask them to guess again; if they have still
 not got it right, keep giving them the same clue and ask the user to enter a colour until they guess it correctly. """ 

from random import choice

colours_choice = choice(["red", "blue", "green", "white", "pink"])


while True:

    user_choice = input("Select from: red, blue, green, pink and white\n>>").lower()
    
    if user_choice == colours_choice:

        print('Well done')
        break

    else:

        if colours_choice == "red":
            
            print("I bet you are seeing RED right now!")

        elif colours_choice == "blue":

            print("Don't feel BLUE.")

        elif colours_choice == "green":

            print("I beet you are GREEN with envy right now.")

        elif colours_choice == "white":

            print("Are you WHITE as a sheet, as you didn't guess correctly?")

        elif colours_choice == "pink":

            print("Shame your are not feeling in the PINK, as you got it wrong!")
        
