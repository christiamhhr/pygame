import pygame

pygame.init()

# colores
black = (0,0,0)
white = (255,255,255)

screen_size = (800,600)
player_width = 15
player_height = 90


screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

#coordenadas y velocidad del jugador 1
player1_x_coor = 50
player1_y_coor = 300 - 45
player1_y_speed = 0

#coordenadas y velocidad del jugador 2
player2_x_coor = 750- player_width
player2_y_coor = 300 - 45
player2_y_speed = 0

# coordenadas de la pelota
pelota_x = 400
pelota_y = 300
pelota_speed_x = 3
pelota_speed_y = 3

game_over = False

while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_over = True

		if event.type == pygame.KEYDOWN:
			# Jugador1 
			if event.key == pygame.K_w:
				player1_y_speed = -3
			if event.key == pygame.K_s:
				player1_y_speed = 3

			# Jugador2 
			if event.key == pygame.K_UP:
				player2_y_speed = -3
			if event.key == pygame.K_DOWN:
				player2_y_speed = 3

		if event.type == pygame.KEYUP:
			# Jugador1 
			if event.key == pygame.K_w:
				player1_y_speed = 0
			if event.key == pygame.K_s:
				player1_y_speed = 0

			# Jugador2 
			if event.key == pygame.K_UP:
				player2_y_speed = 0
			if event.key == pygame.K_DOWN:
				player2_y_speed = 0

	if (pelota_y>590 or pelota_y<10):
		pelota_speed_y *=-1

	# revisa si la pelota se sale del lado derecho
	if (pelota_x > 800):
		pelota_x = 400
		pelota_y = 300
		# si dale de la pantalla, invierte direccion
		pelota_speed_x *= -1
		pelota_speed_y *= -1

	# revisa si la pelota se sale del lado izquierdo
	if (pelota_x < 0):
		pelota_x = 400
		pelota_y = 300
		# si dale de la pantalla, invierte direccion
		pelota_speed_x *= -1
		pelota_speed_y *= -1
	#,pdofoca las coordenadas para larle movimiento a los jugadores
	player1_y_coor += player1_y_speed
	player2_y_coor += player2_y_speed

	# movimiento pelota
	pelota_x += pelota_speed_x
	pelota_y += pelota_speed_y
	screen.fill(black)

	# zona de dibujo
	jugador1 = pygame.draw.rect(screen, white, (player1_x_coor,player1_y_coor, player_width,player_height))
	jugador2 = pygame.draw.rect(screen, white, (player2_x_coor,player2_y_coor, player_width,player_height))

	pelota = pygame.draw.circle(screen, white, (pelota_x,pelota_y), 10)
	# end zona de dibujo 

	# coliciones
	if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
		pelota_speed_x *= -1
	pygame.display.flip()
	clock.tick(60)
