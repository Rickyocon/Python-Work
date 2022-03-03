# Print out all the magic sequence numbers below 10000
# Note: you can only complete the blank lines
# Please do not change other parts of this program.

numToPrint = 1; # number to print
diff = 0; # difference between each pair of numbers
while  numToPrint<10000:
	print(numToPrint);
	diff = diff + 1;
	numToPrint += diff;
	

