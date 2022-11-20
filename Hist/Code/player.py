from time import sleep
import pygame

#On créer la classe joueur qui est un sprite (un personnage)
class Player(pygame.sprite.Sprite):

    #On créer la fonction qui s'effectuera au lancement du jeu
    def __init__(self, x, y):
        super().__init__()

        #On charge le perso
        self.sprite_sheet = pygame.image.load('../Character/char_a_p1/char_a_p1_0bas_humn_v01.png')
        self.image = self.get_img(34, 0)
        self.image.set_colorkey([0, 0, 0])
        self.rect = pygame.Rect(0,0, self.image.get_rect().height * 0.5, 12)

        #On lui donne ses positions comme étant x et y (modifiable donc)
        self.position = [x, y]

        #On attribue les différentes images selon l'animation
        self.position_15tick = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

        self.img_for_pos = {

            'idle_dev' : self.get_img(0, 0),
            'idle_der' : self.get_img(0, 96),
            'idle_dro' : self.get_img(0, 192),
            'idle_gau' : self.get_img(0, 288),

            'mar1_dev' : self.get_img(0, 384),
            'mar2_dev' : self.get_img(96, 384),
            'mar3_dev' : self.get_img(192, 384),
            'mar4_dev' : self.get_img(288, 384),
            'mar5_dev' : self.get_img(384, 384),
            'mar6_dev' : self.get_img(480, 384),

            'mar1_der' : self.get_img(0, 480),
            'mar2_der' : self.get_img(96, 480),
            'mar3_der' : self.get_img(192, 480),
            'mar4_der' : self.get_img(288, 480),
            'mar5_der' : self.get_img(384, 480),
            'mar6_der' : self.get_img(480, 480),

            'mar1_gau' : self.get_img(0, 672),
            'mar2_gau' : self.get_img(96, 672),
            'mar3_gau' : self.get_img(192, 672),
            'mar4_gau' : self.get_img(288, 672),
            'mar5_gau' : self.get_img(384, 672),
            'mar6_gau' : self.get_img(480, 672),

            'mar1_dro' : self.get_img(0, 576),
            'mar2_dro' : self.get_img(96, 576),
            'mar3_dro' : self.get_img(192, 576),
            'mar4_dro' : self.get_img(288, 576),
            'mar5_dro' : self.get_img(384, 576),
            'mar6_dro' : self.get_img(480, 576),

            'run1_dev' : self.get_img(576, 384),
            'run2_dev' : self.get_img(672, 384),

            'run1_der' : self.get_img(576, 480),
            'run2_der' : self.get_img(672, 480),

            'run1_gau' : self.get_img(576, 672),
            'run2_gau' : self.get_img(672, 672),

            'run1_dro' : self.get_img(576, 576),
            'run2_dro' : self.get_img(672, 576),

            'jump1_der' : self.get_img(480, 96),
            'jump2_der' : self.get_img(576, 96),
            'jump3_der' : self.get_img(672, 96),

            'jump1_dev' : self.get_img(480, 0),
            'jump2_dev' : self.get_img(576, 0),
            'jump3_dev' : self.get_img(672, 0),

            'jump1_dro' : self.get_img(480, 192),
            'jump2_dro' : self.get_img(576, 192),
            'jump3_dro' : self.get_img(672, 192),

            'jump1_gau' : self.get_img(480, 288),
            'jump2_gau' : self.get_img(576, 288),
            'jump3_gau' : self.get_img(672, 288),

        }

        #On effectue la zone des pieds (zone de collision)
        self.feet = pygame.Rect(0,0, self.image.get_rect().height * 0.5, 12)

        #On retiens son ancienne positions
        self.old_position = self.position.copy()

        #On lui donne une vitesse
        self.speed = 10

    #On créer la fonction qui nous permet de récupérer les images pour ensuite les animer (les mettres de bout en bout en gros)
    def animations(self, anim_name):
        self.image = self.img_for_pos[anim_name]
        self.image.set_colorkey([0, 0, 0])
        self.rect = pygame.Rect(0,0, self.image.get_rect().height * 0.5, 12)
        self.update() #On update l'image du perso

    #On définit la vitesse selon le mouvement du perso
    def move_right(self): self.position[0] += self.speed
    def move_left(self): self.position[0] -= self.speed
    def move_up(self): self.position[1] -= self.speed
    def move_down(self): self.position[1] += self.speed

    #On sauvegarde l'ancienne position
    def save_location(self): self.old_position = self.position.copy()

    #On créer la fonction qui permet de mettre à jour les images du perso
    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    #On créer une fonction qui permet de rétablir l'ancienne pos du joueur
    def move_back(self):
        self.position = self.old_position
        self.update()

    #On créer une fonction pour récup une image
    def get_img(self, x, y):
        image = pygame.Surface([96, 96])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 96, 96))
        return image