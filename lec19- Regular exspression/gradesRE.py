# Read out the file
f1 = open("grades.txt","r");
s1 = f1.read();
f1.close();

#2. Specify the regex pattern and search for info

import re;
r1 = re.compile("FName: *([a-zA-Z]+).*?Grade: *([A-F])");
arr = r1.findall(s1);
print(arr);
