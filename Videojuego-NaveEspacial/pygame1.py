import pygame
import random
from personaje import Cubo as cb
from enemigo import Enemigo 
#crear constantes 

ANCHO = 1000
ALTO = 800
VENTANA = pygame.display.set_mode([ANCHO, ALTO])
FPS = 60

#constante de jugando
jugando = True

cubo = cb(ANCHO/2,ALTO-75)

tiempo_pasado = 0
tiempo_entreenmigos = 500

reloj = pygame.time.Clock()

enemigos  = []

enemigos.append(Enemigo(ANCHO/2, 100))

#con cada tecla gestionar hacia donde va el cubo
def gestionar_teclas(teclas):
    ##if teclas[pygame.K_w]:
     ##   cubo.y -= cubo.velocidad
   ## if teclas[pygame.K_s]:
      ##  cubo.y += cubo.velocidad
    if teclas[pygame.K_a]:
        cubo.x -= cubo.velocidad
    if teclas[pygame.K_d]:
        cubo.x += cubo.velocidad

#bucle en el cual estamos jugando
while jugando:

    tiempo_pasado += reloj.tick(FPS)

    if tiempo_pasado > tiempo_entreenmigos:
        enemigos.append(Enemigo(random.randint(0,ANCHO),-100))
        tiempo_pasado = 0

    eventos = pygame.event.get()
    teclas = pygame.key.get_pressed() #accede a las teclas de mi teclado mientras se presionan

    gestionar_teclas(teclas)


    for evento in eventos:
        if evento.type == pygame.QUIT:
            jugando = False
    VENTANA.fill("black")
    cubo.dibujar(VENTANA)

    for enemigo in enemigos:
        enemigo.dibujar(VENTANA)
        enemigo.movimiento()

    pygame.display.update()

quit()