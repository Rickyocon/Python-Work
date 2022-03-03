# returns True if n is a prime
def isPrime(n):
    if n<2: return False;
    if n==2: return True;
    for x in range(2, n):
        if n%x==0:
            return False;
        if x*x>n:
            return True;

# return the number of Sophie-Germain primes in the array
def countSophie(arr):
	count = 0;
	for x in arr:
		if isPrime(x) and isPrime(2*x+1) == True:
			count += 1;	
	return count;
# --------------------------------
# MAIN PROGRAM. Do not touch!!!
# --------------------------------

def getNums(filename):
    f1 = open(filename, "r");
    s1 = f1.read();
    f1.close();
    arr = s1.split();
    arr2 = [];
    for x in arr:
        arr2.append(int(x));
    return arr2;

arr = ["num1.txt", "num2.txt", "num3.txt", "num4.txt", "num5.txt"];
for fname in arr:
    arrNums = getNums(fname);
    val = countSophie(arrNums);
    print(fname + ": " + str(val));
