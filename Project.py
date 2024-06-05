import pygame
from sys import exit
def end_of_game():
     global text_surf
     if player_1_health <= 0:
          text_surf = test_font.render('REBECCA WINS!!', False, RED)
     if player_2_health <=0:
          text_surf = test_font.render('BOB 2 WINS!!', False, RED)


def walk_p1():
    global  player_1_surf, player_index_1
    if player_1_rect.y <= 300:
        player_index_1 += 1
        if player_index_1 >= len(player1_walk_animation):
            player_index_1 = 0
        player_1_surf = player1_walk_animation[int(player_index_1)]


def walk_p2():
    global player_index_2, player_2_surf
    player_index_2 += 1
    if player_index_2 >= len(player2_walk_animation):
        player_index_2 = 0
    player_2_surf = player2_walk_animation[int(player_index_2)]


def attack_p1():
        global  player_1_surf, player_index_1
        player_index_1 += 1
        if player_index_1 >= len(player1_attack_animation):
            player_index_1 = 0
        player_1_surf = player1_attack_animation[int(player_index_1)]


def attack_p2():
        global player_index_2, player_2_surf
        player_index_2 += 1
        if player_index_2 >= len(player2_attack_animation):
            player_index_2 = 0
        player_2_surf = player2_attack_animation[int(player_index_2)]
        
def throw_attack_p1():
    global  player_1_surf, player_index_1
    player_index_1 += 1
    if player_index_1 >= len(player1_throw_animation):
        player_index_1 = 0
    player_1_surf = player1_throw_animation[int(player_index_1)]

def jump_throw_attack_p1():
    global  player_1_surf, player_index_1
    player_index_1 += 1
    if player_index_1 >= len(player1_jump_throw_animation):
        player_index_1 = 0
    player_1_surf = player1_jump_throw_animation[int(player_index_1)]

def throw_attack_p2():
        global player_index_2, player_2_surf
        player_index_2 += 1
        if player_index_2 >= len(player2_throw_animation):
            player_index_2 = 0
        player_2_surf = player2_throw_animation[int(player_index_2)]


def jump_throw_attack_p2():
        global player_index_2, player_2_surf
        player_index_2 += 1
        if player_index_2 >= len(player2_jump_throw_animation):
            player_index_2 = 0
        player_2_surf = player2_jump_throw_animation[int(player_index_2)]




def player_animation_p1():
    global player_1_surf, player_index_1, player_jump_index_1
    
    if player_1_rect.bottom < 300:
        player_jump_index_1 += 0.2 
        if player_jump_index_1 >= len(player1_jump_animation):
            player_jump_index_1 = 0
        player_1_surf = player1_jump_animation[int(player_jump_index_1)]

    else:
        player_jump_index_1 = 0
        player_index_1 += 0.1
        if player_index_1 >= len(player1_idle_animation):
            player_index_1 = 0
        player_1_surf = player1_idle_animation[int(player_index_1)]

def player_animation_p2():
    global player_index_2, player_2_surf, player_jump_index_2
    if player_2_rect.bottom < 300:
        player_jump_index_2 += 0.2 
        if player_jump_index_2 >= len(player2_jump_animation):
            player_jump_index_2 = 0
        player_2_surf = player2_jump_animation[int(player_jump_index_2)]

    else:
        player_jump_index_2 = 0
        player_index_2 += 0.1
        if player_index_2 >= len(player2_idle_animation):
            player_index_2 = 0
        player_2_surf = player2_idle_animation[int(player_index_2)]

    

    


pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Fighter')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

game_active = True
kunai_held_p1 = True
kunai_held_p2 = True


player_1_gravity = 0
player_2_gravity = 0



player_index_1 = int(0)
player_index_2 = int(0)
player_jump_index_1 = int(0)
player_jump_index_2 = int(0)

test_surf = pygame.image.load('graphics/Sky.png').convert()
ground_surf = pygame.image.load('graphics/ground.png').convert()
text_surf = test_font.render('     FIGHT!!', False, 'Red')
player_1_surf = pygame.image.load('graphics/ninja_1/Idle__000.png').convert_alpha()
player_1_surf = pygame.transform.scale(player_1_surf, (65,100))
player_1_mask = pygame.mask.from_surface(player_1_surf)
player_2_surf = pygame.image.load('graphics/ninja_2/Idle__000.png').convert_alpha()
player_2_surf = pygame.transform.scale(player_2_surf, (95,100))
player_2_surf = pygame.transform.flip(player_2_surf, True, False)
player_2_mask = pygame.mask.from_surface(player_2_surf)
player_1_rect = player_1_surf.get_rect(midbottom = (150,300))
player_2_rect = player_2_surf.get_rect(midbottom = (600,300))
kunai_player_1 = pygame.image.load('graphics/ninja_1/Kunai.png').convert_alpha()
kunai_player_1 = pygame.transform.rotate(kunai_player_1, (270))
kunai_player_1 = pygame.transform.scale(kunai_player_1, (50,20))
kunai_player_1_mask = pygame.mask.from_surface(kunai_player_1)
kunai_rect = kunai_player_1.get_rect(topleft = player_1_rect.topright)
kunai_player_2 = pygame.image.load('graphics/ninja_2/Kunai.png').convert_alpha()
kunai_player_2 = pygame.transform.rotate(kunai_player_2, (180))
kunai_player_2 = pygame.transform.scale(kunai_player_2, (50,20))
kunai_player_2_mask = pygame.mask.from_surface(kunai_player_2)
kunai_rect_2 = kunai_player_2.get_rect(topright = player_2_rect.topleft)


