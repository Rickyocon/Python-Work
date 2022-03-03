from Tank import *;
from bullet import *;
from time import *;

# MAIN PROGRAM
arr = [Tank(100, 100, 1, 0, "blue"), Bullet(200, 200, 5, 5, "red")];
screen = Screen();
for ticks in range(1000):
	sleep(0.05);
	screen.clear();
	screen.tracer(0);
	for obj in arr:
		obj.update();
		obj.draw();
	screen.update();
