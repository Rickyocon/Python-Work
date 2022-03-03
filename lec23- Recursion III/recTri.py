def printTri(n):
	if n==0:
		return;
	else:
		print("*"*n);
		printTri(n-1);
#---------------------------------
# MAIN PROGRAM
n = int(input("Enter a number: "));
printTri(n);