#Health_________________________________________________________________________________
RED = (255, 0, 0)
GREEN = (0, 255, 0)
player_1_health = 1500
player_2_health = 1500




###_________________________________________________________________________________
#IDLE animation p1
###_________________________________________________________________________________
player1_idle_1 = pygame.image.load('graphics/ninja_1/Idle__001.png').convert_alpha()
player1_idle_1= pygame.transform.scale(player1_idle_1, (65,100))
player1_idle_2 = pygame.image.load('graphics/ninja_1/Idle__002.png').convert_alpha()
player1_idle_2 = pygame.transform.scale(player1_idle_2, (65,100))
player1_idle_3 = pygame.image.load('graphics/ninja_1/Idle__003.png').convert_alpha()
player1_idle_3 = pygame.transform.scale(player1_idle_3, (65,100))
player1_idle_4 = pygame.image.load('graphics/ninja_1/Idle__004.png').convert_alpha()
player1_idle_4 = pygame.transform.scale(player1_idle_4, (65,100))
player1_idle_5 = pygame.image.load('graphics/ninja_1/Idle__005.png').convert_alpha()
player1_idle_5 = pygame.transform.scale(player1_idle_5, (65,100))
player1_idle_6 = pygame.image.load('graphics/ninja_1/Idle__006.png').convert_alpha()
player1_idle_6 = pygame.transform.scale(player1_idle_6, (65,100))
player1_idle_7 = pygame.image.load('graphics/ninja_1/Idle__007.png').convert_alpha()
player1_idle_7 = pygame.transform.scale(player1_idle_7, (65,100))
player1_idle_8 = pygame.image.load('graphics/ninja_1/Idle__008.png').convert_alpha()
player1_idle_8 = pygame.transform.scale(player1_idle_8, (65,100))
player1_idle_9 = pygame.image.load('graphics/ninja_1/Idle__009.png').convert_alpha()
player1_idle_9 = pygame.transform.scale(player1_idle_9, (65,100))

player1_idle_animation = [player_1_surf,player1_idle_1, player1_idle_2, player1_idle_3, player1_idle_4, player1_idle_5, player1_idle_6, player1_idle_7, player1_idle_8, player1_idle_9]
###_________________________________________________________________________________
#IDLE animation p2
###_________________________________________________________________________________
player2_idle_1 = pygame.image.load('graphics/ninja_2/Idle__001.png').convert_alpha()
player2_idle_1= pygame.transform.scale(player2_idle_1, (65,100))
player2_idle_1 = pygame.transform.flip(player2_idle_1, True, False)
player2_idle_2 = pygame.image.load('graphics/ninja_2/Idle__002.png').convert_alpha()
player2_idle_2 = pygame.transform.scale(player2_idle_2, (65,100))
player2_idle_2 = pygame.transform.flip(player2_idle_2, True, False)
player2_idle_3 = pygame.image.load('graphics/ninja_2/Idle__003.png').convert_alpha()
player2_idle_3 = pygame.transform.scale(player2_idle_3, (65,100))
player2_idle_3 = pygame.transform.flip(player2_idle_3, True, False)
player2_idle_4 = pygame.image.load('graphics/ninja_2/Idle__004.png').convert_alpha()
player2_idle_4 = pygame.transform.scale(player2_idle_4, (65,100))
player2_idle_4 = pygame.transform.flip(player2_idle_4, True, False)
player2_idle_5 = pygame.image.load('graphics/ninja_2/Idle__005.png').convert_alpha()
player2_idle_5 = pygame.transform.scale(player2_idle_5, (65,100))
player2_idle_5 = pygame.transform.flip(player2_idle_5, True, False)
player2_idle_6 = pygame.image.load('graphics/ninja_2/Idle__006.png').convert_alpha()
player2_idle_6 = pygame.transform.scale(player2_idle_6, (65,100))
player2_idle_6 = pygame.transform.flip(player2_idle_6, True, False)
player2_idle_7 = pygame.image.load('graphics/ninja_2/Idle__007.png').convert_alpha()
player2_idle_7 = pygame.transform.scale(player2_idle_7, (65,100))
player2_idle_7 = pygame.transform.flip(player2_idle_7, True, False)
player2_idle_8 = pygame.image.load('graphics/ninja_2/Idle__008.png').convert_alpha()
player2_idle_8 = pygame.transform.scale(player2_idle_8, (65,100))
player2_idle_8 = pygame.transform.flip(player2_idle_8, True, False)
player2_idle_9 = pygame.image.load('graphics/ninja_2/Idle__009.png').convert_alpha()
player2_idle_9 = pygame.transform.scale(player2_idle_9, (65,100))
player2_idle_9 = pygame.transform.flip(player2_idle_9, True,False)

player2_idle_animation = [player2_idle_1, player2_idle_2, player2_idle_3, player2_idle_4, player2_idle_5, player2_idle_6, player2_idle_7, player2_idle_8, player2_idle_9]

