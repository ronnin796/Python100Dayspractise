from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, position=(0, 260), score="Score"):
        super().__init__()
        self.hideturtle()
        self.score_text = score
        self.penup()
        self.color("white")
        self.position = position
        self.goto(self.position)  # y=260 is near the top
        self.score = 0
        # Write the score
        self.update_display()

    def update_display(self):
        self.clear()
        self.goto(self.position)
        self.write(
            f"{self.score_text}: {self.score}",
            align="center",
            font=("Arial", 24, "bold"),
        )

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAMEOVER", align="center", font=("Arial", 24, "bold"))

    def update_score(self):
        self.clear()
        self.score += 1
        self.update_display()
