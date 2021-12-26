from turtle import Turtle,Screen
import random

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
tu=Turtle()
tu.pensize(10)
def randomWalk():
    tu.forward(100)
    tu.left(random.randint(0,359))
    tu.color(random.choice(colours))

for i in range(100):
    randomWalk()
screen=Screen()
screen.exitonclick()