from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=700, height=700)
screen.bgcolor("black")
screen.title("My snake game")
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []
for position in starting_positions:
    newsegment = Turtle()
    newsegment.shape("square")
    newsegment.color("red")
    newsegment.penup()
    newsegment.goto(position)
    segments.append(newsegment)


game_on = True
while game_on:
    # screen.update()
    time.sleep(0.1)
    for segment in segments:
        segment.forward(10)
screen.exitonclick()