###_________________________________________________________________________________
#ATTACK p1
###_________________________________________________________________________________
player1_attack_0 = pygame.image.load('graphics/ninja_1/Attack__000.png').convert_alpha()
player1_attack_0= pygame.transform.scale(player1_attack_0, (130,115))
player1_attack_1 = pygame.image.load('graphics/ninja_1/Attack__001.png').convert_alpha()
player1_attack_1= pygame.transform.scale(player1_attack_1, (130,115))
player1_attack_2 = pygame.image.load('graphics/ninja_1/Attack__002.png').convert_alpha()
player1_attack_2 = pygame.transform.scale(player1_attack_2, (130,115))
player1_attack_3 = pygame.image.load('graphics/ninja_1/Attack__003.png').convert_alpha()
player1_attack_3 = pygame.transform.scale(player1_attack_3, (130,115))
player1_attack_4 = pygame.image.load('graphics/ninja_1/Attack__004.png').convert_alpha()
player1_attack_4 = pygame.transform.scale(player1_attack_4, (130,115))
player1_attack_5 = pygame.image.load('graphics/ninja_1/Attack__005.png').convert_alpha()
player1_attack_5 = pygame.transform.scale(player1_attack_5, (130,115))
player1_attack_6 = pygame.image.load('graphics/ninja_1/Attack__006.png').convert_alpha()
player1_attack_6 = pygame.transform.scale(player1_attack_6, (130,115))
player1_attack_7 = pygame.image.load('graphics/ninja_1/Attack__007.png').convert_alpha()
player1_attack_7 = pygame.transform.scale(player1_attack_7, (130,115))
player1_attack_8 = pygame.image.load('graphics/ninja_1/Attack__008.png').convert_alpha()
player1_attack_8 = pygame.transform.scale(player1_attack_8, (130,115))
player1_attack_9 = pygame.image.load('graphics/ninja_1/Attack__009.png').convert_alpha()
player1_attack_9 = pygame.transform.scale(player1_attack_9, (130,115))

player1_attack_animation = [player1_attack_0, player1_attack_1, player1_attack_2, player1_attack_3, player1_attack_4, player1_attack_5, player1_attack_6, player1_attack_7, player1_attack_8, player1_attack_9]

player1_throw_0 = pygame.image.load('graphics/ninja_1/Throw__000.png').convert_alpha()
player1_throw_0= pygame.transform.scale(player1_throw_0, (130,115))
player1_throw_1 = pygame.image.load('graphics/ninja_1/Throw__001.png').convert_alpha()
player1_throw_1= pygame.transform.scale(player1_throw_1, (130,115))
player1_throw_2 = pygame.image.load('graphics/ninja_1/Throw__002.png').convert_alpha()
player1_throw_2 = pygame.transform.scale(player1_throw_2, (130,115))
player1_throw_3 = pygame.image.load('graphics/ninja_1/Throw__003.png').convert_alpha()
player1_throw_3 = pygame.transform.scale(player1_throw_3, (130,115))
player1_throw_4 = pygame.image.load('graphics/ninja_1/Throw__004.png').convert_alpha()
player1_throw_4 = pygame.transform.scale(player1_throw_4, (130,115))
player1_throw_5 = pygame.image.load('graphics/ninja_1/Throw__005.png').convert_alpha()
player1_throw_5 = pygame.transform.scale(player1_throw_5, (130,115))
player1_throw_6 = pygame.image.load('graphics/ninja_1/Throw__006.png').convert_alpha()
player1_throw_6 = pygame.transform.scale(player1_throw_6, (130,115))
player1_throw_7 = pygame.image.load('graphics/ninja_1/Throw__007.png').convert_alpha()
player1_throw_7 = pygame.transform.scale(player1_throw_7, (130,115))
player1_throw_8 = pygame.image.load('graphics/ninja_1/Throw__008.png').convert_alpha()
player1_throw_8 = pygame.transform.scale(player1_throw_8, (130,115))
player1_throw_9 = pygame.image.load('graphics/ninja_1/Throw__009.png').convert_alpha()
player1_throw_9 = pygame.transform.scale(player1_throw_9, (130,115))

player1_throw_animation = [player1_throw_0, player1_throw_1, player1_throw_2, player1_throw_3, player1_throw_4, player1_throw_5, player1_throw_6, player1_throw_7, player1_throw_8, player1_throw_9]

player1_jump_throw_0 = pygame.image.load('graphics/ninja_1/Jump_Throw__000.png').convert_alpha()
player1_jump_throw_0= pygame.transform.scale(player1_jump_throw_0, (130,115))
player1_jump_throw_1 = pygame.image.load('graphics/ninja_1/Jump_Throw__001.png').convert_alpha()
player1_jump_throw_1= pygame.transform.scale(player1_jump_throw_1, (130,115))
player1_jump_throw_2 = pygame.image.load('graphics/ninja_1/Jump_Throw__003.png').convert_alpha()
player1_jump_throw_2 = pygame.transform.scale(player1_jump_throw_2, (130,115))
player1_jump_throw_3 = pygame.image.load('graphics/ninja_1/Jump_Throw__003.png').convert_alpha()
player1_jump_throw_3 = pygame.transform.scale(player1_jump_throw_3, (130,115))
player1_jump_throw_4 = pygame.image.load('graphics/ninja_1/Jump_Throw__004.png').convert_alpha()
player1_jump_throw_4 = pygame.transform.scale(player1_jump_throw_4, (130,115))
player1_jump_throw_5 = pygame.image.load('graphics/ninja_1/Jump_Throw__005.png').convert_alpha()
player1_jump_throw_5 = pygame.transform.scale(player1_jump_throw_5, (130,115))
player1_jump_throw_6 = pygame.image.load('graphics/ninja_1/Jump_Throw__006.png').convert_alpha()
player1_jump_throw_6 = pygame.transform.scale(player1_jump_throw_6, (130,115))
player1_jump_throw_7 = pygame.image.load('graphics/ninja_1/Jump_Throw__007.png').convert_alpha()
player1_jump_throw_7 = pygame.transform.scale(player1_jump_throw_7, (130,115))
player1_jump_throw_8 = pygame.image.load('graphics/ninja_1/Jump_Throw__008.png').convert_alpha()
player1_jump_throw_8 = pygame.transform.scale(player1_jump_throw_8, (130,115))
player1_jump_throw_9 = pygame.image.load('graphics/ninja_1/Jump_Throw__009.png').convert_alpha()
player1_jump_throw_9 = pygame.transform.scale(player1_jump_throw_9, (130,115))

