from turtle import *;
from GraphicObj import *;

#-----------------------------------------------------------------------
def rect(x, y, w, h, scolor):
	# Draw a rectangle at (x,y) as left-bottom corner with (w,h) as width and height
	speed(5000);
	penup();
	goto(x,y);
	pendown();
	
	fillcolor(scolor);
	begin_fill();
	for u in range(2):
		forward(w);
		left(90);
		forward(h);
		left(90);
	end_fill();

#-----------------------------------------------------------------------
class Tank(GraphicObj):
	def __init__(self, xin, yin, sxin, syin, scolor):
		GraphicObj.__init__(self, xin, yin, sxin, syin);
		self.scolor = scolor;

	# No need for update(), from GraphicObj

	def draw(self):
		rect(self.x, self.y, 50, 50, "red");
		rect(self.x+25, self.y+25, 100, 5, "yellow");


#-----------------------------------------------------------------------
# TEST
t1 = Tank(100, 100, 0, 5, "yellow");
t1.update();
t1.draw();

