n = 6001;
bFound = False; # have we found the prime >6000

while bFound==False: # if we have not found it ,continue the search

	#1. TEST if n is a prime number
	iFactors = 0; #how many factors of n
	# LOOP: x from 2 to n-1
	for x in range (2, n): # produces array [2,3,...,n-1]
		if n%x==0: # can divide n?
			iFactors +=1;

	#2. if its a prime, set bFound to true and print it out
	if iFactors==0:
		bFound = True;
		print(n);

	#3. n increaced by 1
	n +=  1;
