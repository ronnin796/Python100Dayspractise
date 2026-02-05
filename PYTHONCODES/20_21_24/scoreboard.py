from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 260)  # y=260 is near the top
        self.score = 0
        self.highscore = 0
        # Write the score
        self.update_display()

    def update_display(self):
        self.clear()
        self.goto(0, 260)
        self.write(
            f"score: {self.score} High Score: {self.highscore}",
            align="center",
            font=("Arial", 24, "bold"),
        )

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAMEOVER", align="center", font=("Arial", 24, "bold"))

    def update_score(self):
        self.score += 1
        self.update_display()
