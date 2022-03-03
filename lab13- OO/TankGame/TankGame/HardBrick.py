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
class HardBrick(pygame.sprite.Sprite):
	bDead = False
	points = 10
	def __init__(self, imgArray, x, y, gvr):
		pygame.sprite.Sprite.__init__(self)
		totalLen = len(imgArray)
		idx = randint(0, totalLen-1) 
		self.image = imgArray[idx]
		self.rect = self.image.get_rect()
		self.rect = Rect((x,y), (self.rect.width, self.rect.height))
		gvr.lstBricks.add(self)
		gvr.lstSprites.add(self)

	def hit(self):
		self.points = self.points -1
		if self.points==0: self.bDead = True

	def update(self):
		if(self.bDead): self.kill()
