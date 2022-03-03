# if n does not exsit return -1
# otherwise return the idx s.t. arr[idx]=n
# assumption: arr is sorted in ascending order 
def binSearch(arr, n):
	if len(arr)==0:
		return -1;
	else:
		midPos = len(arr)//2;
		if arr[midPos] == n:
			return midPos;
		else if arr[midPos]>n:
			return binSearch(arr[0:midPos-1], n);
		else:
			return binSearch(arr[midPos+1:len(arr], n);
midPos + 1;

#--------------------------------------------------------------------
#MAIN PROGRAM
arr = [1, 3, 5, 7, 9];
for x in arr:
	idx = binSearch(arr, x);
	print(str(x) + " appears at " + str(idx));
