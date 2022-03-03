n= int(input("Enter: "));
iFactors = 0; #how many factors of n
# LOOP: x from 2 to n-1
for x in range (2, n): # produces array [2,3,...,n-1]
	if n%x==0: # can divide n?
		iFactors +=1;

if iFactors==0:
	print("prime!");
