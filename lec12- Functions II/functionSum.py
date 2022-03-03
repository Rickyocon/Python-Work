#given an array of integers, return the sum
def getSum(arr):
	s = 0;
	for x in arr:
		s += x;
	return s;

#main program

s2 = getSum([1,2]) + getSum([2,3]);
print("s2 is " + str(s2));
		
