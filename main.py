###############################################################################
# File Name  : main.py
# Date       : 11/12/2022
# Description: Sprite Loading Practice
###############################################################################

import pygame
import spriteSheet

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
BG = (50, 50, 50)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('SpriteSheets')

sprite_sheet_image = pygame.image.load('doux.png').convert_alpha()
sprite_sheet = spriteSheet.SpriteSheet(sprite_sheet_image)


def get_image(sheet, frame,  width, height, scale, color):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet, (0, 0), ((frame * width), 0, width, height))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    image.set_colorkey(color)
    return image


frame_0 = sprite_sheet.get_image(0, 24, 24, 6, BLACK)
frame_1 = sprite_sheet.get_image(1, 24, 24, 6, BLACK)

run = True

if __name__ == '__main__':
    while run:
        screen.fill(BG)

        # show frame image
        screen.blit(frame_0, (0, 0))
        screen.blit(frame_1, (100, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

pygame.quit()
