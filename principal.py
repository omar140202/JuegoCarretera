import sys, pygame, util
from pygame.locals import *
from heroe import *
from villano import *
from random import *


SCREEN_WIDTH = 620
SCREEN_HEIGHT = 590
ICON_SIZE = 32

def game():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode( (SCREEN_WIDTH,SCREEN_HEIGHT) )
    pygame.display.set_caption( "El Cruce" )
    background_image = util.cargar_imagen('imagenes/carretera.jpg');
    pierde_vida = util.cargar_sonido('sonidos/bocina.wav')
    pygame.mouse.set_visible( False )
    temporizador = pygame.time.Clock()
    heroe = Heroe()
    teclas = pygame.key.get_pressed()
    villano = [Villano((0,130),randint(3,10)),
               Villano((0,210),randint(6,10)),
               Villano((0,290),randint(4,10)),
               Villano((0,370),randint(8,10)),
               Villano((0,450),randint(7,10)),
               Villano((0,530),randint(8,10)),
               Villano((0, 50),randint(3,10)),]
    
    while True:
        aviso  = pygame.font.Font(None,80)
        fuente = pygame.font.Font(None,35)
        texto_puntos = fuente.render("Puntos: "+str(heroe.puntos),1,(255,255,255))
        texto_vida = fuente.render("Vida: "+str(heroe.vida),1,(255,255,255))
        texto_final = aviso.render ("you're died",1,(255,0,0))
        texto_ganador = aviso.render ("Ganaste",1,(255,255,0))		
		
        
        heroe.update()
        for n in villano:
            n.update()   
				
        for n in villano:
            if heroe.rect.colliderect(n.rect):
                heroe.image = heroe.imagenes[1]
                pierde_vida.play()
                if heroe.vida > 0:
                    heroe.vida=heroe.vida-1
                if heroe.puntos > 0:
                    heroe.puntos -=1
            if n.rect.y > 579 and heroe.vida > 0:
				heroe.puntos += 1
				if heroe.puntos < 50:
					n.velocidad = randint(5,12)
				elif heroe.puntos < 100:
					n.velocidad = randint(12,20)
				elif heroe.puntos < 150:
					n.velocidad = randint(17,30)
				 
            elif heroe.vida == 0 or heroe.puntos == 150:
		            n.velocidad = 0 
		            n.rect.y = 10                      
            
					
	    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if teclas[K_x]:
				sys.exit()
        
        screen.blit(background_image, (0,0))
        screen.blit(heroe.image, heroe.rect)
        screen.blit(texto_vida,(400,550))
        screen.blit(texto_puntos,(100,550))
    	if heroe.vida == 0:		
			screen.blit(texto_final,(180,250))		
        if heroe.puntos == 150:
			screen.blit(texto_ganador,(180,250))
        
        for n in villano:
            screen.blit(n.image, n.rect)
        pygame.display.update()
        pygame.time.delay(10)

      
if __name__ == '__main__':
      game()

