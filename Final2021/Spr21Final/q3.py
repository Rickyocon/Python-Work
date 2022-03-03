def prtNumTri(n):
	if n==1:
		print(1);
		return 1;
	else:
		lastNum = prtNumTri(n-1);
		sline = "";
		num = lastNum + 1;
		for x in range(n):
			sline += str(num) + " "; 
			num = num + 1;
		print(sline);
		return lastNum + num;

# main program
n = int(input("Enter triangle size: "));
prtNumTri(n);
