import pygame
import string
from pygame.locals import *
from random import *

# Now our own modules
from MyTank import *
from EnemyTank import *
from Grass import *
from EnemyTank import *
from SoftBrick import *
from HardBrick import *
from Bullet import *


# path - the file path to load image
# x, y - the coordinate to pick the transparency color
# if -1, -1, ignore the set_colorkey
def loadImage(path, x, y):
	myImage = pygame.image.load(path)
	myImage = myImage.convert()
	if x<>-1:
		colorkey = myImage.get_at( (x,y) )
		myImage.set_colorkey(colorkey, 0)
	return myImage

# load an image array
# all params same as loadImage
# rg: a range that contains index number
# return an array of image objects
def loadImageArr(path, x, y, rg):
	arrImages = []
	for i in rg:
		name = path + str(i) + ".bmp"
		myImage = loadImage(name, x, y)
		if myImage==None:
			print "load image error: " + name
			return []
		arrImages.append(myImage)
	return arrImages
	
	


# set up the window and two panes	
# return screen, background
def setupWin(width, height):
	pygame.init()
	screen = pygame.display.set_mode((width, height))
	pygame.display.set_caption("Bouncing Ball")
	pygame.mouse.set_visible(0)
	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((10, 100, 10))
	return screen, background

def loadResources(gvr):
	# for MyTank 
	basepath = "images/mytank/"
	mytankUpimgs = loadImageArr("images/mytank/up/tank", \
		0, 0, range(1,3))
	mytankDownimgs = loadImageArr("images/mytank/down/tank", \
		0, 0, range(1,3))
	mytankLeftimgs = loadImageArr("images/mytank/left/tank", \
		0, 0, range(1,3))
	mytankRightimgs = loadImageArr("images/mytank/right/tank", \
		0, 0, range(1,3))
	mytankExpimgs = loadImageArr("images/mytank/explosion/exp", \
	0, 0, range(1,11))
	imgMyTank = [mytankUpimgs, mytankDownimgs, \
		mytankLeftimgs, mytankRightimgs, mytankExpimgs]
	arrTankFPs = [5, 5, 5, 5, 1]  #every FP rates per change of image
	gvr.arrImageMyTank = imgMyTank
	gvr.arrTankFPs = arrTankFPs

	# for enemy Tank 
	enemytankUpimgs = loadImageArr("images/enemy/up/tank", \
		0, 0, range(1,3))
	enemytankDownimgs = loadImageArr("images/enemy/down/tank", \
		0, 0, range(1,3))
	enemytankLeftimgs = loadImageArr("images/enemy/left/tank", \
		0, 0, range(1,3))
	enemytankRightimgs = loadImageArr("images/enemy/right/tank", \
		0, 0, range(1,3))
	enemytankExpimgs = loadImageArr("images/enemy/explosion/exp", \
	0, 0, range(1,11))
	imgEnemyTank = [enemytankUpimgs, enemytankDownimgs, \
		enemytankLeftimgs, enemytankRightimgs, enemytankExpimgs]
	arrEnemyTankFPs = [5, 5, 5, 5, 1]  #every FP rates per change of image
	
	gvr.arrImageEnemyTank = imgEnemyTank
	gvr.arrEnemyTankFPs = arrTankFPs

	# for grasses
	gvr.grassImages = loadImageArr("images/grass/grass",\
		0, 0, range(1,5))
	
	# for softbrick
	gvr.softbrickImages= loadImageArr("images/softbrick/softbrick",\
		0, 0, range(1,5))

	# for hardbrick 
	gvr.hardbrickImages= loadImageArr("images/hardbrick/hardbrick",\
		0, 0, range(1,5))

	# for bullet
	gvr.bulletImages = loadImageArr("images/bullet/bullet", \
		0, 0, range(1,11))
	gvr.bulletExpImages= loadImageArr("images/bullet/explosion/exp", \
	0, 0, range(1,11))

def loadMap(gvr):
	width = gvr.BATTLEFIELD_WIDTH
	height = gvr.HEIGHT
	unitwidth = 25
	mapfile = open("map.txt", "r")
	#1. search the line map and then start read
	iUnit = width/unitwidth
	bStart = False
	count = 0
	for line in mapfile.readlines():
		if count>=iUnit: break	#we've read enough lines
		if line.startswith("#map"):
			bStart = True
			continue
		if bStart:
			rCount = 0
			for ch in line:
			  x, y = rCount*unitwidth, count*unitwidth 
			  if ch=="H": 
			    obj = HardBrick(gvr.hardbrickImages, x, y, gvr)
			  elif ch=="S": 
			    obj = SoftBrick(gvr.softbrickImages, x, y, gvr)
			  elif ch=="G": 
			    obj = Grass(gvr.grassImages, x, y, gvr)
			  else:
			    k = 1
			    #do nothing
			  rCount = rCount + 1
			count = count + 1
			if rCount!=iUnit+1: 
				print "ERROR: rCount, iUnit ", rCount, iUnit
				return
	mapfile.close()

def loadMyTank(gvr):
	mapfile = open("map.txt", "r")
	#1. search the line map and then start read
	bStart = False
	for line in mapfile.readlines():
		if line.startswith("#mytank"):
			bStart = True
			continue
		if bStart:
			words  = line.split()
			x = eval(words[0])	
			y = eval(words[1])
			gvr.mytank = MyTank(gvr.arrImageMyTank, 
				gvr.arrTankFPs, x, y, gvr);
			break 	#we are done!
	mapfile.close()

