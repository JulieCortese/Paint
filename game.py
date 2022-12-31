# this is paint
import pygame
import sys
WIDTH = 1200
HEIGHT = 800
BG_COLOR = (255, 255, 255)
COLOR = (0, 0, 0)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BG_COLOR)
pygame.display.set_caption('J-Paint')
pygame.display.update()
restart = False
while not restart:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('yes')
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()
