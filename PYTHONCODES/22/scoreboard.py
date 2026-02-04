from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, position=(-280, 260)):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(position)  # y=260 is near the top
        self.score = 0
        # Write the score
        self.update_display()

    def update_display(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "bold"))

    def update_score(self):
        self.clear()
        self.score += 1
        self.update_display()