player1_jump_throw_animation = [player1_jump_throw_0,player1_jump_throw_1, player1_jump_throw_2, player1_jump_throw_3, player1_jump_throw_4, player1_jump_throw_5, player1_jump_throw_6, player1_jump_throw_7, player1_jump_throw_8, player1_jump_throw_9]
###_________________________________________________________________________________
#ATTACK p2
###_________________________________________________________________________________
player2_attack_0 = pygame.image.load('graphics/ninja_2/Attack__000.png').convert_alpha()
player2_attack_0= pygame.transform.scale(player2_attack_0, (110,110))
player2_attack_0 = pygame.transform.flip(player2_attack_0, True, False)
player2_attack_1 = pygame.image.load('graphics/ninja_2/Attack__001.png').convert_alpha()
player2_attack_1= pygame.transform.scale(player2_attack_1, (110,110))
player2_attack_1 = pygame.transform.flip(player2_attack_1, True, False)
player2_attack_2 = pygame.image.load('graphics/ninja_2/Attack__002.png').convert_alpha()
player2_attack_2 = pygame.transform.scale(player2_attack_2, (110,110))
player2_attack_2 = pygame.transform.flip(player2_attack_2, True, False)
player2_attack_3 = pygame.image.load('graphics/ninja_2/Attack__003.png').convert_alpha()
player2_attack_3 = pygame.transform.scale(player2_attack_3, (110,110))
player2_attack_3 = pygame.transform.flip(player2_attack_3, True, False)
player2_attack_4 = pygame.image.load('graphics/ninja_2/Attack__004.png').convert_alpha()
player2_attack_4 = pygame.transform.scale(player2_attack_4, (110,110))
player2_attack_4 = pygame.transform.flip(player2_attack_4, True, False)
player2_attack_5 = pygame.image.load('graphics/ninja_2/Attack__005.png').convert_alpha()
player2_attack_5 = pygame.transform.scale(player2_attack_5, (110,110))
player2_attack_5 = pygame.transform.flip(player2_attack_5, True, False)
player2_attack_6 = pygame.image.load('graphics/ninja_2/Attack__006.png').convert_alpha()
player2_attack_6 = pygame.transform.scale(player2_attack_6, (110,110))
player2_attack_6 = pygame.transform.flip(player2_attack_6, True, False)
player2_attack_7 = pygame.image.load('graphics/ninja_2/Attack__007.png').convert_alpha()
player2_attack_7 = pygame.transform.scale(player2_attack_7, (110,110))
player2_attack_7 = pygame.transform.flip(player2_attack_7, True, False)
player2_attack_8 = pygame.image.load('graphics/ninja_2/Attack__008.png').convert_alpha()
player2_attack_8 = pygame.transform.scale(player2_attack_8, (110,110))
player2_attack_8 = pygame.transform.flip(player2_attack_8, True, False)
player2_attack_9 = pygame.image.load('graphics/ninja_2/Attack__009.png').convert_alpha()
player2_attack_9 = pygame.transform.scale(player2_attack_9, (110,110))
player2_attack_9 = pygame.transform.flip(player2_attack_9, True, False)

player2_attack_animation = [player2_attack_0, player2_attack_1, player2_attack_2, player2_attack_3, player2_attack_4, player2_attack_5, player2_attack_6, player2_attack_7, player2_attack_8, player2_attack_9]


