from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
paddle = Paddle()
screen.listen()

screen.onkey(paddle.up, "Up")

screen.onkey(paddle.down, "Down")

screen.exitonclick()
