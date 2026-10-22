import turtle
import math
import random

pen = turtle.Turtle()
pen.getscreen().bgcolor("#BC4848")

pen.speed(14)
pen.color("black", "red")

for i in range(800):
	pen.forward(random.randint(1, 100))
	pen.left(90)

turtle.done()