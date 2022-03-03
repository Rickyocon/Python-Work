# The function returns a string, which is the result of
# appending _ after each letter of the input string
# For example, modStr("ab") returns "a_b_"
def modStr(s):
	if len(s)==1:
		return s+"_";
	else:
		partialStr = modStr(s[1:len(s)]);
		finalStr = s[0] + "_" + partialStr;
		return finalStr;

# ------------------------------
# main program
# ------------------------------
arrStr = ["123", "321", "adefghij", "eefi", "jjlksdf", "lkjslfkjsdfsldkj"];
for x in arrStr:
	print(x + "=> " + modStr(x));
	
