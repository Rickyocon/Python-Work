#return the largest out of three numbers
def getLargest(n1, n2, n3):
	if n1>=n2 and n1>=n3:
		return n1;
	elif n2>=n3 and n2>=n1:
		return n2;
	else:
		return n3;

#----------------------------------------------------------
def getSum(arr):
	s = 0;
	for x in arr:
		s += x;
	return s;
#-----------------------------------------------------------

#-----------------------------------------------------------
#report factorial of n
def factorial(n):
	if n==1:
		return 1;
	else:
		return n * factorial(n-1);
#-----------------------------------------------------------

#-----------------------------------------------------------
# Question: what if you have 100 numbers(or parameters)?
# Answer: we could use an Array!

#Find the max number of a given array
def getMax(arr):
	maxSoFar = arr[0]; 
	for x in arr:
		if x>maxSoFar:
			maxSoFar = x;
	return maxSoFar;
#-----------------------------------------------------------

#-----------------------------------------------------------
#main program
s2 = getSum([1,2]) + getSum([2,3]);
print("s2 is " + str(s2));
print("Max of arr is: " + str(getMax([10, 30, 20])));
print("Factorial of 4 is " + str(factorial(4)));
