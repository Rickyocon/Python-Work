# counter loop: n from 1 to 27
n = 1;
while n<=27:
	iStars = n;
	iCounter = 1;
	while iCounter<=n:
		print(iStars*"*");
		iStars -= 1;
		iCounter += 1;
	n += 1;
