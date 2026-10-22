import turtle
import random

pen = turtle.Turtle()
colors = ["red", "green", "yellow", "blue", "pink", "orange", "purple", "black", "brown"]

pen.speed(20)
pen.color("orange", "red")

pen.penup()
pen.goto(-140, -60)
pen.pendown()

for i in range(9):
	color = random.choice(colors)
	pen.color(color)

	for i in range(40):
		pen.forward(100)
		pen.left(170)

	pen.forward(200)
	for i in range(40):
		pen.forward(100)
		pen.left(170)

	pen.right(200)
turtle.done()