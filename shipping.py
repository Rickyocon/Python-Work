iWeight = int(input("enter pounds: "));
if iWeight<=2:
    fRate = 2.0;
elif iWeight<=6:
    fRate = 1.5;
elif iWeight<=8:
    fRate = 0.5;
else:
    fRate = 0.2;
fTotal = iWeight * fRate;
print("Total charge: " + str(fTotal));
