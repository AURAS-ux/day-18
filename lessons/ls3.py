from turtle import Turtle,Screen
import random

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
tu=Turtle()
angles=[]
def drawShape(numberOfAngles):
    angle=360/numberOfAngles
    for i in range(numberOfAngles):
        tu.forward(100)
        tu.left(angle)
        
for angleNumber in range(3,11):
    tu.color(random.choice(colours))
    drawShape(angleNumber)
screen=Screen()
screen.exitonclick()