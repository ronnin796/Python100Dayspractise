from turtle import Turtle

FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("Black")
        self.goto(0, 260)  # y=260 is near the top
        self.score = 0
        # Write the score
        self.update_display()

    def update_display(self):
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAMEOVER", align="center", font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.update_display()
