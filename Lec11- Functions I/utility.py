#tell if n is a prime number
#i.e , returns True if n is prime;
#otherwise returns False
def isPrime(n):
	if n==2:
		return True;
	for x in range(2,n):
		if n%x==0:
			return False;
	return True;
