import turtle
# from turtle import Turtle, Screen
#
# timmy = Turtle()
#
#
# timmy.shape("turtle")
# timmy.color('red4', 'green')
# print(timmy)
# timmy.right(90)
# timmy.forward(500)
# timmy.right(90)
# timmy.forward(500)
# timmy.right(90)
# timmy.forward(500)
# timmy.right(90)
# timmy.forward(500)
#
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.add_row(["Charizard", "Flying"])
table.align = "l"
print(table)
