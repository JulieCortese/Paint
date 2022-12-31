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

    change_text = button_font.render('change color', True, (0, 0, 0))
    change_surf = pygame.Surface((change_text.get_size()[0] + 20, change_text.get_size()[1] + 20))
    change_surf.fill((235, 148, 9))
    change_surf.blit(change_text, (10, 10))
    change_rect = change_surf.get_rect(center=(900, 750))
    screen.blit(change_surf, change_rect)

    pygame.display.update()
    return reset_rect, change_rect


def color_change(screen):
    screen.fill(BG_COLOR)
    big_font = pygame.font.Font(None, 70)
    title_surface = big_font.render('Color Pick', 0, (0, 0, 0))
    title_rectangle = title_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 300))
    screen.blit(title_surface, title_rectangle)

    done_text = button_font.render('Paint', True, (0, 0, 0))
    done_surf = pygame.Surface((done_text.get_size()[0] + 20, done_text.get_size()[1] + 20))
    done_surf.fill((235, 148, 9))
    done_surf.blit(done_text, (10, 10))
    done_rect = done_surf.get_rect(center=(1100, 750))
    screen.blit(done_surf, done_rect)
    pygame.display.update()

    done = False
    while True and not done:
        timer.tick(fps)
        pygame.draw.rect(screen, color, [WIDTH // 2 - 200, HEIGHT // 2 - 200, 400, 400])
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if done_rect.collidepoint(event.pos):
                    screen.fill(BG_COLOR)
                    reset_button, color_change_button = res_button(screen)
                    done = True
                    break
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()


while run:
    timer.tick(fps)
    mouse_pos = pygame.mouse.get_pos()
    reset_button, color_change_button = res_button(screen)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if reset_button.collidepoint(event.pos):  # clears screen of drawings
                screen.fill((255, 255, 255))
                reset_button, color_change_button = res_button(screen)
                pygame.display.flip()
                continue  # makes it so you can't click and drag from the reset button
            if color_change_button.collidepoint(event.pos):
                # make way of changing color (in a different screen maybe)
                color_change(screen)
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