def loadEnemyTank(gvr):
	gvr.arrEnemyTankEvents = []
	mapfile = open("map.txt", "r")
	#1. search the line map and then start read
	bStart = False
	for line in mapfile.readlines():
		if line.startswith("#enemytank"):
			bStart = True
			continue
		if bStart:
			words = line.split()
			if len(words)!=3: break
			x = int(words[0])
			y = int(words[1])
			sec = int(words[2])
			entry = [x,y,sec]
			gvr.arrEnemyTankEvents.append(entry)
	mapfile.close()
	print gvr.arrEnemyTankEvents

def initObjects(gvr):
	#now load the map
	loadMap(gvr)

	#now load my tank
	loadMyTank(gvr)

	#now load enemy tank
	loadEnemyTank(gvr)



def collisionTest(gvr):
	# Collesion TEST
	#1. bullets with tanks
	dict1 =pygame.sprite.groupcollide(gvr.lstBullets,gvr.lstTanks,\
			False, False)
	for bullet in dict1.keys():
		bKillMe = False
		for tank in dict1[bullet]:
			if tank!=bullet.owner:
				tank.hit()
				bKillMe = True #the bullet should explode too
		if bKillMe: bullet.hit()
		


	#2. tanks with tanks
	dict2 =pygame.sprite.groupcollide(gvr.lstTanks,gvr.lstTanks,\
			False, False)
	for tank1 in dict2.keys():
		for tankTwo in dict2[tank1]:
			if tank1 != tankTwo:
				tankTwo.hit()

	#3. bullets with walls
	dict3 = pygame.sprite.groupcollide(gvr.lstBullets, gvr.lstBricks,\
		False, False)
	for bullet in dict3.keys():
		bullet.hit()
	for bricks in dict3.values():
		for brick in bricks:
			brick.hit()

	#4. tank with walls
	dict4 = pygame.sprite.groupcollide(gvr.lstTanks, gvr.lstBricks,\
		False, False)
	for t in dict4.keys():
		#each tank, stop first, then back up one step
		t.stop()
		t.backup()
	# Collesion test end


def handleEvent(gvr):
	for event in pygame.event.get():
		if event.type==	QUIT:
			return "quit"
		elif event.type==KEYDOWN and event.key == K_ESCAPE:
			return  "quit"
		elif event.type==KEYDOWN and event.key == K_DOWN:
			gvr.mytank.down()	
		elif event.type==KEYDOWN and event.key == K_UP:
			gvr.mytank.up()	
		elif event.type==KEYDOWN and event.key == K_LEFT:
			gvr.mytank.left()	
		elif event.type==KEYDOWN and event.key == K_RIGHT:
			gvr.mytank.right()	
		elif event.type==KEYDOWN and event.key == K_EQUALS:
			gvr.mytank.acc()	
		elif event.type==KEYDOWN and event.key == K_MINUS:
			gvr.mytank.dec()	
		elif event.type==KEYDOWN and event.key == K_COMMA:
			gvr.mytank.fire()
		else:
			# do nothing
			# print event
			k = 0
	return "unknown"
	


def loopRun(screen, background, gvr):
	clock = pygame.time.Clock()
	freq = 60
	decision = "unknown"
	seconds = 0
	tick = freq
	lstEnemyEvents = gvr.arrEnemyTankEvents
	idxNextEvent = 0
	iNextEventSeconds = lstEnemyEvents[0][2]

	while decision == "unknown":
		clock.tick(freq)
		tick = tick -1
		if tick==0:
			tick, seconds = freq, seconds + 1

		if seconds == iNextEventSeconds:
			x = lstEnemyEvents[idxNextEvent][0]
			y = lstEnemyEvents[idxNextEvent][1]
			etank = EnemyTank(gvr.arrImageEnemyTank, gvr.arrEnemyTankFPs, x, y, gvr)
			print "OK created at ", x, y
			idxNextEvent = idxNextEvent + 1 
			if(idxNextEvent<len(lstEnemyEvents)):
				iNextEventSeconds = lstEnemyEvents[idxNextEvent][2]
			else:
				iNextEventSeconds = -1
			print "idxNextEvent, iNextEventSeconds", idxNextEvent, iNextEventSeconds

		
			


		decision = handleEvent(gvr)
		collisionTest(gvr)
				
		screen.blit(background,(0,0))
		gvr.lstSprites.update()
		gvr.lstSprites.draw(screen)
		pygame.display.flip()
	
	print decision
	print "Closing!"
	pygame.quit()



# -- GLOBAL CONSTANTS ----------------
class globalvar:
	WIDTH = 1000 
	HEIGHT = 800
	BATTLEFIELD_WIDTH = 800
	MAX_ENEMY_SPEED = 5
	MAX_MY_SPEED = 8

	arrImageMyTank = []
	arrTankFPs = []
	arrImageEnemyTank = []
	arrEnemyTankFPs = []
	arrEnemyTankEvents = []

	lstSprites = pygame.sprite.RenderClear(()) # used to draw all objects
	lstTanks = pygame.sprite.RenderClear(())   # used for collision detection of enemy tanks
	lstBricks= pygame.sprite.RenderClear(())   # used for collision test of bullets and etc.
	lstBullets = pygame.sprite.RenderClear(()) # used for collision test.
# -- GLOBAL CONSTANTS AND VARIABLES --



def main():
	gvr = globalvar() 	#global var
	#1. init screen
	screen, background = setupWin(gvr.WIDTH, gvr.HEIGHT)

	#2. load images 
	loadResources(gvr)

	#3. init objects	
	initObjects(gvr)


	#5. Handling of events
	loopRun(screen, background, gvr)

	


if __name__=="main": main()