player2_throw_0 = pygame.image.load('graphics/ninja_2/Throw__000.png').convert_alpha()
player2_throw_0= pygame.transform.scale(player2_throw_0, (110,110))
player2_throw_0 = pygame.transform.flip(player2_throw_0, True, False)
player2_throw_1 = pygame.image.load('graphics/ninja_2/Throw__001.png').convert_alpha()
player2_throw_1= pygame.transform.scale(player2_throw_1, (110,110))
player2_throw_1 = pygame.transform.flip(player2_throw_1, True, False)
player2_throw_2 = pygame.image.load('graphics/ninja_2/Throw__002.png').convert_alpha()
player2_throw_2 = pygame.transform.scale(player2_throw_2, (110,110))
player2_throw_2 = pygame.transform.flip(player2_throw_2, True, False)
player2_throw_3 = pygame.image.load('graphics/ninja_2/Throw__003.png').convert_alpha()
player2_throw_3 = pygame.transform.scale(player2_throw_3, (110,110))
player2_throw_3 = pygame.transform.flip(player2_throw_3, True, False)
player2_throw_4 = pygame.image.load('graphics/ninja_2/Throw__004.png').convert_alpha()
player2_throw_4 = pygame.transform.scale(player2_throw_4, (110,110))
player2_throw_4 = pygame.transform.flip(player2_throw_4, True, False)
player2_throw_5 = pygame.image.load('graphics/ninja_2/Throw__005.png').convert_alpha()
player2_throw_5 = pygame.transform.scale(player2_throw_5, (110,110))
player2_throw_5 = pygame.transform.flip(player2_throw_5, True, False)
player2_throw_6 = pygame.image.load('graphics/ninja_2/Throw__006.png').convert_alpha()
player2_throw_6 = pygame.transform.scale(player2_throw_6, (110,110))
player2_throw_6 = pygame.transform.flip(player2_throw_6, True, False)
player2_throw_7 = pygame.image.load('graphics/ninja_2/Throw__007.png').convert_alpha()
player2_throw_7 = pygame.transform.scale(player2_throw_7, (110,110))
player2_throw_7 = pygame.transform.flip(player2_throw_7, True, False)
player2_throw_8 = pygame.image.load('graphics/ninja_2/Throw__008.png').convert_alpha()
player2_throw_8 = pygame.transform.scale(player2_throw_8, (110,110))
player2_throw_8 = pygame.transform.flip(player2_throw_8, True, False)
player2_throw_9 = pygame.image.load('graphics/ninja_2/Throw__009.png').convert_alpha()
player2_throw_9 = pygame.transform.scale(player2_throw_9, (110,110))
player2_throw_9 = pygame.transform.flip(player2_throw_9, True, False)

player2_throw_animation = [player2_throw_0, player2_throw_1, player2_throw_2, player2_throw_3, player2_throw_4, player2_throw_5, player2_throw_6, player2_throw_7, player2_throw_8, player2_throw_9]

player2_jump_throw_0 = pygame.image.load('graphics/ninja_2/Jump_Throw__000.png').convert_alpha()
player2_jump_throw_0= pygame.transform.scale(player2_jump_throw_0, (110,110))
player2_jump_throw_0 = pygame.transform.flip(player2_jump_throw_0, True, False)
player2_jump_throw_1 = pygame.image.load('graphics/ninja_2/Jump_Throw__001.png').convert_alpha()
player2_jump_throw_1= pygame.transform.scale(player2_jump_throw_1, (110,110))
player2_jump_throw_1 = pygame.transform.flip(player2_jump_throw_1, True, False)
player2_jump_throw_2 = pygame.image.load('graphics/ninja_2/Jump_Throw__002.png').convert_alpha()
player2_jump_throw_2 = pygame.transform.scale(player2_jump_throw_2, (110,110))
player2_jump_throw_2 = pygame.transform.flip(player2_jump_throw_2, True, False)
player2_jump_throw_3 = pygame.image.load('graphics/ninja_2/Jump_Throw__003.png').convert_alpha()
player2_jump_throw_3 = pygame.transform.scale(player2_jump_throw_3, (110,110))
player2_jump_throw_3 = pygame.transform.flip(player2_jump_throw_3, True, False)
player2_jump_throw_4 = pygame.image.load('graphics/ninja_2/Jump_Throw__004.png').convert_alpha()
player2_jump_throw_4 = pygame.transform.scale(player2_jump_throw_4, (110,110))
player2_jump_throw_4 = pygame.transform.flip(player2_jump_throw_4, True, False)
player2_jump_throw_5 = pygame.image.load('graphics/ninja_2/Jump_Throw__005.png').convert_alpha()
player2_jump_throw_5 = pygame.transform.scale(player2_jump_throw_5, (110,110))
player2_jump_throw_5 = pygame.transform.flip(player2_jump_throw_5, True, False)
player2_jump_throw_6 = pygame.image.load('graphics/ninja_2/Jump_Throw__006.png').convert_alpha()
player2_jump_throw_6 = pygame.transform.scale(player2_jump_throw_6, (110,110))
player2_jump_throw_6 = pygame.transform.flip(player2_jump_throw_6, True, False)
player2_jump_throw_7 = pygame.image.load('graphics/ninja_2/Jump_Throw__007.png').convert_alpha()
player2_jump_throw_7 = pygame.transform.scale(player2_jump_throw_7, (110,110))
player2_jump_throw_7 = pygame.transform.flip(player2_jump_throw_7, True, False)
player2_jump_throw_8 = pygame.image.load('graphics/ninja_2/Jump_Throw__008.png').convert_alpha()
player2_jump_throw_8 = pygame.transform.scale(player2_jump_throw_8, (110,110))
player2_jump_throw_8 = pygame.transform.flip(player2_jump_throw_8, True, False)
player2_jump_throw_9 = pygame.image.load('graphics/ninja_2/Jump_Throw__009.png').convert_alpha()
player2_jump_throw_9 = pygame.transform.scale(player2_jump_throw_9, (110,110))
player2_jump_throw_9 = pygame.transform.flip(player2_jump_throw_9, True, False)

player2_jump_throw_animation = [player2_jump_throw_0, player2_jump_throw_1, player2_jump_throw_2, player2_jump_throw_3, player2_jump_throw_4, player2_jump_throw_5, player2_jump_throw_6, player2_jump_throw_7, player2_jump_throw_8, player2_jump_throw_9]



