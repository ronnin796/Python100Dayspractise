from turtle import Turtle

PADDLE_SPEED = 30


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.x = 350
        self.y = 0
        self.update_pos()

    def update_pos(self):
        self.teleport(self.x, self.y)

    def up(self):
        if self.y < 300:
            self.y += PADDLE_SPEED
            self.goto(self.x, self.y)

    def down(self):
        if self.y > -300:
            self.y -= PADDLE_SPEED
            self.goto(self.x, self.y)
