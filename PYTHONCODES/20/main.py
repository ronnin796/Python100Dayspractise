from turtle import Screen, Turtle
import time
from snake import Snake

snake = Snake()
screen = Screen()
screen.setup(width=700, height=700)
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
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
