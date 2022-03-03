# return the LAST LONGEST word in the file
def getLastLongestWord(filename):
	
	# Read the file!
	f1 = open(filename, "r");
	s1 = f1.read();
	f1.close();
	
	# Find the longest word
	longestWord = "";
	arrWords = s1.split();
	for word in arrWords:
		if len(word)>=len(longestWord):
			longestWord = word;
	return longestWord;
			

# ---------------------------------
# MAIN PROGRAM. Do not touch
# ---------------------------------
arr = ["Yankee", "HardTime", "GreatExpectation"];
for fname in arr:
    word= getLastLongestWord(fname);
    print(fname + ": " + word);
