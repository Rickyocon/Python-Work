# This is a procedure! It does not return any data!
# Given n, print sequence n, n-1, n-2, .... , 1
def lazyPrint(n):
	if n==0: # the base case
		# do nothing
		return;	
	else: # the recursive case
		print(n);
		n -= 1;
		lazyPrint(n);

lazyPrint(5);

# The output should be
# 5
# 4
# 3
# 2
# 1
