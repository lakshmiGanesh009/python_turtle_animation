# Animation circle using turtle library

import turtle
turtle.bgcolor("lightblue")
turtle.pensize(2.5)
turtle.speed(0.5)

colors = ["red","green", "black","orange", "pink"]

for a in range(9):
    for color in colors:
        turtle.color(color)
        turtle.circle(100)
        turtle.left(10)
turtle.mainloop()