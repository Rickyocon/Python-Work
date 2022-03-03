f1 = open("numbers.txt", "r");
arrLines = f1.readlines();
f1.close();

sum = 0;
idx = 0;
for line in arrLines:
	arr = line.split();
	sum += int( arr[idx] );
	idx += 1;
print("sum: " + str(sum));
