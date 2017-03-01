import turtle
def draw_Shapes():

	window = turtle.Screen()
	window.bgcolor("yellow")
	count = 0;
	
	
	sq = turtle.Turtle()
	sq.shape("turtle");
	sq.color("red");
	sq.speed(2);
	while(count<4):
		sq.forward(100)
		sq.right(90)
		count = count + 1
		# sq.forward(100)
		# sq.right(90)
		# sq.forward(100)
		# sq.right(90)
		# sq.forward(100)
		# sq.right(90)


	cir = turtle.Turtle()
	cir.shape("arrow")
	cir.color("blue")
	cir.circle(100)

	tri = turtle.Turtle()
	tri.left(180)
	tri.forward(100)
	
	tri.left(120)
	tri.forward(100)

	tri.left(120)
	tri.forward(100)


	window.exitonclick()
draw_Shapes()
