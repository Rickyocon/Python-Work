# this function returns True if n is a square number (e.g., 4, 9, 16)
# otherwise return False
def isSquare(n):
	# you need around 3 lines below
	# if you need more lines that is ok
	for x in range(n):
		if x*x == n:
			return True;
		if x*x>n:
			return False;
	return False;

# This function returns how many numbers
# contained in arr are square numbers
def countPerfectSquares(arr):
	# you need around 5 lines below
	# if you need more lines that is ok
	count = 0;
	for u in arr:
		if isSquare(u) == True:
			count += 1;
	return count;


# -------------------------------------------
# main program - do not touch
# -------------------------------------------
def handleFile(filename):
	f1 = open(filename, "r");
	s1 = f1.read();
	f1.close();
	arrWords = s1.split();
	arr = [];
	for x in arrWords:
		arr.append(int(x));
	res = countPerfectSquares(arr);
	return res;

arrFiles = ["num1.txt", "num2.txt", "num3.txt", "num4.txt"];
for fname in arrFiles:	
	res = handleFile(fname);
	print(fname + ": " + str(res));

