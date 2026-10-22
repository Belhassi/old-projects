import turtle
import math

pen = turtle.Turtle()
pen.speed(20)
pen.color("red", "")

pen.penup()
pen.goto(190, 0)
pen.pendown()


pen.begin_fill()
for i in range(800):
	pen.forward(math.cos(i)*500*math.sin(i))
	pen.left(200)
pen.end_fill()

turtle.done()