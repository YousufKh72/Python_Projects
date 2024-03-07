import turtle
from turtle import Turtle, Screen
import turtle as t

screen = turtle.Screen()
tim = Turtle()
tim.speed("fastest")


def move_fd():
    tim.fd(10)
    print("Forward")


def move_bd():
    tim.setheading(180)
    tim.fd(10)
    print("Backward")


def move_clockwise():
    current_heading = tim.heading() + 10
    tim.setheading(current_heading)
    print("ClockWise")


def move_counterCW():
    current_heading = tim.heading() - 10
    tim.setheading(current_heading)
    print("Counter Clockwise")


def clear_screen():
    tim.clear()
    tim.pu()
    tim.home()
    tim.pd()


screen.listen()
screen.onkey(move_fd, "w")
screen.onkey(move_bd, "s")
screen.onkey(move_clockwise, "a")
screen.onkey(move_counterCW, "d")
screen.onkey(clear_screen, "c")

screen.exitonclick()