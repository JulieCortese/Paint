# this is paint
import pygame
import sys
from constants import *
pygame.init()

fps = 60
timer = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BG_COLOR)
pygame.display.set_caption('J-Paint')
pygame.display.update()
run = True
draw = False
color = (0, 0, 0)
button_font = pygame.font.Font(None, 50)


def res_button(screen):
    reset_text = button_font.render('Reset', True, (0, 0, 0))
    reset_surf = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
    reset_surf.fill((235, 148, 9))
    reset_surf.blit(reset_text, (10, 10))
    reset_rect = reset_surf.get_rect(center=(1100, 750))
    screen.blit(reset_surf, reset_rect)

    erase_text = button_font.render('Erase', True, (0, 0, 0))
    erase_surf = pygame.Surface((erase_text.get_size()[0] + 20, erase_text.get_size()[1] + 20))
    erase_surf.fill((235, 148, 9))
    erase_surf.blit(erase_text, (10, 10))
    erase_rect = erase_surf.get_rect(center=(900, 750))
    screen.blit(erase_surf, erase_rect)

    pygame.display.update()
    return reset_rect, erase_rect


def color_options(screen):
    pygame.draw.circle(screen, (0, 0, 0), center=(80, 750), radius=30.0)
    pygame.draw.circle(screen, 'red', center=(80, 750), radius=20.0)




while run:
    timer.tick(fps)
    mouse_pos = pygame.mouse.get_pos()
    reset_button, erase_button = res_button(screen)
    colors = color_options(screen)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if reset_button.collidepoint(event.pos):  # clears screen of drawings
                screen.fill((255, 255, 255))
                reset_button, color_change_button = res_button(screen)
                pygame.display.flip()
                continue  # makes it so you can't click and drag from the reset button
            elif erase_button.collidepoint(event.pos):
                color = (255, 255, 255)
                # make way of changing color (in a different screen maybe)
                draw = True
                continue
            elif colors[0].collidepoint(event.pos):
                print('clicked')
                continue
            draw = True
        elif event.type == pygame.MOUSEBUTTONUP:
            draw = False
        elif event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()
    if draw:
        mouse_pos = pygame.mouse.get_pos()
        x, y = mouse_pos
        pygame.draw.rect(screen, color, pygame.Rect(x, y, 10, 10))
        pygame.display.flip()
