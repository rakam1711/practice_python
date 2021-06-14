# practice_python
from turtle import Turtle, Screen
timmy = Turtle()
screen = Screen()


def move_forward():
    timmy.forward(20)


def move_backward():
    timmy.back(20)


def move_up():
    current_heading = timmy.heading()+15
    timmy.setheading(current_heading)


def move_down():
    current_heading = timmy.heading() - 15
    timmy.setheading(current_heading)


def clear_all():
    timmy.reset()


screen.listen()
screen.onkey(move_forward, 'd')
screen.onkey(move_backward, 'a')
screen.onkey(move_up, 'w')
screen.onkey(move_down, 'x')
screen.onkey(clear_all, 'c')

screen.exitonclick()
