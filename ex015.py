# Challenge 015

""" Ask the user to enter their favourite colour. If they enter "red"
, "RED" or "Red" display the message "I like red too". otherwise display
the message "I don't like [colour], I prefer red". """

colour = input('What is your favourite colour?\n>> ').lower()

if colour == "red":
    print('I like red too.')
else:
    print(f"I don't like {colour}, I prefer red.")
