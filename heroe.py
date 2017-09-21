import pygame
from pygame.sprite import Sprite
from pygame import *
import util

class Heroe(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.puntos = 0
		self.vida = 100
		self.estado = "cruzando"
		self.imagenes = [util.cargar_imagen('imagenes\corredor_izq.png'),
						util.cargar_imagen('imagenes\corredor_cayendo.png'),
						util.cargar_imagen('imagenes\corredor_der.png'),
						util.cargar_imagen('imagenes\corredor_cayendo.png')]
		self.image = self.imagenes[0]
		self.rect = self.image.get_rect()
		self.rect.move_ip(10, 200)
        
	def update(self):
		teclas = pygame.key.get_pressed()
		if self.vida > 0:					
			if teclas[K_LEFT] and self.rect.x>=10:
				self.rect.x -= 10
				self.image = self.imagenes[0]
				if self.rect.x<=20 and self.estado == "volviendo":
					self.puntos = self.puntos + 1
					self.estado = "cruzando"
			elif teclas[K_RIGHT] and self.rect.x<=640-self.rect.width:
				self.rect.x += 10
				self.image = self.imagenes[2]
				if self.rect.x>=470 and self.estado == "cruzando":
					self.puntos = self.puntos + 1
					self.estado = "volviendo"
			if teclas[K_UP] and self.rect.y>=10:
				self.rect.y -= 10
				self.image = self.imagenes[2]
			elif teclas[K_DOWN] and self.rect.y<=480-self.rect.height:
				self.rect.y += 10
				self.image = self.imagenes[0]
				
		else:
			self.image = self.imagenes[3]
