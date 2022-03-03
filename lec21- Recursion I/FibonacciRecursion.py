# Return the n'th number in Fib. sequence
# n>=1
def fib(n):
	if n==1 or n==2:
		return 1;
	else:
		return fib(n-1) + fib(n-2);

# MAIN PROGRAM
n = int(input("How many Fib numbers to print? "));
for x in range(1, n+1):
	print( str(x) + ": " + str( fib(x) ) );
