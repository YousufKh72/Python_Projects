# import os
import colorgram
from turtle import Turtle, Screen
import turtle as t
from random import choice, randint
# from PIL import Image

t.colormode(255)
screen = Screen()
# os.environ['PATH'] += os.pathsep + 'C:/Program Files/gs/gsX.XX/bin'

colors = colorgram.extract('Hirst Painting.jpg', 40)
rgb_values = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]
rgb_values = list(set(rgb_values))


def random_color():
    return choice(rgb_values)


def random_turn():
    turns = [0, 45, 90, 135, 180, 225, 270, 315]
    sq_tn = [0, 90, 180, 270]
    return choice(sq_tn)


tim = Turtle()
tim.shape("turtle")


def paint_the_wall():
    tim.hideturtle()
    tim.speed("fastest")
    tim.penup()
    tim.setpos(-450, -400)
    y = -50
    for _ in range(0, 1000, 50):
        if y < 1000:
            tim.setpos(-450, -400 + y)
            y += 50
        for _ in range(0, 1000, 50):
            # tim.color(random_color())
            # tim.pendown()
            # tim.begin_fill()
            # tim.circle(10)
            # tim.end_fill()
            # tim.penup()
            # tim.fd(50)
            tim.dot(20, random_color())
            tim.fd(50)
    tim.showturtle()


def random_hirst_paint():
    tim.ht()
    tim.pu()
    tim.speed("fastest")
    for _ in range(1000):
        tim.dot(20, random_color())
        tim.setheading(random_turn())
        tim.fd(50)


# random_hirst_paint()
paint_the_wall()

# canvas = screen.getcanvas()
# canvas.postscript(file="turtle_drawing.ps")
# img = Image.open("turtle_drawing.ps")
# img.save("turtle_drawing.jpg", "JPEG")

screen.exitonclick()
