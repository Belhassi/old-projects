import turtle
import math
import random

pen = turtle.Turtle()
colors = ["red", "green", "yellow", "blue", "pink", "orange", "purple", "black", "brown"]

pen.speed(20)
pen.color("blue", "red")

pen.penup()
pen.goto(190, 0)
pen.pendown()


pen.begin_fill()
for i in range(1000):
	color = random.choice(colors)
	pen.color(color)

	pen.forward(math.sin(i)*(20.98**2)*math.sin(i))
	pen.left(200)
pen.end_fill()

turtle.done()