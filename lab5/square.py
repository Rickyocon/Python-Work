from turtle import *;
iSize=200;

speed(1000);
for x in range(20):
	setheading(90);
	for x in range(4):
        	forward(iSize);
        	left(90);
	iSize -= 10;

input();
