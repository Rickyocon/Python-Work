# remove all characters that are not alphanumerical
# e.g., given string "abc.!abc", it returns "abc abc"
def stripNonAlphaNumeric(s):
	import re;
	return re.sub(r'([^\s\w]|_)+', '', s)

# Given the name of a file, returns the average word length
# White spaces and punctuations should not be counted as a part of a word
def getAvgWordLen(filename):
	# Your job here: around 10 lines of code
	# Don't forget to call stripNonAlphaNumeric(s)
	
	#Read The File
	f1 = open(filename, "r");
	s1 = f1.read();
	f1.close;

	#Get the average word length
	s2 = stripNonAlphaNumeric(s1);
	arrWords = s2.split();
	sum = 0;
	for word in arrWords:
		sum += len(word);
		avg = sum/len(arrWords);
	return avg;
# ---------------------------------
# Main Program. Do not change the following.
# ---------------------------------
arrFiles = [
	"test.txt",
	"AdvHuckFinn",       
	"LifeOnMiss", 
	"GreatExpectation",
	"OliverTwist",  
	"HardTime",
	"Yankee"
];
for fname in arrFiles:
	avgWordLen = getAvgWordLen(fname);
	print(fname + ": " + str(avgWordLen));
	

