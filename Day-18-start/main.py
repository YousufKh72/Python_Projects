import random
import turtle as t
from turtle import (Turtle,
                    Screen)
from random import choice, randint

color = ["black", "slate gray", "blue", "midnight blue", "steel blue", "teal", "green",
         "maroon", "olive drab", "indigo", "dark magenta", "dark violet", "red", "saddle brown"]
t.colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


tim = Turtle()
tim.shape("turtle")


def get_home():
    x, y = tim.pos()
    if abs(x) > 500 or abs(y) > 500:
        tim.penup()
        tim.home()
        tim.pendown()


def random_turn():
    angle = [0, 90, 180, 270]
    return choice(angle)
def turtle_draw(n):
    tim.pendown()
    tim.fd(n)


def turtle_dash(n):
    tim.penup()
    tim.fd(n)


def dashed_line(m, n):
    i = 0
    while i < m:
        turtle_draw(n)
        turtle_dash(n)
        i += 2 * n


def draw_square(n):
    for tutle in range(4):
        tim.fd(n)
        tim.right(90)


def draw_square_invert(n):
    tim.right(90)
    for tutle in range(4):
        tim.fd(n)
        tim.right(90)


def draw_dashed_square(m, n):
    tim.color(random_color())
    draw_multiangled_turtle(4, m, n)


def draw_dashed_square_invert(m, n):
    tim.right(180)
    draw_dashed_square(m, n)


def draw_multiangled_turtle(angle, distance=100, gap=5):
    if angle < 2:
        return
    for _ in range(angle):
        tim.color(random_color())
        turtle_draw(distance)
        tim.right(360 / angle)


def multigon():
    for n in range(3, 5):
        draw_multiangled_turtle(n, 100)


def random_walk(distance=10000, gap=25):
    tim.speed("fastest")
    tim.pensize(5)
    tim.hideturtle()
    i = 0
    while i < distance:
        tim.color(random_color())
        tim.fd(gap)
        tim.right(random_turn())
        get_home()
        i += gap
    tim.showturtle()


def draw_spiral(radius, gap=5):
    tim.hideturtle()
    tim.pensize(1)
    tim.speed("fastest")
    for _ in range(0, 360, gap):
        tim.color(random_color())
        tim.circle(radius)
        tim.setheading(tim.heading() + gap)
    tim.showturtle()


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
            tim.color(random_color())
            tim.pendown()
            tim.begin_fill()
            tim.circle(10)
            tim.end_fill()
            tim.penup()
            tim.fd(50)
    tim.showturtle()


paint_the_wall()
# draw_spiral(100)
# random_walk()
# for _ in range(12):
#     multigon()
#     tim.right(360/12)
# turtle_draw(100)
# turtle_dash(100)
# draw_dashed_square(100, 5)
# tim.home()
# draw_dashed_square(300, 15)
# draw_dashed_square_invert(100, 5)
# tim.home()
# draw_dashed_square_invert(300, 15)
# tim.home()

# draw_square(100)
# tim.color('blue')
# draw_square(300)
# tim.color('green')
# draw_square(-300)
# draw_square(-100)
# draw_square_invert(100)
# draw_square(300)
# draw_square_invert(-300)
# draw_square_invert(-100)
#
# tim.fd(30)
# tim.penup()
# tim.fd(30)
# tim.pendown()
# tim.fd(30)
# tim.circle(6)

screen = Screen()
screen.exitonclick()
