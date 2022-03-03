import re;

#------------------------------------------------------------------------------

# Return an array of strings
# Each element is a DATA CELL'S value 
def extractCells(sRec):
	r1 = re.compile("<td.*?>(.*?)</td>");
	arr = r1.findall(sRec);
	return arr;
#------------------------------------------------------------------------------
# Construct a set out of an array                                                 
# Each element should appear once in the output                                   
def getset(arr):
	arrRet = [];
	for x in arr:
		if not(x in arrRet):
			arrRet.append(x);
	return arrRet;

#-------------------------------------------------------------------------------

# Read the given file and return an array of strings (course records)
def extractCourse(filename):
	#1. Read the file
	f1 = open(filename, "r");
	s1 = f1.read();
	f1.close();

	#2. Do the search
	r1 = re.compile("<tr.*?section_row.*?</tr>", re.MULTILINE|re.DOTALL);
	arr = r1.findall(s1);

	#3. arr2 = []  (This is a new array)
	arr2 = [];

	#4. For each sRec in arr, if it's major code
	# If its NOT "&nbsp;", append it to arr2
	for sRec in arr:
		arrCells = extractCells(sRec);
		majorCode = arrCells[2];
		if majorCode!="&nbsp;":
			arr2.append(sRec);

	return arr2;

#-------------------------------------------------------------------------------------
# Return how many majors are offered at hofstra 
# MAJOR CODE- ACCT, and CSC ( Look for those in the html file)
def extractMajors(arr):
	arrMajor = [];
	for sRec in arr:
		arrCells = extractCells(sRec);
		major = arrCells[2];
		arrMajor.append(major);
	setMajor = getset(arrMajor);
	return setMajor;
#--------------------------------------------------------------------------------------
def getTuition(arr):
	sum = 0;
	for sRec in arr:
		arrCells = extractCells(sRec);
		#print(arrCells);
		numS = float(arrCells[9]);
		numC = float(arrCells[6]);
		#print(numS, numC);
		total = numS * numC * 1380;
		sum += total;
	return sum;


#--------------------------------------------------------------------------------------
# MAIN PROGRAM
arr2 = extractCourse("hofstra.html");
arr3 = extractMajors(arr2);
Total = getTuition(arr2);
#print(arr2[10]);
print(len(arr2),"Courses");
print(len(arr3),"Majors");
print(Total,"Dollars");
