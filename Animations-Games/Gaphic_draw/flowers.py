import turtle
import math

wn = turtle.Screen()
pen = turtle.Turtle()
wn.title(" flower")
pen.speed(24)


def reset(pos):
	pen.penup()
	pen.goto(pos[0], pos[1])
	pen.pendown()

def drawsSun(size):
	pen.color("#bfff00", "#bfff00")
	reset((-(size/2), 0))

	for i in range(20):
		pen.forward(size-20)
		pen.left(170)
	
	pen.right(162)
	pen.setheading(0)

def flow():
	pen.width(2)

	pen.color("red", "#950000")
	reset((208, 0))

	for i in range(600):
		pen.forward(math.cos(i)*545.98*math.sin(i))
		pen.left(170)
	pen.end_fill()

drawsSun(100)
flow()

turtle.done()