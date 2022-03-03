def findWord(arrWords, word):
	arrRet = [];
	for x in range(len(arrWords)):
		if arrWords[x]==word:
			arrRet.append(x);
	import random;
	if(len(arrRet)==0): return -1;
	il = len(arrRet);
	return arrRet[random.randint(0, il-1)];	

# main program
f1 = open("hamlet.txt", "r");
arrWords = f1.read().split();
f1.close();
f2 = open("secret.txt", "r");
f3 = open("encoded.txt", "w");
arrlines = f2.readlines();
for line in arrlines:
	arr = line.split();
	sPrint= "";
	for x in arr:
		num = findWord(arrWords, x);
		sPrint += str(num) + " ";
	f3.write(sPrint+"\n");
f3.close();
f2.close();
	

