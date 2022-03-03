from turtle import *;

# Loop: 9 times (for drawing 9 rows)
speed(500);
for row in range(9):
	# Draw a row: loop 9 times: draw 9 cells
	for col in range(9):
		# 1.) determine the fill color
		if (row+col)%2==1:
			sColor = "black";
		else:
			sColor = "white";

		# 2.) draw a square given the color
		x = col * 10;
		y = row * 10;
		penup();
		goto(x,y);
		pendown();

		fillcolor(sColor);
		begin_fill();
		for side in range(4):
			forward(10);
			left(90);
		end_fill();

input();
	
