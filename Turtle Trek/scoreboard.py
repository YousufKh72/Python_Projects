from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-200, 250)
        self.level = 1
        self.update_scoreboard()
        self.scores = {"YK": 14, "Yousuf": 2, "Jannat": 30, "IK": 4, "Ibrahim": 17}
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self, user_input):     
        self.goto(0, 250)
        self.write("GAME OVER", align="center", font=FONT)
        self.scores[user_input] = self.level
        self.display_scores()

    def level_up(self):
        self.level += 1
        self.update_scoreboard()
        self.goto(0, 0)
        self.write("LEVEL UP", align="center", font=FONT)
        self.goto(-200, 250)
        self.clear()
        self.update_scoreboard()
    
    def reset(self):
        self.level = 1
        self.update_scoreboard()
        self.goto(-200, 250)
        self.update_scoreboard()
    
    def display_scores(self):
        self.goto(0, 200)
        self.write("High Scores", align="center", font=FONT)
        sorted_scores = sorted(self.scores.items(), key=lambda item: item[1], reverse=True)
        for index, (player, score) in enumerate(sorted_scores):
            self.goto(0, 200 - (index + 1) * 50)
            self.write(f"{player:<15}: {score}", align="center", font=FONT)
