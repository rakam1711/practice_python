# practice_python
from turtle import Turtle, Screen
import random
timmy = Turtle()
color = ['CadetBlue1', 'blue', 'DarkOrange1', 'DeepPink', 'coral', 'DarkGreen', 'aquamarine']
direction = [0, 90, 180, 270]
timmy.pensize(10)
timmy.speed(50)
for i in range(1, 100):
    timmy.color(random.choice(color))
    timmy.forward(30)
    timmy.setheading(random.choice(direction))


scree = Screen()
scree.exitonclick()
