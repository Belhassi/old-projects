import turtle
import math

pen = turtle.Turtle()
pen.speed(20)
pen.color("black", "red")

pen.begin_fill()
for i in range(5000):
	pen.forward(math.sqrt(i))
	pen.left(i%180)

pen.end_fill()
turtle.done()