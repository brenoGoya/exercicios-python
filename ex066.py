# Challenge 066

""" Draw a octagon that uses a different colour (randomly selected form a list of six possible colours) for each line. """ 

import turtle
from random import choice

turtle.pensize(3)

for i in range(0, 8):
    turtle.color(choice(["red", "blue", "green", "yellow", "black", "pink"]))
    turtle.forward(50)
    turtle.right(45)

turtle.exitonclick()