from turtle import *;

# draw a rectangle.
# x, y: the coordinates of the CENTER of the rectangle
# penColor, fillColor: strings like "#FF0000"
# width, height: in pixels
def drawRectangle(x, y, penColor, fillColor, width, height):
	# -----------------------------------
	# Your job here (challenge 3)
	# -----------------------------------
	speed(1000);
	penup();
	goto(x-width//2, y-height//2);
	pendown();
	fillcolor(fillColor);
	begin_fill();
	for x in range(2):
		forward(width);
		left(90);
		forward(height);
		left(90);
	end_fill();


		
		
		
	
	
	
