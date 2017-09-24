import pygame
from pygame.sprite import Sprite
from pygame import *
import util

class Heroe(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.puntos = 0
		self.vida = 100
		self.imagenes = [util.cargar_imagen('imagenes\corredor_izq.png'),
						util.cargar_imagen('imagenes\corredor_cayendo.png'),
						util.cargar_imagen('imagenes\corredor_der.png'),
						util.cargar_imagen('imagenes\corredor_cayendo.png')]
		self.image = self.imagenes[0]
		self.rect = self.image.get_rect()
		self.rect.move_ip(250, 500)
        
	def update(self):
		teclas = pygame.key.get_pressed()
		if self.vida > 0:					
			if teclas[K_LEFT] and self.rect.x>=20:
				self.rect.x -= 10
				self.image = self.imagenes[0]				
			elif teclas[K_RIGHT] and self.rect.x<=580-self.rect.width:
				self.rect.x += 10
				self.image = self.imagenes[2]				
			if teclas[K_UP] and self.rect.y>=10:
				self.rect.y -= 10
				self.image = self.imagenes[2]
			elif teclas[K_DOWN] and self.rect.y<=550-self.rect.height:
				self.rect.y += 10
				self.image = self.imagenes[0]
				
		else:
			self.image = self.imagenes[3]
