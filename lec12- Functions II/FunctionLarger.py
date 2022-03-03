#define a function which returns the bigger of the two numbers
def getBigger(num1, num2):
	if num1>num2:
		return num1;
	else:
		return num2;

#main program
a = 100;
b = 200;
print("The bigger number is: " + str(getBigger(a, b)) );
		
