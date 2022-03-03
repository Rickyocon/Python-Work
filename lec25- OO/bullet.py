from turtle import *;
from GraphicObj import *;

class Bullet(GraphicObj):
	def __init__(self, xin, yin, sxin, syin, scolor):
		GraphicObj.__init__(self, xin, yin, sxin, syin);
		self.scolor = scolor;

	# No need for update(), from GraphicObj

	def draw(self):
		speed(5000);
		penup();
		goto(self.x , self.y);
		pendown();
		fillcolor(self.scolor);
		begin_fill();
		circle(10);
		end_fill();

#-----------------------------------------------------------------------
# TEST
b1 = Bullet(100, 100, 10, 0, "blue");
b1.update();
b1.draw();
