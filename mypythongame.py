import pygame
from sys import exit


def player_animation():
    global player_surf, player_index

    if player_rect.bottom < 300:
        player_surf = player_jump

    else:
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0
        player_surf = player_walk[int(player_index)]


pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

test_surf = pygame.image.load('graphics/Sky.png').convert()
ground_surf = pygame.image.load('graphics/ground.png').convert()
text_surf = test_font.render('MY GAME', False, 'Blue')
snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom = (800,300))



player_jump = pygame.image.load('graphics/player/jump.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))
health_bar_outline = pygame.image.load('graphics/enemy_health_bar/enemy_health_bar_foreground_001.png')
health_bar_outline_rect = health_bar_outline.get_rect(midbottom = (40,100))
health_bar = pygame.image.load('graphics/enemy_health_bar/enemy_health_bar_000.png')
health_bar_rect = health_bar.get_rect(midbottom = (40, 100))

health_bar_outline_2 = pygame.image.load('graphics/enemy_health_bar/enemy_health_bar_foreground_001.png')
health_bar_outline_2_rect = health_bar_outline_2.get_rect(midbottom = (760,100))
health_bar_2 = pygame.image.load('graphics/enemy_health_bar/enemy_health_bar_000.png')
health_bar_2_rect = health_bar_2.get_rect(midbottom = (760, 100))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(test_surf, (0,0))
    screen.blit(ground_surf, (0,300))
    screen.blit(text_surf, (300, 50))
    snail_rect.x -= 4
    if snail_rect.right <= 0: snail_rect.left = 800
    screen.blit(snail_surf, snail_rect)
    player_animation()
    screen.blit(player_surf, player_rect)

      
    
    pygame.display.update()
    clock.tick(60)