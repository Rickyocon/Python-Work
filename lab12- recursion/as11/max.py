# This is a function!
# It returns the max of arr[0], arr[1], ..., arr[rightEnd]
def getMax(arr, rightEnd):
	if rightEnd==0: # base case
		return arr[0];
	else:
		partial = getMax(arr, rightEnd-1);
		lastEle = arr[rightEnd];
		if partial>lastEle:
			return partial;
		else:
			return lastEle;

arr1 = [1, 3, 5, 2];
max = getMax(arr1, len(arr1)-1);
print("The max is " + str(max));

# output should be 5