###_________________________________________________________________________________
#Player 1 jump
###_________________________________________________________________________________
player1_jump_0 = pygame.image.load('graphics/ninja_1/Jump__000.png').convert_alpha()
player1_jump_0 = pygame.transform.scale(player1_jump_0, (120,100))
player1_jump_1 = pygame.image.load('graphics/ninja_1/Jump__001.png').convert_alpha()
player1_jump_1 = pygame.transform.scale(player1_jump_1, (120,100))
player1_jump_2 = pygame.image.load('graphics/ninja_1/Jump__002.png').convert_alpha()
player1_jump_2 = pygame.transform.scale(player1_jump_2, (120,100))
player1_jump_3 = pygame.image.load('graphics/ninja_1/Jump__003.png').convert_alpha()
player1_jump_3 = pygame.transform.scale(player1_jump_3, (120,100))
player1_jump_4 = pygame.image.load('graphics/ninja_1/Jump__004.png').convert_alpha()
player1_jump_4 = pygame.transform.scale(player1_jump_4, (120,100))
player1_jump_5 = pygame.image.load('graphics/ninja_1/Jump__005.png').convert_alpha()
player1_jump_5 = pygame.transform.scale(player1_jump_5, (120,100))
player1_jump_6 = pygame.image.load('graphics/ninja_1/Jump__006.png').convert_alpha()
player1_jump_6 = pygame.transform.scale(player1_jump_6, (120,100))
player1_jump_7 = pygame.image.load('graphics/ninja_1/Jump__007.png').convert_alpha()
player1_jump_7 = pygame.transform.scale(player1_jump_7, (120,100))
player1_jump_8 = pygame.image.load('graphics/ninja_1/Jump__008.png').convert_alpha()
player1_jump_8 = pygame.transform.scale(player1_jump_8, (120,100))
player1_jump_9 = pygame.image.load('graphics/ninja_1/Jump__009.png').convert_alpha()
player1_jump_9 = pygame.transform.scale(player1_jump_9, (120,100))

player1_jump_animation = [player1_jump_0, player1_jump_1, player1_jump_2, player1_jump_3, player1_jump_4, player1_jump_5, player1_jump_6, player1_jump_7, player1_jump_8, player1_jump_9]

###_________________________________________________________________________________
#Player 2 jump
###_________________________________________________________________________________
player2_jump_0 = pygame.image.load('graphics/ninja_2/Jump__000.png').convert_alpha()
player2_jump_0 = pygame.transform.scale(player2_jump_0, (120,100))
player2_jump_0 = pygame.transform.flip(player2_jump_0, True, False)
player2_jump_1 = pygame.image.load('graphics/ninja_2/Jump__001.png').convert_alpha()
player2_jump_1 = pygame.transform.scale(player2_jump_1, (120,100))
player2_jump_1 = pygame.transform.flip(player2_jump_1, True, False)
player2_jump_2 = pygame.image.load('graphics/ninja_2/Jump__002.png').convert_alpha()
player2_jump_2 = pygame.transform.scale(player2_jump_2, (120,100))
player2_jump_2 = pygame.transform.flip(player2_jump_2, True, False)
player2_jump_3 = pygame.image.load('graphics/ninja_2/Jump__003.png').convert_alpha()
player2_jump_3 = pygame.transform.scale(player2_jump_3, (120,100))
player2_jump_3 = pygame.transform.flip(player2_jump_3, True, False)
player2_jump_4 = pygame.image.load('graphics/ninja_2/Jump__004.png').convert_alpha()
player2_jump_4 = pygame.transform.scale(player2_jump_4, (120,100))
player2_jump_4 = pygame.transform.flip(player2_jump_4, True, False)
player2_jump_5 = pygame.image.load('graphics/ninja_2/Jump__005.png').convert_alpha()
player2_jump_5 = pygame.transform.scale(player2_jump_5, (120,100))
player2_jump_5 = pygame.transform.flip(player2_jump_5, True, False)
player2_jump_6 = pygame.image.load('graphics/ninja_2/Jump__006.png').convert_alpha()
player2_jump_6 = pygame.transform.scale(player2_jump_6, (120,100))
player2_jump_6 = pygame.transform.flip(player2_jump_6, True, False)
player2_jump_7 = pygame.image.load('graphics/ninja_2/Jump__007.png').convert_alpha()
player2_jump_7 = pygame.transform.scale(player2_jump_7, (120,100))
player2_jump_7 = pygame.transform.flip(player2_jump_7, True, False)
player2_jump_8 = pygame.image.load('graphics/ninja_2/Jump__008.png').convert_alpha()
player2_jump_8 = pygame.transform.scale(player2_jump_8, (120,100))
player2_jump_8 = pygame.transform.flip(player2_jump_8, True, False)
player2_jump_9 = pygame.image.load('graphics/ninja_2/Jump__009.png').convert_alpha()
player2_jump_9 = pygame.transform.scale(player2_jump_9, (120,100))
player2_jump_9 = pygame.transform.flip(player2_jump_9, True, False)


player2_jump_animation = [player2_jump_0, player2_jump_1, player2_jump_2, player2_jump_3, player2_jump_4, player2_jump_5, player2_jump_6, player2_jump_7, player2_jump_8, player2_jump_9]

