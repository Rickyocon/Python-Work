class president:
	def __init__(self, sName, sParty):
		self.name = sName;
		self.party = sParty;

	def makeSpeech(self):
		print("Hi, I am " + self.name);
		print("Vote for " + self.party);

#-------------------------------------------------------------
# MAIN PROGRAM
p1 = president("Bill clinton", "Democratics");
p2 = president("George Bush", "Republican");
arr = [p1, p2];
for x in arr:
	x.makeSpeech();
	
