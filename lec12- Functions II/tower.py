#print instructions for
#moving n disks from towerSrc to towerDest
#using towerTemp as a storage device
def moveDisks(n, towerSrc, towerDest, towerStorage):
	if n==1:
		print(towerSrc + "-> " + towerDest);
	else:
		moveDisks(n-1, towerSrc, towerStorage, towerDest);
		print(towerSrc + " -> " + towerDest);
		moveDisks(n-1, towerStorage, towerDest, towerSrc);

#main program
moveDisks(10, "A", "C", "B");

