
import pygame
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
class Bullet(pygame.sprite.Sprite):
	bDead = False
	points = 10
	speed = 0
	arrImages = []
	arrRunImages = []
	arrExplodeImages = []
	idx = 0
	count = 0
	arrFPs = [5,5, 5, 5, 2]
	state = 0
	gvr = None
	owner = None

	#CONSTANTS
	UP=0
	DOWN=1
	LEFT=2
	RIGHT=3
	EXPLOSION=4

	def __init__(self, owner, 
		imgRunArray, imgExplodeArray, x, y, direction, gvr):
		self.owner = owner
		pygame.sprite.Sprite.__init__(self)
		self.state = direction
		self.arrRunImages = imgRunArray
		self.arrExplodeImages = imgExplodeArray
		self.arrImages = self.arrRunImages
		self.image = self.arrRunImages[0]
		self.rect = self.image.get_rect()
		self.rect = Rect((x,y), (self.rect.width, self.rect.height))
		self.gvr = gvr
		self.speed = self.gvr.MAX_MY_SPEED * 1
		gvr.lstSprites.add(self)
		gvr.lstBullets.add(self)

	def hit(self):
		if self.state!=self.EXPLOSION:
			self.state = self.EXPLOSION
			self.arrImages = self.arrExplodeImages
			self.idx = 0
		self.gvr.lstBullets.remove(self) 
		# note: explosion stage 11 pictures
		# this is to prevent triggering hit many times
		# also avoid triggering hit of tank many times

	def update(self):
		if(self.rect.top<10 or \
				self.rect.top>self.gvr.HEIGHT-10 or \
				self.rect.left<0 or \
				self.rect.left>self.gvr.BATTLEFIELD_WIDTH-10):
			self.hit()
		self.image = self.arrImages[self.idx]
		if self.state==self.UP:
			self.rect.move_ip(0, -self.speed)
		elif self.state==self.DOWN:
			self.rect.move_ip(0, self.speed)
		elif self.state==self.LEFT:
			self.rect.move_ip(-self.speed,0)
		elif self.state==self.RIGHT:
			self.rect.move_ip(self.speed,0)
		else:
			if(self.idx==len(self.arrImages)-1):
				self.kill()
		self.count = (self.count + 1) % 10000
		if self.count% self.arrFPs[self.state]==0: 
			self.idx = (self.idx+1)%len(self.arrImages)

