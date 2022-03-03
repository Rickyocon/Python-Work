# Print array in reverse order, void function!
def printRev(arr):
	if len(arr)==0:
		return;
	else:
		print( arr[len(arr)-1] );
		printRev( arr[0: len(arr)-1] );
#----------------------------------------------------
#MAIN PROGRAM
arr1 = [1, 2, 5, 7];
print(printRev(arr1));
