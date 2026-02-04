from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("blue")
        self.y_move = 10
        self.x_move = 10

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def ball_bounce(self):
        self.y_move *= -1

    def hit(self):
        self.x_move *= -1

    def reset(self):
        self.goto(0, 0)
