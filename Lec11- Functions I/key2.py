#tell if n is a prime number
#i.e , returns True if n is prime;
#otherwise returns False
def isPrime(n):
	if n==2:
		return True;
	#use the sieve method
	#to test each x from 2..n-1


	#------------------------------
	#slow version

	#iFactors = 0;
	#for each x in range(2,n):
		#if n%==0:
			#iFactors +=1;
	#if iFactors==0:
		#return True;
	#else:
		#return False;


	#------------------------------
	#fast version

	for x in range(2,n):
		if n%x==0:
			return False;
	return True;


#--------------------------------------
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
