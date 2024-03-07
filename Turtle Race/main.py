import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(1200, 1200)
screen.title("Welcome to the turtle race!")
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")

colors = ["red", "orange", "yellow", "blue", "green", "purple"]
n = -125
participants = {}

judge = Turtle(shape="turtle")

for color in colors:
    tim = Turtle(shape="turtle")
    tim.color(color)
    tim.penup()
    tim.goto(x=-500, y=n)
    n += 50
    participants[color] = tim

judge.pu()
judge.goto(x=500, y=300)
judge.setheading(-90)
judge.pd()
judge.fd(600)
judge.setheading(-90)


def who_won(winner, user=user_bet):
    if user == winner:
        screen.textinput("Result", f"{user} wins")
    else:
        screen.textinput("Result", f"{user} lost")


end_race = False

while not end_race:
    t = random.choice(colors)
    # print(t)
    tom = participants[t]
    move = random.randint(0, 10)
    tom.fd(move)
    x, y = tom.position()
    if x > 500:
        who_won(winner=t)
        print(f"{t} wins")
        break

screen.exitonclick()
