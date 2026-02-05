from turtle import Turtle

MOVE_DISTANCE = 20
TURN_ANGLE = 90
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
SPEED = "fastest"


class Snake:
    def __init__(self):
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []
        self.create_snake_whole()
        self.head = self.segments[0]

    def create_snake_whole(self):
        for position in self.starting_positions:
            self.create_snake(position)

    def reset(self):
        for snake in self.segments:
            snake.hideturtle()
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            print(segment, "= ", new_x, " ", new_y)
        self.segments.clear()
        self.create_snake_whole()
        self.head = self.segments[0]
        self.head.setheading(RIGHT)

    def create_snake(self, position):
        newsegment = Turtle()
        newsegment.penup()
        newsegment.speed(SPEED)
        newsegment.shape("square")
        newsegment.color("red")
        newsegment.goto(position)
        self.segments.append(newsegment)

    def increase_size(self):
        self.create_snake(self.segments[-1].position())

    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            print(segment, "= ", new_x, " ", new_y)
            self.segments[segment].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
