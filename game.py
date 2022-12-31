# this is paint
import pygame
import sys
WIDTH = 1200
HEIGHT = 800
BG_COLOR = (255, 255, 255)
COLOR = (0, 0, 0)
fps = 60
timer = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BG_COLOR)
pygame.display.set_caption('J-Paint')
pygame.display.update()
run = True
draw = False


def res_button(screen):
    button_font = pygame.font.Font(None, 50)
    reset_text = button_font.render('Reset', True, (0, 0, 0))
    reset_surf = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
    reset_rect = reset_surf.get_rect(center=(1100, 750))
    screen.blit(reset_surf, reset_rect)
    pygame.display.update()


while run:
    timer.tick(fps)
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('yes')
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
        pygame.draw.rect(screen, COLOR, pygame.Rect(x, y, 10, 10))
        pygame.display.update()