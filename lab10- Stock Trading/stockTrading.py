#----------------------------------------------------------------------------------

# get a REVERSE COPY  of the given array
def getReverse(arr):
	#1. Declare arr2 as an EMPTY array
	arr2 = [];
	#2. declare idx  = len(arr) -1
	idx = len(arr)-1;
	#3. FOR LOOP: idx from len(arr)-1 to 0
	for not_used in arr:
		#4. Append arr[idx] to arr2
		arr2.append(arr[idx]);
		idx -= 1;
	#5. Return arr2
	return arr2;

#----------------------------------------------------------------------------------

# Read the GIVEN file and return a 2D array
# Sorted by DATE
def readData(filename):
	#1. read ALL lines into arrLines
	f1 = open(filename, "r");
	arrLines = f1.readlines();
	f1.close();
	#2. CHOP OFF the first ELEMENT of arrLines
	arrLines = arrLines[1: len(arrLines)];
	#3. declare arr2 as EMPTY ARRAY 
	arr2 = [];
	#4. FOR EACH LINE IN arrLines
	for line in arrLines:
		#5. use split to get: sDate, and fPrice
		arrWords = line.split(",");
		sDate = arrWords[0];
		fPrice = float(arrWords[1]);
		#6. build a rec = [sDate, fPrice] ==> (rec means record)
		rec = [sDate, fPrice];
		#7. append rec to arr2
		arr2.append(rec);
	#8. arr3 is the REVERSED COPY  of arr2
	arr3 = getReverse(arr2)
	#9. Return arr3
	return arr3;

#----------------------------------------------------------------------------------------

# Calculate 10 day average given INDEX i of the day
def get10DayAvg(data, i):
	#1. If i is 0: return data[0][1]
	if i==0:
		return data[0][1];
	#2. if i<10:
	if i<10:
		#3. set idxStart to 0 and idxEnd to i-1
		idxStart = 0;
		idxEnd = i-1;
	#4. if i>=10:
	if i>=10:
		#5. set idxStart to i-10 and idxEnd to i-1
		idxStart = i-10;
		idxEnd = i-1;
	#6. sum = 0, days = idxEnd - idxStart + 1
	sum = 0;
	days = idxEnd - idxStart + 1;
	#7. FOR LOOP: summing up ALL price from idxStart to idxEnd
	for idx in range(idxStart, idxEnd+1):
		#8. sum += data[idx][1]
		sum += data[idx][1];
	#9. return sum/days
	return sum/days;

#------------------------------------------------------------------------------------------

# Back test the algrotihm over 2-d array
def backTest(data, perc, initFund): # Data is the 2-d array
	#1. Reset perc = perc/100.0
	perc = perc/100.0;

	#2. init portfolio variables
	# fCash = initFund
	fCash = initFund;
	#iShares = 0
	iShares = 0;
	# n = len(data) # This is HOW MANY BUISNESS DAYS in data
	n = len(data); 

	#3. FOR EACH DAY IN HISTORICAL DATA
	for i in range(n):
		#3.1 Let rec = data[i]
		rec = data[i];
		#3.2 Price = rec[1], sDate = rec[0]
		price = rec[1];
		sDate = rec[0];
		#3.3 avg = get10DayAvg(data, i); #Data is the array, i is index
		avg = get10DayAvg(data, i);
		#3.4 if price>(1-perc)*avg:           # Buy!
		if price<(1-perc)*avg: 
			# iToBuy = int( fCash/price )
			iToBuy = int(fCash/price);
			# iShares += iToBuy 	
			iShares += iToBuy;
			#fCash -= iToBuy * price
			fCash -= iToBuy * price;
			if iToBuy>0:
				print(sDate, "Buy: ", iToBuy, "shares for ", fCash,"dollars","//", "Stock average:",avg,"//","Stock price:",price);
			
		#3.5 if price>(1+perc)*avg: # SELL ALL!
		if price>(1+perc)*avg:
			# iToSell = iShares
			iToSell = iShares;
			# iShares = 0
			iShares = 0;
			# fCash += price * iToSell
			fCash += price * iToSell;
			if iToSell>0:
				print(sDate, "Sell: ", iToSell, "shares for: ", fCash,"dollars","//", "Stock average:",avg,"//","Stock price:",price);

	# OUT OF LOOP BUT STILL IN THE FUNCTION!
	fLastPrice = data[len(data)-1][1]; # The price of last day
	asset = fCash + fLastPrice * iShares;
	return asset;

#-------------------------------------------------------------------------------------------------

# MAIN PROGRAM
#print(readData("GOOG.csv"));

#--------------------------------------------------------------------------------------------------

# MAIN PROGRAM
data = readData("GOOG.csv");
avgLast = get10DayAvg(data, len(data)-1);

#--------------------------------------------------------------------------------------------------

# MAIN PROGRAM
data = readData("GOOG.csv");
initFund = 10000.0
total = backTest(data, 1.0, initFund);
profit = (total- initFund)/ initFund*100.0;

#--------------------------------------------------------------------------------------------------

# MAIN PROGRAM
data = readData("GOOG.csv");
perc = 0.1;
bestPerc = 0.1;
maxAsset = 0;
while perc <= 10.0:
	asset = backTest(data, perc, 10000);
	if asset > maxAsset:
		bestPerc = perc
		maxAsset = asset 
	perc += 0.1;
profit2 = (maxAsset- initFund)/ initFund*100.0;

#----------------------------------------------------------------------------------------------------
# Print statments

print("-----------------------------------------------------------------------------------------------------------------------------");
print("The 10-day Avg for last day is: " + str(avgLast));
print("Your Profit is " + str(profit) + "%");
print("The max profit is: ",profit2,"At percentage",bestPerc);

#----------------------------------------------------------------------------------------------------
