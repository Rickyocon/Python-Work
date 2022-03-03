import re;   # Or from re import *;

r1 = re.compile("\(([0-9]{3})\) [0-9]{3}-[0-9]{4}");
f1 = open("prof.html", "r");
s1 = f1.read();
arr = r1.findall(s1);
print(arr);


