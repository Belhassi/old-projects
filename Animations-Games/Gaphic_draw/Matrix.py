import turtle
import math

pen = turtle.Turtle()
pen.speed(50)
pen.color("black", "red")

pen.begin_fill()


for i in range(3000):
	pen.forward((i**1.444444444444449999999999999994444444444444444444449999999))
	pen.left(170)
	
pen.home()
pen.clear()
	

pen.end_fill()

turtle.done()