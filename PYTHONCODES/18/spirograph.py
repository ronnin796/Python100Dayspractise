from turtle import Turtle, Screen
import random as rm

t = Turtle()
t.speed("fastest")

t.width(10)


def random_color():
    r = rm.randint(0, 255)
    g = rm.randint(0, 255)
    b = rm.randint(0, 255)
    return (r, g, b)


direction = [0, 90, 180, 270]
screen = Screen()
screen.colormode(255)


def spirograph():
    t.color(random_color())
    t.circle(100)
    current_heading = t.heading()
    t.setheading(current_heading + 10)


for _ in range(int(360 / 10)):
    spirograph()

screen.exitonclick()
