from turtle import Turtle

# Font configuration for the scoreboard display
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    """A class to represent the game's scoreboard."""
    
    def __init__(self):
        """Initialize the scoreboard."""
        super().__init__()
        self.hideturtle()  # Hide the turtle since we only need to display text
        self.penup()
        self.color("black")
        self.goto(-200, 250)  # Top left corner position for level display
        self.level = 1  # Start game at level 1
        self.scores = {"YK": 14, "Yousuf": 2, "Jannat": 30, "IK": 4, "Ibrahim": 17}  # Preloaded scores
        self.update_scoreboard()  # Display the initial level
    
    def update_scoreboard(self):
        """Clear the current scoreboard and display the current level."""
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self, user_input):
        """Display the game over message and the final scoreboard."""
        self.goto(0, 250)  # Position for game over message
        self.write("GAME OVER", align="center", font=FONT)
        # Update the scores dictionary with the player's score
        self.scores[user_input] = self.level
        self.display_scores()  # Show final scores

    def level_up(self):
        """Increase the level and update the scoreboard."""
        self.level += 1
        self.clear()  # Ensure to clear before redrawing
        self.update_scoreboard()
        self.goto(0, 0)  # Temporary position for level up message
        self.write("LEVEL UP", align="center", font=FONT)
        self.goto(-200, 250)  # Return to the original position for level display

    def reset(self):
        """Reset the level to 1 and update the scoreboard."""
        self.level = 1
        self.clear()  # Clear previous messages
        self.update_scoreboard()  # Display the reset level
    
    def display_scores(self):
        """Sort and display the high scores."""
        self.goto(0, 200)  # Position for high scores title
        self.write("High Scores", align="center", font=FONT)
        # Sort scores in descending order for display
        sorted_scores = sorted(self.scores.items(), key=lambda item: item[1], reverse=True)
        # Display each score
        for index, (player, score) in enumerate(sorted_scores, start=1):
            y_position = 200 - (index * 50)  # Calculate Y position for each score dynamically
            self.goto(0, y_position)
            self.write(f"{player:<15}: {score}", align="center", font=FONT)
