from utility import*;

# main program (using function call)
b1 = isPrime(11);
print("11 is prime: " + str(b1));

bFound = False;
n = 6001;
while bFound==False:
	if isPrime(n):
		bFound = True;
		print(n);
	else:
		n = n + 1;
