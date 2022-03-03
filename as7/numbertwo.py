from turtle import *;

# draw a bar chart of given array
# the width of each bar should be 5 pixels
# the space between each two bars should be 2 pixels
# the height of each bar is the VALUE of the element in the array
def drawBarChart(arr):
	#LOOP: for each element x in the array
	for x in arr:
		#1.) set the fill color and begin fill
		fillcolor("black");
		begin_fill();
		#2.) DRAW a rectangel: width is 5, height is x
		forward(5);
		left(90);
		forward(x);
		left(90);
		forward(5);
		left(90);
		forward(x);
		left(90);
		#3.) end fill
		end_fill();
		#4.) MOVE FORWARD 7 pixals.
		forward(7);
		
