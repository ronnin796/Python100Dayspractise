from turtle import Screen, Turtle
import time
from snake import Snake
from food import FOOD
from scoreboard import ScoreBoard

food = FOOD()
score = ScoreBoard()
snake = Snake()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")


game_on = True
while game_on:

    screen.update()
    time.sleep(0.05)
    snake.move()
    if snake.head.distance(food) < 15:
        food.new_food()
        snake.increase_size()
        score.update_score()

    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        game_on = False
        score.game_over()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()

screen.exitonclick()
