import random
from turtle import Turtle

START = 370
END = -370


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        random_x = random.randint(END, START)
        random_y = random.randint(END, START)
        self.goto(random_x, random_y)

    def refresh(self):
        random_x = random.randint(END, START)
        random_y = random.randint(END, START)
        self.goto(random_x, random_y)
