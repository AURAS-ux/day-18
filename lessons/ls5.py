from turtle import Turtle,Screen
import random
import turtle

def randColor():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return (r,g,b)

def randAngle():
    angles=[0,30,45,72,90]
    angle=random.choice(angles)
    return angle

tu=Turtle()
turtle.colormode(255)
tu.pensize(10)
def randomWalk():
    tu.forward(100)
    tu.left(randAngle())
    tu.color(randColor())

for i in range(100):
    randomWalk()
screen=Screen()
screen.exitonclick()