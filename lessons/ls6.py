import random
import turtle as t

def randColor():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return (r,g,b)

t.colormode(255)
tu=t.Turtle()
tu.speed(0)
for i in range(360):
    tu.color(randColor())
    hd=tu.heading()
    tu.circle(100)
    tu.setheading(hd+10)
screen=t.Screen()
screen.exitonclick()