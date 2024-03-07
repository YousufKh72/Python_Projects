import time
from turtle import Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=1000, height=800)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)

player_one = Paddle((450, 0))
player_two = Paddle((-450, 0))
screen.update()
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(player_one.paddle_move_up, "Up")
screen.onkey(player_one.paddle_move_down, "Down")

screen.onkey(player_two.paddle_move_up, "w")
screen.onkey(player_two.paddle_move_down, "s")

game_is_on = True
while game_is_on:
    score.update_scoreboard()
    time.sleep(0.1)
    screen.update()
    ball.move()
    if abs(ball.ycor()) > 380:
        ball.wall_bounce()
    if ball.distance(player_one) < 70 and ball.xcor() > 420 or ball.distance(player_two) < 70 and ball.xcor() < -420:
        ball.paddle_bounce()
    if ball.xcor() > 480:
        ball.reset_position()
        score.l_point()
    if ball.xcor() < -480:
        ball.reset_position()
        score.r_point()

screen.exitonclick()
