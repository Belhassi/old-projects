import turtle
import math

pen = turtle.Turtle()
pen.speed(20)
pen.color("black", "red")
pen.width(3)

def draw(color):
	pen.begin_fill()
	pen.left(120)
	for i in range(120):
		print(i)
		pen.right(2)
		pen.forward(10)
	pen.end_fill()

turtle.done()