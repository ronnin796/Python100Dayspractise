from turtle import Turtle
import random as rm

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager:
    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def move(self):
        for car in self.cars:
            car.setx(car.xcor() - self.move_distance)
            if car.xcor() < -300:
                car.hideturtle()
                self.cars.remove(car)

    def increase_speed(self):
        for car in self.cars:
            car.hideturtle()
        self.cars.clear()
        self.move_distance += MOVE_INCREMENT

    def gen_car(self):
        car = Turtle()
        car.color(rm.choice(COLORS))
        car.shape("square")
        car.penup()
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.goto(300, rm.randint(-240, 280))
        self.cars.append(car)
