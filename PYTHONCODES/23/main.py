import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

score = ScoreBoard()
cars = CarManager()
player = Player()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(player.move_up, "w")
game_is_on = True
counter = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if counter == 6:
        counter = 0
        cars.gen_car()
    counter += 1
    for car in cars.cars:
        if car.distance(player) < 20 and car.xcor() - 20 < player.xcor():
            score.game_over()
            game_is_on = False
    cars.move()

    if player.ycor() > 280:
        score.update_score()
        player.reset()
        cars.increase_speed()
screen.exitonclick()
