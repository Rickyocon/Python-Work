sText = "I love Hofstra. I like computer science. I like programing. I love to hangout as well. I really like people";
# 1.) How many words?
arr = sText.split();
print("The word count is " + str(len(arr)));

# 2.) average of word length?
totalLen = 0; # sum of the word length
for word in arr:
	totalLen += len(word);
avg = totalLen/len(arr);
print("And the average word length is " + str(avg));

# Return how many times sWord appears in sText
def countKeyword(sText, sWord):
	arr = sText.split();
	iCounter = 0;
	for word in arr:
		if word==sWord:
			iCounter += 1;
	return iCounter;

# Main program
iTimes = countKeyword(sText, "people");
print("People appears " + str(iTimes) + " times");
