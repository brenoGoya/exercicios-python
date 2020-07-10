# Challenge 049

""" Create a variable called compnum and set the value to 50. Ask the user to enter a number.
While their guess is not the same as the compnum value, tell them if their guess is too low
or too high and ask them to have another guess. If they enter the same value as compnum, display
the message "Well done, you took [count] attempts". """

comp_num = 50 
count = 0
answer = int(input("Try to guess the number I am thinking of?:\n>> "))

while answer != comp_num:

    if answer < 50:
        print("Too low")

    else:
        print("Too high")

    answer =  int(input('Have another guess:\n>> '))
    count += 1

print(f'Well done, you took {count} attempts.') 