# Print a triangle of n rows
def printTri(n):
	if n==0:
		return; # Do nothing
	else:
		printTri(n-1);
		print("*" * n);
#----------------------------------------

#MAIN PROGRAM
printTri(20);
