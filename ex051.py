# Challenge 051

""" Using the song "10 green bottles", display the lines "There are [num]  green bottles hanging on the wall, [num] green
bottles hanging on the wall, and if 1 green bottle should accidentally fall". Then ask the question "How many green bottles will
be hanging on the wall?". If the user answers correctly, display the message "There will be [num] green bottles
hanging on the wall". If they answer incorrectly, display the message "No, try again" until they get it right.
When the number of green bottles gets down to 0, display the message "There are no more green bottles hanging on the wall". """

num_bottles = 10

while num_bottles > 0:

    print(f'There are {num_bottles} green bottles hanging on the wall, {num_bottles} green bottles hanging on the wall, and if 1 green bottle should accidentally fall.\n')

    num_bottles -= 1

    user_answer = int(input('How many green bottles will be hanging on the wall?\n>> '))

    if user_answer == num_bottles:
        print(f'There will be {num_bottles} green bottles hanging  on the wall\n')
    
    else:
        while user_answer != num_bottles:
            user_answer = int(input('No, try again:\n>> '))

print('There are no more green bottles hanging on the wall')
