from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Inter", 10, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.ht()
        self.penup()
        self.goto(0, 380)
        self.color("white")
        self.update_score()

    def update_score(self):
        self.write(f"Current Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()
