def getSum(arr):
	sum = 0;
	for x in arr:
		sum += x;
	return sum;

# Return the largest number in the array
# arr is an array of numbers and len(arr)>0
def getMax(arr):
	max = arr[0];
	for x in arr:
		if x>max:
			max = x;
	return max;

# read an ARRAY of NUMBERS out of the file
def readArrInt(filename):
	f1 = open(filename, "r");
	s1 = f1.read(); # READING THE ENTIRE FILE CONTENT
	arr1 = s1.split();

	arr2 = [];
	for x in arr1:
		ix = int(x);
		arr2.append(ix);
	return arr2;

#MAIN PROGRAM
arr = readArrInt("numbers.txt");
iSum = getSum(arr);
iMax = getMax(arr);
print("max: " + str(iMax) + ", sum: " + str(iSum));




