import turtle
import math
wn=turtle.Screen()
wn.bgcolor("black")
test=turtle.Turtle()
test.speed(500000000)
test.color("White","yellow")
x=5
y=1
a=101
for j in range(180):
    for k in range(3):
        y+=1
        test.forward(math.sqrt(y*y+x*x))
        test.left(a+1)
        test.fillcolor("black")
        test.forward(x+0.1*y)
wn.exitonclick()
