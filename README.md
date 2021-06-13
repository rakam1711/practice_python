# practice_python
import turtle
from turtle import Turtle, Screen
import random
timmy = Turtle()
turtle.colormode(255)


def colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color1 = (r, g, b)
    return color1
timmy.speed(50)

def spirall(size_of_the_gap):
    for i in range(1, 360//size_of_the_gap):
        timmy.color(colors())
        timmy.circle(50)
        timmy.setheading(timmy.heading()+size_of_the_gap)


spirall(5)
scree = Screen()
scree.exitonclick()
