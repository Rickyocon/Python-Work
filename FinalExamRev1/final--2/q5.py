# Calculate the sum of all the numbers
# located on the boundary of a matrix of numbers
# Input parameter "filename" is the name of the file that contains the numbers
def getSumBoundary(filename):
	# Your job here
	# Around 15 lines of code
	# if necessary, you can define additional functions
	# before getSumBoundary
	
	# Raed the file
	f1 = open(filename, "r");
	s1 = f1.readlines();
	f1.close();
	
	
	
		















# ----------------------------------------
# Main program. Do not change.
# ----------------------------------------
for id in range(6):
	fname = "num"+str(id)+".txt";
	mysum = getSumBoundary(fname);
	print(fname + ": " + str(mysum));
		
		
