import pygame, random


class Meteor(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("meteor.png").convert()
		self.image.set_colorkey(black)
		self.rect = self.image.get_rect()


class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("player.png").convert()
		self.image.set_colorkey(black)
		self.rect = self.image.get_rect()

	def update(self):
		mouse_pos = pygame.mouse.get_pos()
		player.rect.x = mouse_pos[0]
		player.rect.y = 510

class Laser(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("laser.png").convert()
		self.image.set_colorkey(black)
		self.rect = self.image.get_rect()

	def update(self):
		self.rect.y -= 3


white = (255,255,255)
black = (0,0,0)

pygame.init()
screen = pygame.display.set_mode([900,600])
clock = pygame.time.Clock()

done = False
score = 0

all_sprites_list = pygame.sprite.Group()
meteor_list = pygame.sprite.Group()
laser_list = pygame.sprite.Group()

for i in range(50):
	meteor = Meteor()
	meteor.rect.x = random.randrange(880)
	meteor.rect.y = random.randrange(450)

	meteor_list.add(meteor)
	all_sprites_list.add(meteor)

player = Player()
all_sprites_list.add(player)


while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

		if event.type == pygame.MOUSEBUTTONDOWN:
			laser = Laser()
			laser.rect.x = player.rect.x + 45
			laser.rect.y = player.rect.y - 20

			all_sprites_list.add(laser)
			laser_list. add(laser)

	all_sprites_list.update()

	for laser in laser_list:
		meteor_hit_list = pygame.sprite.spritecollide(laser, meteor_list,True)
		for meteor in meteor_hit_list:
			all_sprites_list.remove(laser)
			laser_list.remove(laser)
			score += 1
			print(score)
		if laser.rect.y < -10:
			all_sprites_list.remove(laser)
			laser_list.remove(laser)


	screen.fill(white)
	all_sprites_list.draw(screen)

	pygame.display.flip()
	clock.tick(60)