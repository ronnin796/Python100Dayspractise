from turtle import Turtle, Screen
from paddle import Paddle
import time
from scoreboard import ScoreBoard
from ball import Ball

score1 = ScoreBoard()
score2 = ScoreBoard(position=(280, 260))
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
    # Detect Collision with edges
    if ball.xcor() > 380:
        ball.reset()
        score1.update_score()  # Update score of opposing player
    if ball.xcor() < -380:
        ball.reset()
        score2.update_score()
    # Detect collision with Paddles
    if (
        ball.xcor() > 340
        and ball.distance(paddle1) < 50
        or ball.xcor() < -340
        and ball.distance(paddle2) < 50
    ):
        ball.hit()
        ball.speed_up()

screen.exitonclick()
