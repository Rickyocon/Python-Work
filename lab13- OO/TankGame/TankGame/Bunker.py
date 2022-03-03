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

class Bunker(pygame.sprite.Sprite):
	speed = 0
	arrImages = []
	idx = 0
	count = 0
	arrImgArr = []
	arrFPs = []
	state = 0
	MAX_SPEED = 5
	gvr = None
	life = 3

	#CONSTANTS
	UP=0
	DOWN=1
	LEFT=2
	RIGHT=3
	EXPLOSION=4
	def __init__(self, arrImageArr, arrFPs, x, y, gvr):
		pygame.sprite.Sprite.__init__(self)
		self.arrImgArr = arrImageArr
		self.arrFPs = arrFPs
		self.arrImages = self.arrImgArr[0]
		self.image = self.arrImages[0]
		self.rect = self.image.get_rect()
		self.rect = Rect((x,y), (self.rect.width, self.rect.height)) 
		self.state = 0
		self.gvr = gvr
		self.update()
		gvr.lstSprites.add(self)
		gvr.lstTanks.add(self)
	
	def up(self):
		self.state = self.UP
		self.idx = 0

	def down(self):
		self.state = self.DOWN	
		self.idx = 0

	def left(self):
		self.state = self.LEFT
		self.idx = 0

	def right(self):
		self.state = self.RIGHT
		self.idx = 0

	def acc(self):
		if self.speed < self.gvr.MAX_MY_SPEED:
			self.speed = self.speed + 1

	def dec(self):
		if self.speed > 0:
			self.speed = self.speed - 1

	def stop(self):
		self.speed = 0

	def backup(self): 
		#reverse one step
		dist = self.speed + 2
		if self.state == self.LEFT:
			self.rect.move_ip(dist ,0)
		elif self.state == self.RIGHT:	
			self.rect.move_ip(-dist ,0)
		elif self.state == self.DOWN:	
			self.rect.move_ip(0, -dist)
		elif self.state == self.UP:	
			self.rect.move_ip(0, dist)

	def explode(self):
		self.state = self.EXPLOSION
		self.idx = 0

	def hit(self):
		self.life = self.life -1
		if self.life==0:
			self.explode()

	def fire(self):
		newbullet = Bullet(
			self,
			self.gvr.bulletImages, 
			self.gvr.bulletExpImages, 
			self.rect.left + 25, 
			self.rect.top + 25,
			self.state, 
			self.gvr)
		self.gvr.lstSprites.add(newbullet)


	def rotate(self):
		if self.state == self.RIGHT:
			self.state = self.DOWN;
		elif self.state == self.LEFT:
			self.state = self.UP
		elif self.state == self.DOWN:
			self.state = self.LEFT
		elif self.state == self.UP:
			self.state = self.RIGHT
	

	def update(self):
		self.count = (self.count+1)% 100000
		if self.count%50==0:
			self.rotate();
		if self.count%100==0:
			self.fire();
		self.arrImages = self.arrImgArr[self.state]
		if self.count%25==0:
			self.rotate()
		if self.count%self.arrFPs[self.state]==0:
			self.idx = (self.idx + 1) % len(self.arrImages)
		if self.state==self.UP:
			self.rect.move_ip(0,-self.speed)
		elif self.state==self.DOWN:
			self.rect.move_ip(0,self.speed)
		elif self.state==self.LEFT:
			self.rect.move_ip(-self.speed,0)
		elif self.state==self.RIGHT:
			self.rect.move_ip(self.speed,0)
		elif self.state==self.EXPLOSION:
			if self.idx == len(self.arrImages)-1:
				self.kill()
		else:
			print("ERROR. unrecognized state: ", state)
		self.image = self.arrImages[self.idx]

		#prevent out of boundary
		x = self.rect.left
		y = self.rect.top
		if x<5 or x>self.gvr.BATTLEFIELD_WIDTH-5 \
			or y<5 or y>self.gvr.HEIGHT:
			self.stop()

