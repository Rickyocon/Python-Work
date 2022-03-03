from turtle import *;

# draw a circle given the radius
# x, y: CENTER of the circle
# radius: in pixels
def drawCircle(x, y, radius):
	speed(1000);
	penup();
	goto(x, y-radius);
	setheading(0);
	pendown();
	circle(radius);
	return 1;

# draw a rectangle.
# x, y: the coordinates of the CENTER of the rectangle
# penColor, fillColor: strings like "#FF0000"
# width, height: in pixels
def drawRectangle(x, y, penColor, fillColor, width, height):
	speed(1000);
	penup();
	goto(x-width/2, y-width/2);
	heading = 0;
	pendown();
	pencolor(penColor);
	fillcolor(fillColor);
	begin_fill();
	for c in range(4):
		setheading(heading);
		heading += 90;
		if c%2==0:
			forward(width);
		else:
			forward(height);	
	end_fill();
	penup();
	return 1;
