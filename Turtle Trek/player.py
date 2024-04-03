from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.color("black")
        self.speed("fastest")
    
    def moveup(self):
        self.forward(MOVE_DISTANCE)
    
    def movedown(self):
        self.backward(MOVE_DISTANCE)
    
    def reset(self):
        self.goto(STARTING_POSITION)
