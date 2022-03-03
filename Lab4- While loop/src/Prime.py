n = int(input("Enter n: "));
iFactors = 0;
x = 2;
while x<= n-1:
	if n%x==0:
		iFactors +=1;
	x += 1;
if iFactors == 0:
	print(str(n) + " is prime");

