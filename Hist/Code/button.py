import sys, pygame, option
import menu as mn
import sound as sd
import main as main_game

class Button():
	def __init__(self, x, y, image, image2, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.effect = pygame.mixer.Sound('./songs/sound.mp3')
		self.image2 = pygame.transform.scale(image2, (int(width * scale), int(height * scale)))
		self.music = True

	def draw(self, surface, name):
		pos = pygame.mouse.get_pos()

	#####################--MENU--#############################
		if name == 'exit':
			if self.rect.collidepoint(pos):
				surface.blit(self.image2, (self.rect.x, self.rect.y))
				for event in pygame.event.get():
					if event.type == pygame.MOUSEBUTTONDOWN:
						self.effect.play()
						sys.exit()
			else:
				surface.blit(self.image, (self.rect.x, self.rect.y))

		if name == 'start':
			if self.rect.collidepoint(pos):
				surface.blit(self.image2, (self.rect.x, self.rect.y))
				for event in pygame.event.get():
					if event.type == pygame.MOUSEBUTTONDOWN:
						self.effect.play()
						main_start = main_game.Main()
						main_start.run()
						sys.exit()
			else:
				surface.blit(self.image, (self.rect.x, self.rect.y))
		
		if name == 'options':
			if self.rect.collidepoint(pos):
				surface.blit(self.image2, (self.rect.x, self.rect.y))
				for event in pygame.event.get():
					if event.type == pygame.MOUSEBUTTONDOWN:
						self.effect.play()
						settings = option.Option()
						settings.options()
			else:
				surface.blit(self.image, (self.rect.x, self.rect.y))

##############################--Option--#####################
		if name == 'return_menu':
			if self.rect.collidepoint(pos):
				surface.blit(self.image2, (self.rect.x, self.rect.y))
				for event in pygame.event.get():
					if event.type == pygame.MOUSEBUTTONDOWN:
						self.effect.play()
						main = mn.Main()
						main.main_menu()
			else:
				surface.blit(self.image, (self.rect.x, self.rect.y))

		if name == 'pause':

			if self.music == True:
				surface.blit(self.image, (self.rect.x, self.rect.y))
			else:
				surface.blit(self.image2, (self.rect.x, self.rect.y))

			if self.rect.collidepoint(pos):
					for event in pygame.event.get():
						if event.type == pygame.MOUSEBUTTONDOWN:
							self.music = False
