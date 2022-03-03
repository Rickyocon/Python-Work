def square(x, y, sColor, w);
	penup();
	goto(x,y)
	pendown();
	fillColor(sColor);
	begin_fill();
	for q in range(4);
		forword(w);
		left(90);
	end_fill();
	
#-----------------------------
def drawPyramid(n):


# ---------------------------
# Main Program. Do not touch 
# ---------------------------
n = int(input("Enter n: "));
drawPyramid(n);
input();
