import pygame, sys     
mainClock = pygame.time.Clock()         
from pygame.locals import *             
import button

class Main:

    def __init__(self):
        pygame.init()

        self.logo = pygame.image.load('./assets/img/logo.png')
        pygame.display.set_icon(self.logo)
        pygame.display.set_caption('Histevel - Main Menu')      
        self.screen = pygame.display.set_mode((1280, 720),0,32)    
        font = pygame.font.Font('./assets/font.ttf', 52)             
        self.font = font  
        font2 = pygame.font.Font('./assets/font.ttf', 52)   
        self.font2 = font2
        self.background = pygame.image.load("./assets/img/bg.gif")    
        self.background = pygame.transform.scale(self.background, (1280, 720))
        self.isPlay = False                                                
        self.start_img = pygame.image.load('./assets/img/start_btn.png').convert_alpha()
        self.exit_img = pygame.image.load('./assets/img/exit_btn.png').convert_alpha()
        self.options_img = pygame.image.load('./assets/img/options+btn.png')
        self.start_img2 = pygame.image.load('./assets/img/start_btn2.png').convert_alpha()
        self.exit_img2 = pygame.image.load('./assets/img/exit_btn2.png').convert_alpha()
        self.options_img2 = pygame.image.load('./assets/img/optionsbtn2.png')

    def draw_text(self, text, font, color, suface, x, y):                 #
        self.textobj = font.render(text, 1, color)                       #   
        self.textrect = self.textobj.get_rect()                               #   Création de la fonction pour pouvoir afficher du text sur le Menu.
        self.textrect.topleft = (x, y)                                   #
        self.screen.blit(self.textobj, self.textrect)                              #

    def draw_numbers(self, variable, color,font, surface, x, y):          #
        self.variableobj = font.render(str(variable), 1, color)          #
        self.variablerect = self.variableobj.get_rect()                       #   Création de la fonction pour pouvoir afficher des nombres sur le Menu.
        self.variablerect.topleft = (x, y)                               #
        self.screen.blit(self.variableobj, self.variablerect)                      #

    def main_menu(self):       
                                                                 
        running = True                                                              
        if self.isPlay == False:
            self.isPlay = True
        
        while running:
            screen = self.screen
                                                   
            self.screen.fill((202, 228, 241))                                            
            self.screen.blit(self.background, (0, 0))                              
            self.draw_text('Histevel', self.font, (53,61,50), self.screen, 560, 40)      
            self.draw_text('Alpha 0.0.1', self.font2, (255, 255, 255), self.screen, 1010, 625)

            start_button = button.Button(540, 200, self.start_img, self.start_img2,0.8)
            exit_button = button.Button(555, 320, self.exit_img, self.exit_img2,0.8)
            options_button = button.Button(40, 600, self.options_img, self.options_img2,0.5)

            start_button.draw(screen, 'start')
            exit_button.draw(screen, 'exit')
            options_button.draw(screen, 'options')

            for event in pygame.event.get():            
                if event.type == QUIT:                  
                    pygame.quit()                       
                    sys.exit()                          
                if event.type == KEYDOWN:               
                    if event.key == K_ESCAPE:           
                        pygame.quit()                   
                        sys.exit()                      

            pygame.display.update()
            pygame.display.flip()

            mainClock.tick(60)
