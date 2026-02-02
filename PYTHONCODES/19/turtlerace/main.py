from turtle import Turtle, Screen
import random as rm

# tim = Turtle()
# tim.shape("turtle")
# tim.penup()
screen = Screen()
race_on = False
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
screen.setup(width=700, height=700)
x_positon = -int(screen.window_width() / 2) + 50
y_positon = -int(screen.window_height() / 2) + 50
# tim.setpos(x_positon, y_positon)
turtles = []
for turtle in colors:
    color = turtle
    turtle = Turtle()
    turtle.shape("turtle")
    turtle.penup()

    turtle.color(color)
    turtle.setpos(x_positon, y_positon)
    y_positon += 50
    turtles.append(turtle)
bet = screen.textinput(title="Wanna bet???", prompt="Enter the color")
winner = ""
if bet:
    race_on = True
while race_on:
    for turtle in turtles:
        turtle.forward(rm.randint(5, 10))
        if turtle.xcor() > 340:
            race_on = False
            winner = turtle
if winner.pencolor() == bet:
    print("You win the bet congrats!!")
else:
    print("You lose . The winner was ", winner.pencolor())
screen.exitonclick()
