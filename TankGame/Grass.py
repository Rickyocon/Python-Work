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

class Grass(pygame.sprite.Sprite):
	def __init__(self, imgArray, x, y, gvr):
		pygame.sprite.Sprite.__init__(self)
		totalLen = len(imgArray)
		idx = randint(0, totalLen-1) 
		self.image = imgArray[idx]
		self.rect = self.image.get_rect()
		self.rect = Rect((x,y), (self.rect.width, self.rect.height))
		gvr.lstSprites.add(self)

	def update(self):
		# do nothing
		k = 0
