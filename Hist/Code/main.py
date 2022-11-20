import math
from time import sleep
import pygame
import pytmx
import pyscroll
from player import Player
from enemy import Enemy
import menu as mn

class Main():

    def __init__(self):

        pygame.init()

        self.screen = pygame.display.set_mode((1280, 720),0,32) 
        self.tmx_data = pytmx.util_pygame.load_pygame('../Tiled/tmx/Arene.tmx')
        map_data = pyscroll.data.TiledMapData(self.tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 1.25

        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)

        self.player_pos = self.tmx_data.get_object_by_name('SpawnArene')
        self.player = Player(self.player_pos.x, self.player_pos.y)

        self.enemy = Enemy(0, 0)

        self.group.add(self.player)
        self.group.add(self.enemy)

        self.collision = []

        self.barre_vie_full = pygame.image.load("../HUD/barrevie_full.png")
        self.barre_vie_1 = pygame.image.load("../HUD/1-.png")
        self.barre_vie_2 = pygame.image.load("../HUD/2-.png")
        self.barre_vie_3 = pygame.image.load("../HUD/3-.png")
        self.barre_vie_4 = pygame.image.load("../HUD/4-.png")
        self.barre_vie_5 = pygame.image.load("../HUD/5-.png")
        self.barre_vie_6 = pygame.image.load("../HUD/6-.png")
        self.barre_vie_7 = pygame.image.load("../HUD/7-.png")
        self.barre_vie_8 = pygame.image.load("../HUD/8-.png")
        self.barre_vie_9 = pygame.image.load("../HUD/9-.png")
        self.barre_vie_10 = pygame.image.load("../HUD/10-.png")
        self.barre_vie_11 = pygame.image.load("../HUD/11-.png")
        self.barre_vie_12 = pygame.image.load("../HUD/12-.png")
        self.barre_vie_13 = pygame.image.load("../HUD/13-.png")
        self.barre_vie_14 = pygame.image.load("../HUD/14-.png")
        self.barre_vie_15 = pygame.image.load("../HUD/15-.png")
        self.barre_vie_vide = pygame.image.load("../HUD/barrevie_vide.png")

        for obj in self.tmx_data.objects:
            self.collision.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        self.last_move = None

        self.vie = 16
        self.vie_enemy = 5
        self.vie_enemy_backup = 5

        self.enemy_kill = 0

        self.count_click = 10

        self.need_wait = False
        self.waiting_tick = 0

        self.waiting_tick2 = 0

        self.text_vie_ennemy = str(self.vie_enemy)
        self.text_ennemy_kill = str(self.enemy_kill)
        self.text_click_restant = str(self.count_click)

        self.font = pygame.font.SysFont('Comic Sans MS', 26)
        self.font2 = pygame.font.SysFont('Comic Sans MS', 70)

    def show_barre_vie(self, img, pv):
        if self.vie == pv:
            self.screen.blit(img, (35, 640))

    def refresh_screen(self): 
        self.group.update()
        self.group.center(self.player.rect.center)
        self.group.draw(self.screen)
        self.show_barre_vie(self.barre_vie_full, 16)
        self.show_barre_vie(self.barre_vie_1, 15)
        self.show_barre_vie(self.barre_vie_2, 14)
        self.show_barre_vie(self.barre_vie_3, 13)
        self.show_barre_vie(self.barre_vie_4, 12)
        self.show_barre_vie(self.barre_vie_5, 11)
        self.show_barre_vie(self.barre_vie_6, 10)
        self.show_barre_vie(self.barre_vie_7, 9)
        self.show_barre_vie(self.barre_vie_8, 8)
        self.show_barre_vie(self.barre_vie_9, 7)
        self.show_barre_vie(self.barre_vie_10, 6)
        self.show_barre_vie(self.barre_vie_11, 5)
        self.show_barre_vie(self.barre_vie_12, 4)
        self.show_barre_vie(self.barre_vie_13, 3)
        self.show_barre_vie(self.barre_vie_14, 2)
        self.show_barre_vie(self.barre_vie_15, 1)
        self.show_barre_vie(self.barre_vie_vide, 0)

        self.text_vie_ennemy = "Vie de ennemi : " + str(self.vie_enemy)
        self.text_ennemy_kill = str(self.enemy_kill)
        self.text_click_restant = "Clic restant : " + str(self.count_click)

        vie_enemy_rendu = self.font.render(self.text_vie_ennemy, False, (0, 0, 0))
        self.screen.blit(vie_enemy_rendu, (1000, 500))

        kill_ennemy_rendu = self.font.render(self.text_ennemy_kill, False, (0, 0, 0))
        self.screen.blit(kill_ennemy_rendu, (1200, 37))

        click_restant_rendu = self.font.render(self.text_click_restant, False, (0, 0, 0))
        self.screen.blit(click_restant_rendu, (1000, 550))

        if self.vie <= 0:
            self.screen.blit(self.barre_vie_vide, (35, 640))
        if self.need_wait == True:
            self.waiting_tick += 1
        self.waiting_tick2 += 1
        pygame.display.flip()

    def move_enemy(self):
        if len(self.player.position_15tick) <= 15:
            self.player.position_15tick.append(self.player.old_position)
        else:
            del self.player.position_15tick[0]
            self.player.position_15tick.append(self.player.old_position)

        self.enemy.position[0] = self.player.position_15tick[0][0] 
        self.enemy.position[1] = self.player.position_15tick[0][1]


    def anim_walk(self, anim1, anim2, anim3, anim4, anim5, anim6, direction, anim_end, key, last_move):
        key_prsd = pygame.key.get_pressed()
        self.last_move = last_move

        self.player.speed = 5
        self.player.animations(anim1)
        self.enemy.animations(anim1)
        self.refresh_screen() 
        self.move_enemy()
        sleep(0.1)
        direction()
        self.player.animations(anim2)
        self.enemy.animations(anim2)
        self.refresh_screen() 
        self.move_enemy()
        sleep(0.1)
        direction()
        self.player.animations(anim3)
        self.enemy.animations(anim3)
        self.refresh_screen() 
        self.move_enemy()
        sleep(0.1)
        direction()
        self.player.animations(anim4)
        self.enemy.animations(anim4)
        self.refresh_screen() 
        self.move_enemy()
        sleep(0.1)
        direction()
        self.player.animations(anim5)
        self.enemy.animations(anim5)
        self.refresh_screen() 
        self.move_enemy()
        sleep(0.1)
        direction()
        self.player.animations(anim6)
        self.player.animations(anim6)
        self.refresh_screen() 
        self.move_enemy()
        sleep(0.1)
        direction()

        if pygame.key.get_pressed()[key_prsd[key]] == False:
            self.player.animations(anim_end)

    def anim_run(self, anim1, anim2, direction, anim_end, key, last_move):
        key_prsd = pygame.key.get_pressed()
        self.last_move = last_move

        self.player.speed = 15
        self.player.animations(anim1)
        self.refresh_screen() 
        self.move_enemy()
        sleep(0.15)
        direction()
        self.player.animations(anim2)
        self.refresh_screen() 
        self.move_enemy()
        sleep(0.15)
        direction()

        if pygame.key.get_pressed()[key_prsd[key]] == False:
            self.player.animations(anim_end)

    def anim_jump(self, anim1, anim2, anim3, anim_end):
        key_prsd = pygame.key.get_pressed()

        self.player.animations(anim1)
        self.refresh_screen() 
        self.move_enemy()
        sleep(0.15)
        self.player.animations(anim2)
        self.refresh_screen() 
        self.move_enemy()
        sleep(0.15)
        self.player.animations(anim3)
        self.refresh_screen() 
        self.move_enemy()
        sleep(0.15)

        if pygame.key.get_pressed()[key_prsd[pygame.K_SPACE]] == False:
            self.player.animations(anim_end)

    def check_mvmt(self):

        key_prsd = pygame.key.get_pressed()

        if key_prsd[pygame.K_s] and not key_prsd[pygame.K_LCTRL]:
            self.anim_walk("mar1_dev", "mar2_dev", "mar3_dev", "mar4_dev", "mar5_dev", "mar6_dev", self.player.move_down, "idle_dev", pygame.K_s, 'down')

        if key_prsd[pygame.K_z] and not key_prsd[pygame.K_LCTRL]:
            self.anim_walk("mar1_der", "mar2_der", "mar3_der", "mar4_der", "mar5_der", "mar6_der", self.player.move_up, "idle_der", pygame.K_z, 'up')

        if key_prsd[pygame.K_q] and not key_prsd[pygame.K_LCTRL]:
            self.anim_walk("mar1_gau", "mar2_gau", "mar3_gau", "mar4_gau", "mar5_gau", "mar6_gau", self.player.move_left, "idle_gau", pygame.K_q, 'left')

        if key_prsd[pygame.K_d] and not key_prsd[pygame.K_LCTRL]:
            self.anim_walk("mar1_dro", "mar2_dro", "mar3_dro", "mar4_dro", "mar5_dro", "mar6_dro", self.player.move_right, "idle_dro", pygame.K_d, 'right')


        if key_prsd[pygame.K_s] and key_prsd[pygame.K_LCTRL]:
            self.anim_run("run1_dev", "run2_dev", self.player.move_down, "idle_dev", pygame.K_s, 'down')

        if key_prsd[pygame.K_z] and key_prsd[pygame.K_LCTRL]:
            self.anim_run("run1_der", "run2_der", self.player.move_up, "idle_der", pygame.K_z, 'up')

        if key_prsd[pygame.K_q] and key_prsd[pygame.K_LCTRL]:
            self.anim_run("run1_gau", "run2_gau", self.player.move_left, "idle_gau", pygame.K_q, 'left')

        if key_prsd[pygame.K_d] and key_prsd[pygame.K_LCTRL]:
            self.anim_run("run1_dro", "run2_dro", self.player.move_right, "idle_dro", pygame.K_d, 'right')

        if key_prsd[pygame.K_SPACE]:
            if self.last_move == 'down':
                self.anim_jump("jump1_dev", "jump2_dev", "jump3_dev","idle_dev")
            elif self.last_move == 'up':
                self.anim_jump("jump1_der", "jump2_der", "jump3_der","idle_der")
            elif self.last_move == 'left':
                self.anim_jump("jump1_gau", "jump2_gau", "jump3_gau","idle_gau")
            else:
                self.anim_jump("jump1_dro", "jump2_dro", "jump3_dro","idle_dro")

    def update_coll(self):

        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.collision) > -1:
                sprite.move_back() 
            
        if pygame.sprite.collide_rect(self.player, self.enemy):
            if pygame.mouse.get_pressed()[0] and self.count_click >= 1:
                self.count_click -= 1
                self.vie_enemy -= 1
            elif self.count_click == 0:
                if self.waiting_tick2 >= 10:
                    self.vie -= 1
                    self.waiting_tick2 = 0
                self.need_wait = True
            else:
                if self.waiting_tick2 >= 10:
                    self.vie -= 1
                    self.waiting_tick2 = 0

        if self.waiting_tick >= 10:
            self.count_click = 10
            self.need_wait = False
            self.waiting_tick = 0

        if self.vie_enemy <= 0:
            self.enemy.kill()
            self.enemy_kill += 1
            self.vie_enemy_backup = self.vie_enemy_backup + self.enemy_kill
            self.vie_enemy = self.vie_enemy_backup
            self.player.position_15tick = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
            self.enemy = Enemy(0, 0)
            self.group.add(self.enemy)
            if self.vie <= 11:
                self.vie += 5
            else:
                self.vie = 16

        if self.vie <= 0:
            perdu_txt = self.font.render("VOUS ETES MORT !", False, (255, 255, 255))
            self.screen.blit(perdu_txt, (500, 350))
            pygame.display.flip()
            sleep(3)
            menu = mn.Main()
            menu.main_menu()

    def run(self):
        running = True

        clock = pygame.time.Clock()

        while running:
            self.refresh_screen()
            self.check_mvmt()
            self.update_coll()  
            sleep(0.1)  
            self.move_enemy()    

            self.player.old_position = self.player.position.copy()

            self.screen.blit(self.barre_vie_full, (200, 1000))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False 

            clock.tick(60)
    