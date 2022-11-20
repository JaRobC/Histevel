import pygame, sys
mainClock = pygame.time.Clock()
from pygame.locals import *
from pygame import mixer
import button, sound

class Option():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Histevel - Options')
        self.screen = pygame.display.set_mode((1280, 720),0,32)    
        font = pygame.font.Font('./Code/assets/font.ttf', 52)            
        self.font = font 
        self.background = pygame.image.load("./Code/assets/img/bg2.gif")
        self.background = pygame.transform.scale(self.background, (1280, 720))
        self.isPlay = False
        self.exit_img = pygame.image.load('./Code/assets/img/exit_btn.png').convert_alpha()
        self.exit_img2 = pygame.image.load('./Code/assets/img/exit_btn2.png').convert_alpha()
        self.img_son = pygame.image.load('./Code/assets/img/sound.png')
        self.img_noson = pygame.image.load('./Code/assets/img/nosound.png')

    def draw_text(self, text, font, color, suface, x, y):           
        self.textobj = font.render(text, 1, color)                          
        self.textrect = self.textobj.get_rect()                               
        self.textrect.topleft = (x, y)                                   
        self.screen.blit(self.textobj, self.textrect)                        

    def draw_numbers(self, variable, color,font, surface, x, y):         
        self.variableobj = font.render(str(variable), 1, color)          
        self.variablerect = self.variableobj.get_rect()                    
        self.variablerect.topleft = (x, y)                               
        self.screen.blit(self.variableobj, self.variablerect)

    def options(self):
        if self.isPlay == False:
            self.isPlay = True
        running = True                                            
        while running:
            screen = self.screen                                                       
            self.screen.fill((202, 228, 241))                                            
            self.screen.blit(self.background, (0, 0))                              
            self.draw_text('Options', self.font, (0,0,0), self.screen, 560, 40)      
            self.draw_text('Alpha 0.0.1', self.font, (0, 0, 0), self.screen, 1010, 625)
            self.draw_text('Musique:', self.font, (255, 167, 76), self.screen, 1010, 225)


            exit_button = button.Button(50, 450, self.exit_img, self.exit_img2, 0.8)
            exit_button.draw(screen, 'return_menu')

            son = button.Button(1010, 325, self.img_son, self.img_noson, 0.2)
            son.draw(screen, 'pause')


            for event in pygame.event.get():            #
                if event.type == QUIT:                  #
                    pygame.quit()                       #
                    sys.exit()                          #
                if event.type == KEYDOWN:               #
                    if event.key == K_ESCAPE:           # Déclaration des conditions utilisés pour chaque events (clique, exit...). [*]
                        pygame.quit()                   #
                        sys.exit()                      #
            # Mise à jour de l'affichage.
            pygame.display.update()
            pygame.display.flip()

            # On définit les ticks de notre jeu (le temps pour éviter que cela soit trop rapide).
            mainClock.tick(60)
