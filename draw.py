"""homework 3: create picture of similar shape and use red and blue colors"""

import turtle

pen = turtle.Turtle()

# control turtle speed and width
pen.speed(2)
pen.width(7)

# this is the start of the shape
pen.setheading(140)
pen.color("red")
pen.forward(90)
pen.setheading(40)
pen.forward(150)
pen.setheading(90)
pen.right(150)
pen.forward(90)
pen.color("blue")
pen.setheading(40)
pen.forward(90)
pen.setheading(300)
pen.forward(140)
pen.right(90)
pen.forward(90)



# this is to conclude the shape for turtle
turtle.done()