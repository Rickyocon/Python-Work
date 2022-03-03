# return sum of numbers
def getSum(arr):
	sum = 0;
	for x in arr:
		sum += x;
	return sum;

#-----------------------------------------------------

# return an array of 26 charactors
def getFreq(sText):
	# 1). build up 26 number array
	arr = [];
	for x in range(26):
		arr.append(0);
	
	# 2). process letter by letter
	sText = sText.lower(); # convert to lower case letters
	for letter in sText:
		if letter>="a" and letter<="z":
			idx = ord(letter) - ord("a");
			arr[idx] += 1;
	# 3). Done
	return arr;

#----------------------------------------------------

# Print the frequency of the array
def printFreq(arr):
	# 1). get the sum
	sum = getSum(arr);
	
	# 2). print each line
	ordCh = ord("a"); # ordCh stands for order of charactor
	for x in arr:
		freq = x/sum; # Floating point number
		sPerc = str(freq*100) + "%";
		ch = chr(ordCh);
		ordCh += 1;
		print(ch + ": " + sPerc);
#-----------------------------------------------------

#Main program
f1  = open("ind.txt", "r");
s1 = f1.read();
f1.close();
arr = getFreq(s1);
printFreq(arr);






