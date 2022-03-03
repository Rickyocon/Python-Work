from minime import *;

arr1 = [1, 2, 3, 9, 301, 954, 2034, 7391, 332211223];

s = getSum(arr1);
print("The sum is: ", s);

co = getCountOdd(arr1);
print("There are ", co, " odd numbers.");

mx = getMax(arr1);
print("The max is ", mx);

avg = getAvg(arr1);
print("The average is " , avg);

rvs = getReverse(arr1);
print("The reverse of the array is: ");
print(rvs)

bAsc = isAscending(arr1);
print("Ascending? ", bAsc);
