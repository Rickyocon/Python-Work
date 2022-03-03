def getMax(arr):
	max = arr[0];
	for x in arr:
		if x > max:
			max = x;
	return max;


def getMax(arr,num):
	bFound = False; #if we have found an element less then the number
	max = 0; # dosent matter
	for x in arr:
		if x > num:
			if bFound==False: # is this the first time we see an element which is l-ess then the given nunber
				max = x;
				bFound = True;
			else:
				if x > max:
					max = x;
	return max;
				
