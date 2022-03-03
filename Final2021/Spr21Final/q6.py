def hasMagicSum(arr, goal):
	#-------------------------------------
	# Your job below (need to be FAST!)
	#-------------------------------------
	return False;




#------------------------------------
# Main Program. Don't change
#------------------------------------
f1 = open("numbers.txt", "r");
s1 = f1.read();
f1.close();
arrNums = [];
for x in s1.split():
	arrNums.append(int(x));

goals= [160173909, 8658449, 63119213, 92734901, 98364118, 10988265, 52001284, 10351046, 2167742, 28029619];
for goal in goals:
	print(goal, ":", hasMagicSum(arrNums, goal));
