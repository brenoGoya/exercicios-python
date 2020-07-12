# Challenge 058

""" Make a maths quiz that asks five questions by randomly genereting two whole number to make the question 
(e.g. [num1] + [num2]). Ask the user to enter the answer. If they get it right add a point to their score. At 
the end of the quiz, tell them how many they got correct out of five. """ 

from random import randint

score = 0

for i in range(1, 6):

    num1 = randint(1, 50)

    num2 = randint(1, 50)

    print(f"{num1} + {num2} = ")
    
    computer_answer = num1 + num2

    user_answer = int(input('>> '))

    if user_answer == computer_answer:

        score += 1

print(f'Total score = {score}')
