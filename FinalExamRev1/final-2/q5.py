# Calculate the sum of all the numbers
# located on the boundary of a matrix of numbers
# Input parameter "filename" is the name of the file that contains the numbers
def getSumBoundary(filename):
	# Your job here
	# Around 15 lines of code
	# if necessary, you can define additional functions
	# before getSumBoundary
	

	f1 = open(filename, "r");
	arrLines = f1.readlines();
	f1.close();

	lineNo = 0;
	sum = 0;
	for line in arrLines:
		if lineNo==0 or lineNo==len(arrLines)-1:
			arrWords = line.split();
			for word in arrWords:
				sum += int(word);
		else:
			arrWords = line.split();
			sum += int(arrWords[0]) + int(arrWords[len(arrWords)-1]);
		
		lineNo += 1;	
		
	return sum;

# ----------------------------------------
# Main program. Do not change.
# ----------------------------------------
for id in range(6):
	fname = "num"+str(id)+".txt";
	mysum = getSumBoundary(fname);
	print(fname + ": " + str(mysum));
		
		
