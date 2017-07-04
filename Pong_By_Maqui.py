#Importamos Las Clases
import pygame,sys
from pygame.locals import *
from random import randint

#Iniciamos Pygame
pygame.init()

#Inicializamos El Reloj
FPS = 20
fpsClock = pygame.time.Clock()

#Propiedades De La Ventana
Ventana = pygame.display.set_mode([600, 400])
pygame.display.set_caption("Pong Alpha 0.1")

Negro = (0,0,0)


while True:
	Ventana.fill(Negro)
	for event in pygame.event.get():
        	if event.type == pygame.QUIT:
                	pygame.quit()
			sys.exit()

                elif event.type==KEYDOWN:
			if event.key==K_ESCAPE:
                                pygame.quit()
	                        sys.exit()
           	        #elif event.key==K_LEFT:

                  	#elif event.key==K_RIGHT:

	        	#elif event.key==K_SPACE:

	        	#elif event.key==K_TAB:

                        


        pygame.display.update ()
	fpsClock.tick(FPS)

