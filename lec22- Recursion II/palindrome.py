# Return True if s is a palindrome
def isPal(s):
	if len(s)<=1:
		return True;
	else:
		return s[0]==s[len(s)-1] and isPal(s[1: len(s)-1]);

#----------------------------------------------------------------------

# MAIN PROGRAM
arrStr = ["1", "1221", "12321", "123421"];
for s in arrStr:
	res = isPal(s);
	print(s + ": " + str(res));
