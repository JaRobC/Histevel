import pygame

class Enemy(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()

        self.all_sprite_pos = pygame.image.load("../Character/enemy/Gladiator Sprite Sheet.png")
        self.image = self.get_img(0, 0)
        self.image.set_colorkey([0, 0, 0])
        self.rect = pygame.Rect(0,0, self.image.get_rect().height * 0.5, 12)

        self.position = [x, y]
        self.old_position = [0, 0]

        self.speed = 5

        self.feet = pygame.Rect(0,0, self.image.get_rect().height * 0.5, 12)

        self.img_for_pos = {

            'idle_dro' : self.get_img(0, 0),
            'idle_gau' : self.get_img(0, 160),

            'mar1_gau' : self.get_img(768, 96),
            'mar2_gau' : self.get_img(864, 96),
            'mar3_gau' : self.get_img(960, 96),
            'mar4_gau' : self.get_img(1152, 96),
            'mar5_gau' : self.get_img(1248, 96),
            'mar6_gau' : self.get_img(1344, 96),

            'mar1_dro' : self.get_img(0, 96),
            'mar2_dro' : self.get_img(96, 96),
            'mar3_dro' : self.get_img(192, 96),
            'mar4_dro' : self.get_img(384, 96),
            'mar5_dro' : self.get_img(480, 96),
            'mar6_dro' : self.get_img(576, 96),

            'mar1_der' : self.get_img(768, 96),
            'mar2_der' : self.get_img(864, 96),
            'mar3_der' : self.get_img(960, 96),
            'mar4_der' : self.get_img(1152, 96),
            'mar5_der' : self.get_img(1248, 96),
            'mar6_der' : self.get_img(1344, 96),

            'mar1_dev' : self.get_img(0, 96),
            'mar2_dev' : self.get_img(96, 96),
            'mar3_dev' : self.get_img(192, 96),
            'mar4_dev' : self.get_img(384, 96),
            'mar5_dev' : self.get_img(480, 96),
            'mar6_dev' : self.get_img(576, 96),

        }

    def animations(self, anim_name):
        self.image = self.img_for_pos[anim_name]
        self.image.set_colorkey([0, 0, 0])
        self.rect = pygame.Rect(0,0, self.image.get_rect().height * 0.5, 12)
        self.update()

    def move_right(self): self.position[0] += self.speed
    def move_left(self): self.position[0] -= self.speed
    def move_up(self): self.position[1] -= self.speed
    def move_down(self): self.position[1] += self.speed

    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def move_back(self):
        self.position = self.old_position
        self.update()

    def get_img(self, x, y):
        image = pygame.Surface([96, 96])
        image.blit(self.all_sprite_pos, (0, 0), (x, y, 96, 96))
        return image