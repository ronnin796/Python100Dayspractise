from turtle import Turtle, Screen
from paddle import Paddle
import time
from ball import Ball

ball = Ball()
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
paddle1 = Paddle()
paddle2 = Paddle(-350, 0)
screen.listen()
screen.tracer(0)

screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")
screen.onkey(paddle2.up, "w")
screen.onkey(paddle2.down, "s")
game_on = True
while game_on:
    screen.update()
    ball.move()
    time.sleep(0.05)
    # Collision detection
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.ball_bounce()
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.reset()
    if ball.xcor() > paddle1.xcor() - 20 and ball.distance(paddle1) < 70:
        ball.hit()
    if ball.xcor() < paddle2.xcor() + 20 and ball.distance(paddle2) < 70:
        ball.hit()

screen.exitonclick()
