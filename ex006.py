# Challenge 006

""" Ask how many slices of pizza the user started with and ask how many slices they have eaten. Work
out how many slices they have left and display the answer in a user-friendly format. """

start_slices = int(input("How many slices you started?\n>> "))
eaten_slices = int(input("How many slices have you eaten?\n>> "))

slices_left = start_slices - eaten_slices

print(f"You have, {slices_left}, slices remaining.")