###_________________________________________________________________________________
#WALK player 1
###_________________________________________________________________________________
player1_walk_0 = pygame.image.load('graphics/ninja_1/Run__000.png').convert_alpha()
player1_walk_0= pygame.transform.scale(player1_walk_0, (105,105))
player1_walk_1 = pygame.image.load('graphics/ninja_1/Run__001.png').convert_alpha()
player1_walk_1= pygame.transform.scale(player1_walk_1, (105,105))
player1_walk_2 = pygame.image.load('graphics/ninja_1/Run__002.png').convert_alpha()
player1_walk_2 = pygame.transform.scale(player1_walk_2, (105,105))
player1_walk_3 = pygame.image.load('graphics/ninja_1/Run__003.png').convert_alpha()
player1_walk_3 = pygame.transform.scale(player1_walk_3, (105,105))
player1_walk_4 = pygame.image.load('graphics/ninja_1/Run__004.png').convert_alpha()
player1_walk_4 = pygame.transform.scale(player1_walk_4, (105,105))
player1_walk_5 = pygame.image.load('graphics/ninja_1/Run__005.png').convert_alpha()
player1_walk_5 = pygame.transform.scale(player1_walk_5, (105,105))
player1_walk_6 = pygame.image.load('graphics/ninja_1/Run__006.png').convert_alpha()
player1_walk_6 = pygame.transform.scale(player1_walk_6, (105,105))
player1_walk_7 = pygame.image.load('graphics/ninja_1/Run__007.png').convert_alpha()
player1_walk_7 = pygame.transform.scale(player1_walk_7, (105,105))
player1_walk_8 = pygame.image.load('graphics/ninja_1/Run__008.png').convert_alpha()
player1_walk_8 = pygame.transform.scale(player1_walk_8, (105,105))
player1_walk_9 = pygame.image.load('graphics/ninja_1/Run__009.png').convert_alpha()
player1_walk_9 = pygame.transform.scale(player1_walk_9, (105,105))

player1_walk_animation = [player1_walk_0, player1_walk_1, player1_walk_2, player1_walk_3, player1_walk_4, player1_walk_5, player1_walk_6, player1_walk_7, player1_walk_8, player1_walk_9]

###_________________________________________________________________________________
#WALK player 2
###_________________________________________________________________________________
player2_walk_0 = pygame.image.load('graphics/ninja_2/Run__000.png').convert_alpha()
player2_walk_0= pygame.transform.scale(player2_walk_0, (105,105))
player2_walk_0 = pygame.transform.flip(player2_walk_0, True, False)
player2_walk_1 = pygame.image.load('graphics/ninja_2/Run__001.png').convert_alpha()
player2_walk_1= pygame.transform.scale(player2_walk_1, (105,105))
player2_walk_1 = pygame.transform.flip(player2_walk_1, True, False)
player2_walk_2 = pygame.image.load('graphics/ninja_2/Run__002.png').convert_alpha()
player2_walk_2 = pygame.transform.scale(player2_walk_2, (105,105))
player2_walk_2 = pygame.transform.flip(player2_walk_2, True, False)
player2_walk_3 = pygame.image.load('graphics/ninja_2/Run__003.png').convert_alpha()
player2_walk_3 = pygame.transform.scale(player2_walk_3, (105,105))
player2_walk_3 = pygame.transform.flip(player2_walk_3, True, False)
player2_walk_4 = pygame.image.load('graphics/ninja_2/Run__004.png').convert_alpha()
player2_walk_4 = pygame.transform.scale(player2_walk_4, (105,105))
player2_walk_4 = pygame.transform.flip(player2_walk_4, True, False)
player2_walk_5 = pygame.image.load('graphics/ninja_2/RUn__005.png').convert_alpha()
player2_walk_5 = pygame.transform.scale(player2_walk_5, (105,105))
player2_walk_5 = pygame.transform.flip(player2_walk_5, True, False)
player2_walk_6 = pygame.image.load('graphics/ninja_2/Run__006.png').convert_alpha()
player2_walk_6 = pygame.transform.scale(player2_walk_6, (105,105))
player2_walk_6 = pygame.transform.flip(player2_walk_6, True, False)
player2_walk_7 = pygame.image.load('graphics/ninja_2/Run__007.png').convert_alpha()
player2_walk_7 = pygame.transform.scale(player2_walk_7, (105,105))
player2_walk_7 = pygame.transform.flip(player2_walk_7, True, False)
player2_walk_8 = pygame.image.load('graphics/ninja_2/Run__008.png').convert_alpha()
player2_walk_8 = pygame.transform.scale(player2_walk_8, (105,105))
player2_walk_8 = pygame.transform.flip(player2_walk_8, True, False)
player2_walk_9 = pygame.image.load('graphics/ninja_2/Run__009.png').convert_alpha()
player2_walk_9 = pygame.transform.scale(player2_walk_9, (105,105))
player2_walk_9 = pygame.transform.flip(player2_walk_9, True, False)

player2_walk_animation = [player2_walk_0, player2_walk_1, player2_walk_2, player2_walk_3, player2_walk_4, player2_walk_5, player2_walk_6, player2_walk_7, player2_walk_8, player2_walk_9]







