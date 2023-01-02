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
    erase_rect = erase_surf.get_rect(center=(960, 750))
    screen.blit(erase_surf, erase_rect)

    pygame.display.update()
    return reset_rect, erase_rect


def color_options(screen):
    red_img = pygame.image.load('red_square.png')
    red_rect = red_img.get_rect(center=(40, 750))
    screen.blit(red_img, red_rect)
    orange_img = pygame.image.load('orange_square.png')
    orange_rect = orange_img.get_rect(center=(100, 750))
    screen.blit(orange_img, orange_rect)
    yellow_img = pygame.image.load('yellow_square.png')
    yellow_rect = yellow_img.get_rect(center=(160, 750))
    screen.blit(yellow_img, yellow_rect)
    green_img = pygame.image.load('green_square.png')
    green_rect = green_img.get_rect(center=(220, 750))
    screen.blit(green_img, green_rect)
    blue_img = pygame.image.load('blue_square.png')
    blue_rect = blue_img.get_rect(center=(280, 750))
    screen.blit(blue_img, blue_rect)
    purple_img = pygame.image.load('purple_square.png')
    purple_rect = purple_img.get_rect(center=(340, 750))
    screen.blit(purple_img, purple_rect)
    black_img = pygame.image.load('black_square.png')
    black_rect = black_img.get_rect(center=(460, 750))
    screen.blit(black_img, black_rect)
    pink_img = pygame.image.load('pink_square.png')
    pink_rect = pink_img.get_rect(center=(400, 750))
    screen.blit(pink_img, pink_rect)
    return red_rect, orange_rect, yellow_rect, green_rect, blue_rect, purple_rect, black_rect, pink_rect


while run:
    timer.tick(fps)
    mouse_pos = pygame.mouse.get_pos()
    reset_button, erase_button = res_button(screen)
    colors = color_options(screen)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if reset_button.collidepoint(event.pos):  # clears screen of drawings
                screen.fill('white')
                color = 'black'
                reset_button, color_change_button = res_button(screen)
                pygame.display.flip()
                continue  # makes it so you can't click and drag from the reset button
            elif erase_button.collidepoint(event.pos):
                color = 'white'
                # make way of changing color (in a different screen maybe)
                draw = True
                continue
            elif colors[0].collidepoint(event.pos):
                color = 'red'
                continue
            elif colors[1].collidepoint(event.pos):
                color = (255, 146, 14)
                continue
            elif colors[2].collidepoint(event.pos):
                color = 'yellow'
                continue
            elif colors[3].collidepoint(event.pos):
                color = 'green'
                continue
            elif colors[4].collidepoint(event.pos):
                color = 'blue'
                continue
            elif colors[5].collidepoint(event.pos):
                # color is purple
                color = (163, 73, 164)
                continue
            elif colors[6].collidepoint(event.pos):
                color = 'black'
                continue
            elif colors[7].collidepoint(event.pos):
                # color is pink
                color = (255, 174, 201)
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
