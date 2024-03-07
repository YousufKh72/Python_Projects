from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.direction = self.head.heading()

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def change_direction(self, new_heading):
        if abs(self.direction - new_heading) != 180:
            self.head.setheading(new_heading)
            self.direction = new_heading

    def add_segment(self, position):
        tim = Turtle("square")
        tim.penup()
        tim.color("white")
        tim.goto(position)
        self.segments.append(tim)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)
        self.no_boundary()

    def no_boundary(self):
        x, y = self.head.position()
        if x > 380:
            self.head.goto(-380, y)
        elif x < -380:
            self.head.goto(380, y)
        elif y > 380:
            self.head.goto(x, -380)
        elif y < -380:
            self.head.goto(x, 380)

    def right(self):
        self.change_direction(RIGHT)

    def up(self):
        self.change_direction(UP)

    def left(self):
        self.change_direction(LEFT)

    def down(self):
        self.change_direction(DOWN)
