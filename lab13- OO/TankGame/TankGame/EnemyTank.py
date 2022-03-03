
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

class EnemyTank(pygame.sprite.Sprite):
	speed = 1
	arrImages = []
	idx = 0
	count = 0
	arrImgArr = []
	arrFPs = []
	state = 0
	gvr = None

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
		self.state = 1
		self.gvr = gvr
		gvr.lstSprites.add(self)
		gvr.lstTanks.add(self)
		self.update()
	
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
		if self.speed < self.gvr.MAX_ENEMY_SPEED:
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

	def hit(self):
		self.explode()

	def explode(self):
		self.state = self.EXPLOSION
		# self.idx = 0, 	think about why this is commented out

	def fire(self):
		newbullet = Bullet(self,
			self.gvr.bulletImages, 
			self.gvr.bulletExpImages, 
			self.rect.left + 25, 
			self.rect.top + 25,
			self.state, 
			self.gvr)
		self.gvr.lstSprites.add(newbullet)
		self.gvr.lstBullets.add(newbullet)


	def ai(self):
		if (self.state==self.EXPLOSION): return 
		if (self.count%10!=0): return
		x = randint(0, 200)
		if x >= 0 and x <= 10:
			self.acc()
		elif x >10 and x <= 20:
			self.dec()
		elif x >20 and x <= 30:
			if self.rect.left<self.gvr.BATTLEFIELD_WIDTH-100:
				self.right()
		elif x >30 and x <= 40:
			self.fire()
		elif x <40 and x <= 50:
			if self.rect.top>100:
				self.up()
		elif x >50 and x <= 60:
			if self.rect.left>100:
				self.left()
		elif x >60 and x <= 100:
			if self.rect.top<self.gvr.HEIGHT-100:
				self.down()
		else:
			# do nothing
			k = 1

		cx = self.rect.left
		cy = self.rect.top
		if cy<10:
			self.down()
		elif cy>self.gvr.HEIGHT-100:
			self.up()
		else:	k = 1

		if cx<10:
			self.right()
		elif cx>self.gvr.BATTLEFIELD_WIDTH-100:
			self.left()
		else:  k = 1
	



	def update(self):
		self.ai()

		self.count = (self.count+1)% 1000000
		self.arrImages = self.arrImgArr[self.state]
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
			print "ERROR. unrecognized state: ", state
		self.image = self.arrImages[self.idx]

