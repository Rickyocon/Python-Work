class GraphicObj:
	def __init__(self, xin, yin, sxin, syin): # s stands for speed
		self.x = xin;
		self.y = yin;
		self.sx = sxin; # speed on x axis
		self.sy = syin;

	def update(self):
		self.x += self.sx;
		self.y += self.sy;
 
