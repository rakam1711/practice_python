# practice_python
import random
from turtle import Turtle, Screen
race_on = False
screen = Screen()
screen.setup(width=400, height=400)
user_bet = screen.textinput(title='enter your bet', prompt='enter color  of the turtle')
colors = ['red', 'blue', 'green', 'yellow', 'purple']
y_position = [-60, -30, 0, 30, 60]
all_turtle = []
for i in range(0, 5):
    new_turtle = Turtle()
    new_turtle.shape('turtle')
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-170, y=y_position[i])
    all_turtle.append(new_turtle)

if user_bet:
    race_on = True
while race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 200:
            race_on = False
            winner_color = turtle.pencolor()
            if winner_color == user_bet:
                print(f"your{winner_color} wins ")
            else:
                print(f"u lost {winner_color} wins")
        turtle.forward(random.randint(1, 10))
screen.exitonclick()

