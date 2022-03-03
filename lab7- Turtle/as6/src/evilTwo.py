from numbertwo import *;
def decoTwo():
	for row in range(10):
		for col in range(10):
			fillColor = "#000000";
			if (row+col)%2==0:
				fillColor = "#FFFFFF";
			drawRectangle(col*10, row*10, "#000000", fillColor, 10, 10);
decoTwo();
input();
