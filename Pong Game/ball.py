from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.setheading(45)
        self.x_move = 10
        self.y_move = 10
        # self.draw_midline()

    def draw_midline(self):
        y = self.ycor()
        self.pensize(10)
        self.setheading(270)
        while y > -390:
            self.pendown()
            self.fd(40)
            self.penup()
            self.fd(40)
            y = self.ycor()
        self.goto(0, 0)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        # current_direction = self.heading()
        # x, y = self.position()
        # if abs(y) > 380 or abs(x) > 500:
        #     self.setheading(current_direction - 90)
        # if abs(y) > 380 or abs(x) > 480:
        #     self.goto(0, 0)

    def wall_bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.paddle_bounce()
