import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('DVD BOUNCER')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

Red_square = pygame.surface.Surface((100, 100))

Red_square.fill('Red')
x_vel = 3
y_vel = 4

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(Red_square, (0,0))
      
    
    pygame.display.update()
    clock.tick(60)