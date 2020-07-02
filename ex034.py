# Challenge 034

""" Display the following message: 

            1) Square
            2) Triangle

    Enter a number:

If the user enters 1, then it should ask them for the length of one of its sides and display the area.
If They select 2, it should ask for the base and height of the triangle and display the are. If they
type in anything else, it should give them a suitable error message. """

user_answer = int(input('1) Square\n2) Triangule\nEnter a number:\n>>'))

if user_answer == 1 :

    square_side = float(input('Enter the length of one of it sides:\n>> '))

    print(f'AREA = {square_side ** 2}')

elif user_answer == 2 :

    base_triangle = float(input('Enter the base:\n>> '))
    
    height_triangle = float(input('Enter the height:\n>> '))

    print(f'AREA = {(base_triangle * height_triangle) / 2} ')

else:

    print('INCORRECT OPTION SELECTED')
