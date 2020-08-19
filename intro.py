import pygame, sys
pygame.init()


# definir colores
BLACK = (0,0,0)
WHITE = (225,225,225)
GREEN = (0,225,0)
RED = (225,0,0)
BLUE = (0,0,225)

size = (800, 500)

# crear una ventana

screen = pygame.display.set_mode(size)
# controlar los FPS
clock = pygame.time.Clock()
# coordenadas
cord_x = 400
cord_y = 200

# velocidad de movimiento del cuadrado
speed_x = 3
speed_y = 3

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	# logica
	if (cord_x>720 or cord_x<0):
		speed_x *= -1
	if (cord_y>420 or cord_y<0):
		speed_y *= -1

	cord_x += speed_x
	cord_y += speed_y
	# end logica
	screen.fill(WHITE)   # poner color de fondo 
	###### Zona de dibujo

	pygame.draw.rect(screen, RED, (cord_x,cord_y,80,80))
		

	### fin zona de dibujo
	pygame.display.flip()  #actualizar pantalla

	clock.tick(60)