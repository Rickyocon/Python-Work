n = int(input("Enter n: "));
iCounter = 1;
while iCounter<=n:
    if iCounter==1 or iCounter==n:
        print(n*"*");
    else:
        print( "*" + (n-2)*" " + "*");
    iCounter += 1;
