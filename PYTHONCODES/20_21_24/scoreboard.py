from turtle import Turtle
from pathlib import Path

BASE_DIR = Path(__file__).parent
high_score_file = BASE_DIR / "highscore.txt"


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
        self.read_high_score()
        self.update_display()

    def read_high_score(self):
        with open(high_score_file, mode="r") as file:
            score = int(file.read())
            self.highscore = score
            file.close()

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
            with open(high_score_file, mode="w") as file:
                file.write(str(self.highscore))

        self.score = 0

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAMEOVER", align="center", font=("Arial", 24, "bold"))

    def update_score(self):
        self.score += 1
        self.update_display()
