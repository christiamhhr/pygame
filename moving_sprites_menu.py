import pygame, random

screen_width = 900
screen_height = 600
white = (255,255,255)
black = (0,0,0)

class Meteor(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("meteor.png")
		self.image.set_colorkey(black)
		self.rect = self.image.get_rect() #captura la posicion

	def update(self):
		self.rect.y += 1

		if self.rect.y > screen_height:
			self.rect.y = -10
			self.rect.x = random.randrange(screen_width)

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("player.png")
		self.image.set_colorkey(black)
		self.rect = self.image.get_rect()

	def update(self):
		mouse_pos = pygame.mouse.get_pos()
		self.rect.x = mouse_pos[0]
		self.rect.y = mouse_pos[1]	


class Game(object):
	def __init__(self):
		self.score = 0

		self.meteor_list = pygame.sprite.Group()
		self.all_sprites_list = pygame.sprite.Group()

		for i in range(50):
			meteor = Meteor()
			meteor.rect.x = random.randrange(900)
			meteor.rect.y = random.randrange(600)

			self.meteor_list.add(meteor)
			self.all_sprites_list.add(meteor)

		self.player = Player()
		self.all_sprites_list.add(self.player)

	def process_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return True
		return False

	def run_logic(self):
		self.all_sprites_list.update()

		meteor_hit_list = pygame.sprite.spritecollide(self.player,self.meteor_list,True) #para eliminar las colisiones
		for meteor in meteor_hit_list:
			self.score += 1
			print(self.score)

	def display_frame(self, screen):
		screen.fill(white)
		self.all_sprites_list.draw(screen)
		pygame.display.flip()


def main():
	pygame.init()
	screen = pygame.display.set_mode([screen_width,screen_height])

	done =  False
	clock = pygame.time.Clock()

	game = Game()

	while not done:
		done = game.process_events()

		game.run_logic()

		game.display_frame(screen)

		clock.tick(60)
	pygame.quit()

if __name__ == "__main__":
	main()