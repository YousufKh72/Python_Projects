import time
from config import screen  # Import the configured Turtle screen
from player import Player  # Player class handling the turtle/player behavior
from car_manager import CarManager  # Manages the cars' movements and spawning
from scoreboard import Scoreboard  # Displays the current score and high scores

# Initialize game components
car = CarManager()
player = Player()
score = Scoreboard()

# Setup keyboard bindings for player movement
screen.onkey(player.moveup, "Up")  # Bind the "Up" arrow key to move the player up
screen.onkey(player.movedown, "Down")  # Bind the "Down" arrow key for down movement
screen.listen()  # Listen for key presses

# Game control variable
game_is_on = True
# Time interval for spawning cars
car_creation_time = 1

# Main game loop
while game_is_on:
    time.sleep(0.1)  # Control game speed / frame rate
    screen.update()  # Update the screen with each iteration
    
    # Spawn and move cars
    car.spawn_car(car_creation_time)
    car.move_cars()
    
    # Collision detection with cars
    for car_inst in car.cars[1:]:  # Check each car in the list except the first one
        if car_inst.distance(player) < 10:  # Detect collision based on distance
            game_is_on = False  # End the game on collision
            screen.clear()  # Clear the screen to prepare for the game over message
            # Prompt the player for their name and display the game over screen
            user_input = screen.textinput("Player", "Enter your name: ")
            score.game_over(user_input)
    
    # Check if the player has reached the top of the screen to level up
    if player.ycor() > 280:
        player.reset()  # Reset the player position
        score.level_up()  # Increment the level and update the scoreboard
        # Increase the cars' speed every 5 levels, max speed capped at 60
        if score.level % 5 == 0:
            car.car_speed = min(car.car_speed + 5, 60)
        else:
            # Decrease the car spawning time to a minimum of 0.1 seconds for higher levels
            car_creation_time = max(car_creation_time - 0.1, 0.1)

# Exit the game cleanly on click
screen.exitonclick()
