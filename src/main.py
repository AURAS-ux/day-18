import turtle
import random
# import colorgram

# colors=colorgram.extract("asset\painting.jpg",30)
# color_list=[]

# def getRGB():
#     for color in colors:
#         rgb=color.rgb
#         color_tuple=(rgb.r,rgb.g,rgb.b)
#         color_list.append(color_tuple)


# getRGB()
colors = [(241, 222, 86), (35, 98, 185), (86, 174, 218), (169, 67, 37), (217, 158, 84), (187, 16, 34), (173, 49, 85),
          (78, 108, 210), (225, 57, 103), (161, 163, 23), (166, 27, 17), (75, 176, 77), (232, 70, 44), (225, 123, 172),
          (125, 198, 117), (20, 55, 146), (59, 119, 64), (118, 226, 184), (71, 30, 43), (135, 216, 233),
          (238, 158, 217),
          (41, 172, 183), (29, 41, 84), (242, 175, 152), (162, 165, 235), (90, 30, 22)]
scree = turtle.Screen()
tur = turtle.Turtle()
turtle.colormode(255)
tur.penup()
tur.setpos(-300,300)
tur.hideturtle()
def getRandomIndex():
    randomindex=random.randint(0,len(colors))
    return randomindex

def paint():
    for i in range(10):
        for j in range(10):
            tur.dot(20)
            tur.forward(50)
            tur.color(colors[getRandomIndex()-1])
        tur.backward(500)
        tur.right(90)
        tur.forward(50)
        tur.left(90)

tur.penup()
paint()


scree.exitonclick()
