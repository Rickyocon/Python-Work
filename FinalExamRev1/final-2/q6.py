import re;

f1 = open("ncc.html", "r");
s1 = f1.read();
f1.close();

r1 = re.compile("<tr>.*?</tr>", re.DOTALL | re.MULTILINE);
arr = r1.findall(s1);

# ONLY print put the Associate Professors
for rec in arr:
	if rec.find("Associate")>=0:
		r2 = re.compile("<strong>(.*?)</strong>");
		arr2 = r2.findall(rec);
		print(arr2[0]);
