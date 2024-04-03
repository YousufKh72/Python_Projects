from turtle import Turtle

# Constants for player's starting position, move distance, and finish line Y-coordinate
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280

class Player(Turtle):
    """Represents the player's turtle in the game."""
    
    def __init__(self):
        """Initialize the player turtle with default settings."""
        super().__init__()
        self.shape("turtle")  # Set turtle shape for the player
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)  # Make the turtle smaller
        self.penup()  # Ensure the turtle doesn't draw lines
        self.setheading(90)  # Point the turtle upwards
        self.goto(STARTING_POSITION)  # Move turtle to the starting position
        self.color("black")  # Set the turtle's color
        self.speed("fastest")  # Set the drawing speed to the fastest (affects the move speed)
    
    def moveup(self):
        """Move the player up by a set distance."""
        self.forward(MOVE_DISTANCE)
    
    def movedown(self):
        """Move the player down by a set distance."""
        self.backward(MOVE_DISTANCE)
    
    def reset(self):
        """Reset the player to the starting position."""
        self.goto(STARTING_POSITION)
