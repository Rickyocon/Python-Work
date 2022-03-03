# alerts when over 100 F
temp = float(input("Enter the reading in Celsius: "));
temp = temp*1.8 + 32;
if temp>100:
	print("Red Alert!");
