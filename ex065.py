# Challenge 065

""" Write the numbers as shown below, starting at the bottom of the number one. """

import turtle

# Number one

turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.penup()

turtle.forward(50)  # Espace between the numbers

# Number two

turtle.pendown()
turtle.forward(75)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(75)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(75)
turtle.penup()

turtle.forward(50)  # Espace between the number 2 to 3


# Number three

turtle.pendown()
turtle.forward(75)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(180)
turtle.penup()
turtle.forward(50)
turtle.pendown()
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(75)


turtle.hideturtle()
turtle.exitonclick()
