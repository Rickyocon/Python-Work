# print a triangle of size n
# shift it nShiftRight positions to the right
def prtTri2(n, nShiftRight):
	if n==0:
		return;
	else:
		prtTri2(n-1, nShiftRight+1);
		print(" "*nShiftRight + "*"*(2*n-1) );

#------------------------------------------------------
#MAIN PROGRAM
prtTri2(10, 5);
