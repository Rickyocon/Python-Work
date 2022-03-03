from numbertwo import *;
def decoThree():
	# ---------------------------------
	size = 500;
	penup();
	goto(-250, -250);
	pendown();
	for x in range(50):
		fillColor = "black";
		if x%2==1:
			fillColor = "white";
		drawRectangle(0, 0, "#000000", fillColor, size, size);
		size -= 10;
	#-----------------------------------
decoThree();
input();
