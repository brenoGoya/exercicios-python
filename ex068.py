# Challenge 068

""" Draw a pattern that will change each time the program is run. Use the random function to pick the number of lines, the lenght of each line and the angle of each turn. """

import turtle
from random import randint

for x in range(0, randint(5, 20)):
    turtle.forward(randint(25, 100))
    turtle.right(randint(1, 365))

turtle.exitonclick()