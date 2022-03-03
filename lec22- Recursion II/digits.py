# Return sum of digits n
def sumDigits(n):
	if n<10:
		return n;
	else:
		return sumDigits(n//10) + n%10;

#----------------------------------------------------

# MAIN  PROGRAM
y = sumDigits(1111);
print(y);
