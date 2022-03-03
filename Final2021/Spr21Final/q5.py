n = int(input("Enter n: "));
from turtle import *;
# Your job below (around 30 lines)
# -----------------------------------------------
def square(x, y, w):
	speed(5000);
	penup();
	goto(x, y);
	pendown();
	begin_fill();
	for q in range(4):
		forward(w);
		left(90);
	end_fill();

def triangleOfSquares(u):
	nSquares = 1;
	startX = 0;
	startY = 0;

	for squareId in range(nSquares):
		if squareId%2==1:
			
				
