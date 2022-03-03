from graphics import *

# create a window
def createWin():
	win = GraphWin("tictac", 500, 500)
	win.setCoords(0, 0, 3, 3)
	for x in range(3):
		for y in range(3):
			Rectangle(Point(x, y), Point(x+1, y+1)).draw(win)
	return win

# -----------------------------------------------------------
# Your Job! Complete the evaluate function
# -----------------------------------------------------------
# this function evaluates how "good" is the move by "color" at (x,y) by looking ahead "steps"
# It returns 1 if color for sure is going to win
# It returns -1 if color for sure is going to lose
# It returns 0 if eventually there is a draw, or it does not know the final result because "steps" is too small
# Note that we should NOT put the "color" at (x,y) because we are just evaluating it!
# -----------------------------------------------------------
def evaluate(grids, color, x, y, steps):
	# pretend that "color" is placed in cell (x,y), you WILL HAVE TO REMOVE IT before return!
	grids[x][y] = color;

	# In the following we will assess how "good" the move is for player "color".
	# base case: steps is 0, just evaluate right now WITHOUT looking ahead
	if steps==0: 
		winner = getWinner(grids);

		#before return, remove the stone of color at (x,y).
		grids[x][y] = "_"; 

		if winner==color: return 1 
		elif winner=="_": return 0 
		else: return -1 

	# recursive case: try each empty cell, and look ahead "steps-1" steps
	else:
		# Note: variable 'oponent' is the oponent's color
		if color=="red": oponent = "yellow"
		else: oponent = "red" 

		# First, check if there is already a winner
		winner = getWinner(grids);
		if winner==color: 
			grids[x][y] = "_";
			return 1
		elif winner==oponent: 
			grids[x][y] = "_";
			return -1

		#Otherwise, check recursively
		# Note that we have already played "color" at (x,y) at the beginning of this function
		# Therefore, it's now the turn of oponent. We will evaluate each empty cell and check
		# oow good it is for the oponent. (Note: NOT how good for the "color")
		bestX, bestY = -1, -1; # the x,y of the best move for the OPPONENT 
		maxScore = -2; #the score of the best move for the OPPONENT!
		for tx in range(3):
			for ty in range(3):
				if grids[tx][ty]=="_":
					grids[tx][ty]=oponent;
					# recursive call here! Note: avoid infinite loop!
					score = _________________________________________________;
					grids[tx][ty]="_";
					if score>=maxScore:
						_________________________________;
						maxScore = score;
		if maxScore ==-2: maxScore =  0; # this cooresponds to the case that there is no empty cell.

		# Don't forget the action you need to perform BEFORE return;
		____________________________________;
		#Note here: maxScore is the BEST MOVE for the opponent! Your return should NOT be "maxScore", but an expression built upon it.
		return _____________________________________________;



# computer player chooses a location, returns (x,y)
def computerChooseLocation(grid):
	bestScore = -1;
	bestX, bestY = -1, -1;
	for x in range(3):
		for y in range(3):
			if grid[x][y]=="_":
				score = evaluate(grid, "red", x, y, 8);
				if score>=bestScore:
					bestX, bestY = x, y;
					bestScore = score;
	return bestX, bestY;

def userChooseLocation(win):
	p = win.getMouse()
	x, y = int(p.getX()),int(p.getY())
	return x,y

def canPlaceToken(grid, x, y):
	if grid[x][y]=="_": return True
	else: return False

def placeToken(win, grid,x, y, color):
	grid[x][y] = color
	circ = Circle(Point(x+0.5, y+0.5), 0.5)
	circ.setFill(color)
	circ.draw(win)
	


def getWinner(grids):
	#1. check rows
	for x in range(3):
		if grids[x][0] == grids[x][1]==grids[x][2] and grids[x][0]!="_":
			return grids[x][0]

	#2. check columns
	for x in range(3):
		if grids[0][x] == grids[1][x]==grids[2][x] and grids[0][x]!="_":
			return grids[0][x]

	#3. check the two diagnals
	if grids[0][0]==grids[1][1]==grids[2][2] and grids[0][0]!="_":
		return grids[0][0]

	if grids[2][0]==grids[1][1]==grids[0][2] and grids[2][0]!="_":
		return grids[2][0]
	
	return "_"

def reportWinner(win, winner):
	lbl = Text(Point(1.5, 1.5), "Winner is " + winner)
	lbl.setSize(24)
	lbl.draw(win)


def main():
#1. create window and grids
	win = createWin()

# turn = red; //alternates between red/yellow
	turn = "red"

# grids is 3 X 3 array to store information
	grid = [
		[ "_", "_", "_"],
		[ "_", "_", "_"],
		[ "_", "_", "_"]
		]

#2. repeat up to 9 times
	for x in range(9):
   #          wait for user to place a token
		if turn=="red":
			x, y = computerChooseLocation(grid)
		else:
			x, y = userChooseLocation(win)
		if canPlaceToken(grid, x, y):
			placeToken(win, grid, x, y, turn)
		else:
			print "User", turn, "places token in the wrong place!"
			print "User", turn, "loses the game!"
			break

   #	    if someone wins, display msg, AND break
		winner = getWinner(grid)
		if winner!="_":
			reportWinner(win, winner)
			break

   # 		Switch color
		if turn=="red":
			turn= "yellow"
		else:
			turn= "red"

	win.getMouse()

main()
