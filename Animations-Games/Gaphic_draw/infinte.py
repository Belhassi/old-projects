import turtle
import math

wn = turtle.Screen()
pen = turtle.Turtle()
wn.title("Infinte Paradox")
pen.speed(14)

pen.left(30)

pen.begin_fill()
for i in range(40):
	pen.left(i)

	for j in range(10):
		pen.forward(j**i)
		pen.left(90)
pen.end_fill()

turtle.done()