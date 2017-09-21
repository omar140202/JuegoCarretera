import pygame
from pygame.sprite import Sprite
from pygame import *
import util

class Villano(Sprite):
	def __init__(self,coord,vel):
		Sprite.__init__(self)
		self.image = util.cargar_imagen('imagenes/auto.png')
		self.rect = self.image.get_rect()
		self.rect.move_ip(coord[1], coord[0])
		self.dir = "l"
		self.velocidad=vel
        
	def update(self):
		self.rect.y += self.velocidad
		self.rect.y =self.rect.y %620
		print self.rect.y
		
