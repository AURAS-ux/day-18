from turtle import Turtle,Screen, Vec2D

tu=Turtle()
for i in range(10):
    for j in range(2):
        tu.forward(5)
        tu.penup()
    tu.pendown()
screen=Screen()
screen.exitonclick()