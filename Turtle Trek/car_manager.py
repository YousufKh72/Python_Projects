import random
import time
from turtle import Turtle
from config import screen

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
CARS = {
    "race_car"   : "car/racecar.gif", 
    "blue_car"   : "car/bluecar.gif",
    "green_car"  : "car/greencar.gif", 
    "orange_car" : "car/orangecar.gif", 
    "purple_car" : "car/purplecar.gif", 
    "red_car"    : "car/redcar.gif",
    "white_car"  : "car/whitecar.gif", 
    "yellow_car" : "car/yellowcar.gif"
}

for car in CARS.values():
            screen.addshape(car)

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
Y_AXIS = [-240, -200, -160, -120, -80, -40, 0, 40, 80, 120, 160, 200, 240]

class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.last_y = []
        self.last_car_time = time.time()

    def create_car(self):
        new_car = Turtle()
        new_car.penup()
        new_car.shape(random.choice(list(CARS.values())))
        new_car.setheading(180)

        current_y = random.choice(Y_AXIS)
        while current_y in self.last_y:
            current_y = random.choice(Y_AXIS)

        new_car.goto(280, current_y)
        self.last_y.append(current_y)
        self.last_y = self.last_y[-5:]
        self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.car_speed)

    def remove_car(self, car):
        for car in self.cars:
            if car.xcor() < -280:
                car.hideturtle()
                self.cars.remove(car)
    
    def spawn_car(self, car_creation_time):
        if time.time() - self.last_car_time > car_creation_time:
            self.create_car()
            self.last_car_time = time.time()
