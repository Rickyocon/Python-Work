n = int(input("Enter n: "));
iSpaces = n - 1;
iStars = 1;

# print n lines
iCounter = 1;
while iCounter<=n:
    # print a line mixed with spaces and stars
    print(iSpaces*" " + iStars*"*");
    iSpaces -= 1;
    iStars += 1;

    iCounter += 1;
