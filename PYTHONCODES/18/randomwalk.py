from turtle import Turtle, Screen
import random as rm

color_list = ["red", "blue", "green"]
t = Turtle()
t.shape("turtle")
t.color("blue")
# for i in range(0, 4):
#     gaypan_turtle.forward(20)
#     gaypan_turtle.penup()
#     gaypan_turtle.forward(20)
#     gaypan_turtle.pendown()

# for whilei in range(3, 11):
#     angle = 360 / i
#     for _ in range(i):
#         t.forward(100)
#         t.rt(angle)
# screen = Screen()
# screen.exitonclick()

t.width(20)


def random_walk():
    r = rm.randint(0, 255)
    g = rm.randint(0, 255)
    b = rm.randint(0, 255)
    t.color(r, g, b)
    t.forward(50)
    t.setheading(rm.choice(direction))


direction = [0, 90, 180, 270]
screen = Screen()
screen.colormode(255)


for _ in range(200):
    random_walk()

screen.exitonclick()
