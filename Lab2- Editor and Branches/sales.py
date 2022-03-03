iNum = int(input("type the number of textbooks you are geting: "));
if iNum<=10:
    fDiscount = 0.02;
elif iNum<=20:
    fDiscount = 0.05;
elif iNum<=100:
    fDiscount = 0.10;
else: 
    fDiscount = 0.20;

fTotal=132.24 * iNum * (1-fDiscount);
print("Total Change: " + str(fTotal));
