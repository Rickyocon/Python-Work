# This is a procedure! It does not return anything!
# The function prints a triangle of the given "size"
#   AND it shifts the entire triangle to the right for "nShiftRight"
def printTri(nShiftRight, size):
	if size==0:
		return;
	else:
		print(" "*nShiftRight + "*"*size);
		nShiftRight += 1;
		size -= 1;
		printTri(nShiftRight, size);

printTri(0, 4);
# Output should be
# ****
#  ***
#   **
#    *
