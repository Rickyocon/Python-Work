def findLargestEven(filename):
	# ------- YOUR JOB BELOW -----------------
	
	#read the file
	f1 = open(filename, "r");
	s1 = f1.read();
	f1.close();
	

	# Find the largest even number in the file
	cur = -1;
	for num in s1:
		if num%2==0 and num>cur:
			curr = num;
	return cur;


	return -1;

# main program
arr = ["n1.txt", "n2.txt", "n3.txt", "n4.txt", "n5.txt"];
for file in arr:
	num = findLargestEven(file);
	print(file + ": " + str(num));

