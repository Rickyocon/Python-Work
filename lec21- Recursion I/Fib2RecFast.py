# Return thr n'th fib number, n>=1
def fib(n):
	if n==1 or n==2:
		return 1;
	else:
		#return fib(n-1) + fib(n-2);

		n2 = 1; # Two positions before me 
		n1 = 1; # Fib number RIGHT BEFORE me
		for x in range(n-2):
			res = n1 + n2;
			n2 = n1;
			n1 = res;
		return res;
#-------------------------------------------------------
# MAIN PROGRAM
n = int(input("Enter n: "));
for x in range(1, n+1):
	print(str(x) + ": " + str( fib(x) ));
