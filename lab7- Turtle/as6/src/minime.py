from turtle import *;

# draw a circle given the radius
# x, y: CENTER of the circle
# radius: in pixels
speed(500);
def drawCircle(x, y, radius):
	# -----------------------
	# YOUR JOB HERE (challenge 2)
	# -----------------------
	goto(x, y-radius);
	circle(radius);