while True:
    if game_active:
        keys = pygame.key.get_pressed()
        if player_1_rect.bottom >= 300:
            if keys[pygame.K_e]:
                throw_attack_p1()

            elif keys[pygame.K_a]:
                player_1_rect.x -= 6
                walk_p1()
            elif keys[pygame.K_d]:
                player_1_rect.x += 6
                walk_p1()
            elif keys[pygame.K_q]:
                attack_p1()
    
            else:
                player_animation_p1()

        elif keys[pygame.K_e] and keys[pygame.K_w]:
             jump_throw_attack_p1()

        elif keys[pygame.K_d] and keys[pygame.K_w]:
            player_animation_p1()
            player_1_rect.x += 6


        elif keys[pygame.K_a] and keys[pygame.K_w]:
            player_animation_p1()
            player_1_rect.x -= 6


             
        elif keys[pygame.K_w]:
            player_animation_p1()

        

        if player_2_rect.bottom >= 300:
            if keys[pygame.K_RETURN]:
                 throw_attack_p2()
            elif keys[pygame.K_LEFT]:
                player_2_rect.x -= 6
                walk_p2()
            elif keys[pygame.K_RIGHT]:
                player_2_rect.x += 6
                walk_p2()
            elif keys[pygame.K_RSHIFT]:
                attack_p2()

            else:
                 player_animation_p2()

        elif keys[pygame.K_RETURN] and keys[pygame.K_UP]:
             jump_throw_attack_p2()
    

        elif keys[pygame.K_RIGHT] and keys[pygame.K_UP]:
            player_animation_p2()
            player_2_rect.x += 6

        elif keys[pygame.K_LEFT] and keys[pygame.K_UP]:
            player_animation_p2()
            player_2_rect.x -= 6

        elif keys[pygame.K_UP]:
             player_animation_p2()
    

    




    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and player_1_rect.bottom >= 300:
                    player_1_gravity = -17
                    player_1_rect.bottom = 300
                if event.key == pygame.K_UP and player_2_rect.bottom >= 300:
                    player_2_gravity = -17
                    player_2_rect.bottom = 300
        
        if game_active == True and player_1_health != 1500:
            player_1_health += 1
        if game_active == True and player_2_health != 1500:
             player_2_health += 1
     
        if player_2_mask.overlap(player_1_mask, (player_1_rect.x - player_2_rect.x, player_1_rect.y - player_2_rect.y)) and keys[pygame.K_q]:
                    player_2_health -= 25

        if player_1_mask.overlap(player_2_mask, (player_2_rect.x - player_1_rect.x, player_2_rect.y - player_1_rect.y)) and keys[pygame.K_RSHIFT]:
                    player_1_health -= 25

        elif kunai_player_1_mask.overlap(player_2_mask, (player_2_rect.x - kunai_rect.x, player_2_rect.y - kunai_rect.y)) and kunai_held_p1 == False:
                    player_2_health -= 50

        elif kunai_player_2_mask.overlap(player_1_mask, (player_1_rect.x - kunai_rect_2.x, player_1_rect.y - kunai_rect_2.y)) and kunai_held_p2 == False:
                    player_1_health -= 50

        if player_1_health <= 0:
            game_active = False
        if player_2_health <= 0:
            game_active = False

    
        screen.blit(test_surf, (0,0))
        screen.blit(ground_surf, (0,300))
        screen.blit(text_surf, (300, 50))
        player_1_health_bar = pygame.draw.rect(ground_surf, RED, (85,50,150,5))
        player_1_health_juice = pygame.draw.rect(ground_surf, GREEN, (85,50, player_1_health//10, 5))
        player_2_health_bar = pygame.draw.rect(ground_surf, RED, (550,50,150,5))
        player_2_health_juice = pygame.draw.rect(ground_surf, GREEN, (550,50, player_2_health//10, 5))
        player_1_gravity += 1
        player_1_rect.y += player_1_gravity
        if player_1_rect.bottom >= 300:
            player_1_rect.bottom = 300

        screen.blit(player_1_surf, player_1_rect)
        player_2_gravity += 1
        player_2_rect.y += player_2_gravity
        if player_2_rect.bottom >= 300:
            player_2_rect.bottom = 300

        screen.blit(player_2_surf, player_2_rect)
        if player_1_rect.x < 0 or player_1_rect.x > 728:
            if player_1_rect.x < 0:
                player_1_rect.x = 0
            else:
                player_1_rect.x = 728

        if player_2_rect.x < 0 or player_2_rect.x > 728:
            if player_2_rect.x < 0:
                player_2_rect.x = 0
            else:
                player_2_rect.x = 728

        if keys[pygame.K_e] and kunai_held_p1 == True:
             kunai_rect = kunai_player_1.get_rect(topleft = player_1_rect.topright)
             screen.blit(kunai_player_1, kunai_rect)
             kunai_held_p1 = False

        if kunai_held_p1 == False:
            screen.blit(kunai_player_1,kunai_rect)
            kunai_rect.x += 15
            if kunai_rect.x >= 1200:
                 kunai_held_p1 = True

        if keys[pygame.K_RETURN] and kunai_held_p2 == True:
             kunai_rect_2 = kunai_player_2.get_rect(topright = player_2_rect.topleft)
             screen.blit(kunai_player_2, kunai_rect_2)
             kunai_held_p2 = False

        if kunai_held_p2 == False:
            screen.blit(kunai_player_2,kunai_rect_2)
            kunai_rect_2.x -= 15
            if kunai_rect_2.x <= -400:
                 kunai_held_p2 = True

    
        
        
        
    

    if game_active == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        screen.blit(test_surf, (0,0))
        screen.blit(ground_surf, (0,300))
        screen.blit(text_surf, (300, 50))
        end_of_game()

    

    

      
    
    pygame.display.update()
    clock.tick(30)
