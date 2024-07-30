from turtle import Turtle, Screen
import random

race_on = False
screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race Enter a color: ")
colors = ["blue", "green", "brown", "pink", "red", "black"]
number = 60
# y_pos = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtles_index in range (0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtles_index])
    new_turtle.goto(-230, number)
    number -= 30
    # new_turtle.goto(x=-230, y=y_pos[turtles_index])
    all_turtles.append(new_turtle)

if bet:
    race_on = True

while race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == bet:
                print(f"You have won! The {winning_color} turtle wins!")
            else:
                print(f"You have lost! The {winning_color} turtle wins!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

# tim = Turtle("turtle")
# tom = Turtle("turtle")
# tum = Turtle("turtle")
# tam = Turtle("turtle")
# tem = Turtle("turtle")
# tham = Turtle("turtle")
# tim.penup()
#
# tim.goto(x=-230, y=-90)
# tam.goto(x=-230, y=-60)
# tom.goto(x=-230, y=-30)
# tem.goto(x=-230, y=30)
# tum.goto(x=-230, y=60)
# tham.goto(x=-230, y=0)


screen.exitonclick()