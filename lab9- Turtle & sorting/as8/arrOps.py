from turtle import *;
from time import *;
import time;

# ---------------------------------------------------
# Function: drawRectangle(...)
# draw a rectangle 
# Its left corner is located at  (x, 0)
# width: 5 pixel
# height is the "height" parameter given
# fill color is the given "sColor"
# ---------------------------------------------------
def drawRectangle(x, height, sColor):
	speed(7000);
	#------------------------
	# your job here!
	width = 5;
	penup();
	goto(x,0);
	pendown();
	pencolor("white");
	fillcolor(sColor);
	begin_fill();
	forward(width);
	left(90);
	forward(height);
	left(90);
	forward(width);
	left(90);
	forward(height);
	left(90);
	end_fill();
 	
	#------------------------

# ---------------------------------------------------
# drawArrElement(...)
# Draw a bar for the i'th element of the given array
# location of the left-bottom corner: (i*10, 0)
# width of the bar: 5 pixel
# height of the bar: arr[i]
# Attention: you need to achieve a FLASHING effect below
#    You should first clear the bar (height 1000) with WHITE color
#    draw the bar in color RED
#    pause for the "pauseTime" seconds
#    draw the bar in color BLACK
# ---------------------------------------------------
def drawArrElement(arr, i, pauseTime):
	#------------------------
	# Your job here
	# STEPS-
	#1) let x be i*10, and let height be arr[i]
	height = arr[i];
	x = i*10;
	#2) draw a rectangle at (x,0), with height 1000, with "white" as the fill color
	drawRectangle(x, 1000, "white");
	#3) draw a rectangle at (x,0), with heigth set to "height" var, with "red"
	drawRectangle(x, height, "red");
	#4) sleep for pauseTime seconds
	sleep(pauseTime); #sleep for 3 seconds
	#5) draw a rectangle at (x,0), with "height" var as the height, with "black"
	drawRectangle(x, height, "black");  
	#------------------------
	return drawArrElement;

# -----------------------------------------------------
# draw an entire array by calling drawArrElement(...)
# -----------------------------------------------------
def drawArr(arr):
	#------------------------
	# You job here
	# STEPS-
	#1) n = len(arr)
	n = len(arr); 
	#2) LOOP: i will be from 0 --> n-1
	for i in range(0, n-1):
		#3) drawArrElement(____, _____, 1)
		drawArrElement(arr, i, 1); 
	#------------------------
	return drawArrElement;

# -----------------------------------------------------
# set the value of element located at index i of the array
# draw the write operation
# -----------------------------------------------------
def setArrElement(arr, i, val): 
	#------------------------
	# You job here
	# STEPS-
	#1) arr[i] = val;
	arr[i] = val;
	#2) call drawArrElement(_____, ______, _____) ( arr name, index, pauseTime)
	drawArrElement(arr, i, 1); 
	#------------------------
	return setArrElement;
