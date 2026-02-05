from turtle import Screen, Turtle
import time
from snake import Snake
from food import FOOD
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

game_on = False
snake = Snake()


def gamestart():
    global game_on
    game_on = True


food = FOOD()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")
screen.onkey(gamestart, "space")


pen = Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0, 0)
pen.write("Press SPACE to start", align="center", font=("Arial", 24, "bold"))

while True:
    screen.update()
    if game_on:
        snake.reset()
        pen.clear()
        score.reset()
        score.update_display()

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
            food.new_food()
            game_on = False
            score.game_over()

        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                food.new_food()
                game_on = False
                score.game_over()


screen.exitonclick()
