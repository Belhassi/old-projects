import turtle
import math

wn = turtle.Screen()
wn.title("Morocco")

pen = turtle.Turtle()
wn.bgcolor("green")

pen.speed(14)
pen.color("red", "black")
pen.width(3)

def star(pen, leg):
	for i in range(5):
		pen.begin_fill()
		pen.forward(leg)
		if leg > 10:
			star(pen, leg/3)
		else:
			return
		pen.left(216)
		pen.end_fill()

size = 400
pen.penup()
pen.goto(-(size/2), 0)
pen.pendown()

star(pen, size)
pen.penup()

turtle.done()