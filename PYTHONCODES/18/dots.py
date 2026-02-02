###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import random as rm
from turtle import Turtle, Screen


def random_color():
    r = rm.randint(0, 255)
    g = rm.randint(0, 255)
    b = rm.randint(0, 255)
    return (r, g, b)


screen = Screen()
screen.colormode(255)
t = Turtle()
t.hideturtle()
t.speed("fastest")
x_position = 0
y_position = 0
# t.penup()
# t.setpos(x_position, y_position)
# t.pendown()


def reset_pos():
    global y_position
    y_position += 40
    t.penup()
    t.setpos(x_position, y_position)
    t.pendown()


for _ in range(15):
    for _ in range(15):
        t.dot(20, random_color())
        t.penup()
        t.forward(40)
        t.pendown()
    reset_pos()
screen.exitonclick()
