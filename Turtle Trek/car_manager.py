import random
import time
from turtle import Turtle
from config import screen

# Define available car colors and car images
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

# Register car images as shapes
for car in CARS.values():
            screen.addshape(car)

# Initial movement distance for cars and increment for speed increase
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
# Possible Y-axis positions for cars to appear
Y_AXIS = [-240, -200, -160, -120, -80, -40, 0, 40, 80, 120, 160, 200, 240]

class CarManager(Turtle):
    """Manages the creation, movement, and removal of cars in the game."""
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.last_y = []
        self.last_car_time = time.time()

    def create_car(self):
        """Creates a new car at a random Y position not used by the last 5 cars."""
        new_car = Turtle()
        new_car.penup()
        new_car.shape(random.choice(list(CARS.values())))  # Set car shape to a random image
        new_car.setheading(180)  # Face the car to the left

         # Ensure the new car does not spawn at the same Y position as the last 5 cars
        current_y = random.choice(Y_AXIS)
        while current_y in self.last_y:
            current_y = random.choice(Y_AXIS)

        new_car.goto(280, current_y)  # Position the new car on the right edge
        self.last_y.append(current_y)  # Track the Y position
        self.last_y = self.last_y[-5:]  # Keep only the last 5 Y positions
        self.cars.append(new_car)  # Add the new car to the list of cars

    def move_cars(self):
        """Moves all cars forward based on the current speed."""
        for car in self.cars:
            car.forward(self.car_speed)

    def remove_car(self, car):
        for car in self.cars:
            if car.xcor() < -280:  # Check if the car is out of screen
                car.hideturtle()  # Hide the car
                self.cars.remove(car)  # Remove the car from the list
    
    def spawn_car(self, car_creation_time):
        """Spawns a new car based on a specified time interval."""
        if time.time() - self.last_car_time > car_creation_time:
            self.create_car()
            self.last_car_time = time.time()
