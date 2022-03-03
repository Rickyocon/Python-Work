# return the sum of of an array of integers
def getSum(arr):
	sum = 0;
	for x in arr:
		sum += x;
	return sum;

# return the number of odd numbers in an array
def getCountOdd(arr):
	iCounter = 0;
	for x in arr:
		if x%2==1:
			iCounter+=1;
	return iCounter;

# return the max of an array of numbers
def getMax(arr):
	max = arr[0];
	idx = 0;
	for x in arr:
		if x > max:
			max = x;	
	return max;

# return the average (must be a float point number) of an array of numbers
def getAvg(arr):
	sum = getSum(arr);
	avg = sum/len(arr);
	return avg;

# return a new array which is a REVERSE of the original array
def getReverse(arr):
	#1.) declare arr2 as an empty array
	arr2 = [];
	#2.) declare idx as an integer value and initilaize it with len(arr)-1
	idx = len(arr)-1;
	#3.) FOR LOOP: len(arr) times
	for x in range(len(arr)):
		#4.) do the append: read arr[idx] and append it to arr2
		arr2.append(arr[idx]);
		#5.) idx decreased by 1
		idx -= 1;
	return [arr2]; 

# return True if the given array is in ascending order
def isAscending(arr):
	n = len(arr);
	idx1 = 0;
	idx2 = 1; 
	for x in range(n-1):
		if arr[idx1]>arr[idx2]:
			return False;
		idx1 += 1;
		idx2 += 1;
	return True;
		

