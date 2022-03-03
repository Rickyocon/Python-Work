n = int(input("Enter n: "));
iStars = n;
iCounter = 1;
while iCounter<=n:
	print(iStars*"*");
	iStars -= 1;
	iCounter += 1;
