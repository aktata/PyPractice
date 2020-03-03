# PyPractice-RainbowBenzeneDraw

import turtle

turtle.speed(100)
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
turtle.bgcolor('black')
t = turtle.Pen()

for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x/100 + 1)
    t.forward(x)
    t.left(59)

turtle.done()