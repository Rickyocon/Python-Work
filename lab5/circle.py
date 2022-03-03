from turtle import *;
iRadious=10;
y=0;

speed(1000);
for x in range(20):
	goto(0,y);
	circle(iRadious);
	y -= 10;
	iRadious += 10;

input();
