# Return the n'th number in the fib sequence (1 means the first)
# Parameter arr: is used to store results
# Initially arr[idx] is 0, but once its set, it is the result fib(idx)

def fib(n, arr):
	if n==1 or n==2:
		return 1;
	else:
		if arr[n]!=0:
			return arr[n];
		else:
			res = fib(n-1, arr) + fib(n-2, arr);    # res = Result
			arr[n] = res; # this is the storage used for the storage
			return res;

#-------------------------------------------------------------------------------

# MAIN PROGRAM 
# print out 1000 Fib sequence numbers

arr = [0] * 1001;
for x in range(1,1001):
	res = fib(x,arr); # This is the storage
	print( str(x) + ": " + str(res) );
	
