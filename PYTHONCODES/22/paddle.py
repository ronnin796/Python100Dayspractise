from turtle import Turtle

PADDLE_SPEED = 30


class Paddle(Turtle):
    def __init__(self, start_x=350, start_y=0):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.x = start_x
        self.y = start_y
        self.update_pos()

    def update_pos(self):
        self.teleport(self.x, self.y)

    def up(self):
        if self.ycor() < 300:
            self.new_y = self.ycor() + PADDLE_SPEED
            self.goto(self.x, self.new_y)

    def down(self):
        if self.ycor() > -300:
            self.new_y = self.ycor() - PADDLE_SPEED
            self.goto(self.x, self.new_y)
