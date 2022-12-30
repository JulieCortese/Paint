# this is paint
import pygame
import sys
WIDTH = 600
HEIGHT = 600
BG_COLOR = (255, 245, 218)
LINE_COLOR = (0, 0, 0)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((255, 255, 255))
pygame.display.set_caption('J-Paint')
pygame.display.update()
pygame.time.wait(600)