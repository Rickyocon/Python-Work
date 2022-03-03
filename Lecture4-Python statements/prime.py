# Ricky )2/10/21
#a program which tells if a number is prime

iNum = int( input("enter a number: ") );
iCount = 0;
for iFactor in range(2, iNum):
    if iNum%iFactor == 0:
       iCount = iCount + 1;
if iCount==0:
    print("Prime!");
else:
    print("Composite!");
