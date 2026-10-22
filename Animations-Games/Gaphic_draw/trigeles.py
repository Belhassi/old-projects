import turtle

pen = turtle.Turtle()
pen.speed(20)
pen.color("black", "black")

pen.penup()
pen.goto((-80, 0))
pen.pendown()

def tri():
	pen.begin_fill()
	for i in range(4):
		pen.forward(120)
		pen.left(170)
	pen.end_fill()

for i in range(45):
	pen.forward(123)
	tri()
	pen.left(144)

turtle.done()