from turtle import Turtle
import random as rm

HEIGHT = 400
WIDTH = 400


class FOOD(Turtle):
    def __init__(self):
        super().__init__()
        self.x_pos = rm.randint(0, HEIGHT)
        self.y_pos = rm.randint(0, WIDTH)
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")

    def update_food_pos(self):
        self.x_pos = rm.randint(0, HEIGHT)
        self.y_pos = rm.randint(0, WIDTH)

    def new_food(self):
        self.update_food_pos()
        self.clear()
        self.teleport(self.x_pos, self.y_pos)
