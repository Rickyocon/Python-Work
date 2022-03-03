# Assumption: all in CAPITAL CASE letters
def encrypt(sPlaintext, key):
	sCiphertext = "";
	for sLetter in sPlaintext:
		idx = ord(sLetter) - ord("A");
		idx_new = (idx+key)%26;
		ch_new = chr(idx_new + ord("A"));
		sCiphertext += ch_new;
	return sCiphertext;

#-----------------------------------------------------

# MAIN PROGRAM
s2 = encrypt("ABCZ", 2);
print(s2);

#-----------------------------------------------------
