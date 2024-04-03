import time
from config import screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

car = CarManager()
player = Player()
score = Scoreboard()

screen.onkey(player.moveup, "Up")
screen.onkey(player.movedown, "Down")

game_is_on = True
car_creation_time = 1

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.spawn_car(car_creation_time)
    car.move_cars()
    for car_inst in car.cars[1:]:
        if car_inst.distance(player) < 10:
            game_is_on = False
            screen.clear()
            screen.user_input = screen.textinput("Player", "Enter your name: ")
            score.game_over(screen.user_input)
    if player.ycor() > 280:
        player.reset()
        score.level_up()
        if score.level % 5 == 0:
            car.car_speed = min(car.car_speed + 5, 60)
        else :
            car_creation_time = max(car_creation_time - 0.1, 0.1)

screen.exitonclick()