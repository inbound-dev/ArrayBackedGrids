import pygame
import random


BACKGROUND_COLOR = 255,255,255

WIDTH = 20
HEIGHT = 20

MARGIN = 3

SCREEN_WIDTH = 762
SCREEN_HEIGHT = 601

GREY = (150, 150, 150)
WHITE = (255,255,255)
RED = (255, 0, 0)
BLUE = (55, 55, 255)
BLACK = (0, 0, 0)
GREEN = (0,255,0)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake")
screen.fill((BACKGROUND_COLOR))

grid = []
for row in range(10):
    grid.append([])
    for column in range(10):
        grid[row].append(0)

grid[1][5] = 1


running = True
while running:

    pos = pygame.mouse.get_pos()
    column = pos[0] // (WIDTH + MARGIN)
    row = pos[1] // (HEIGHT + MARGIN)

    print("Grid coordinates: ", row, column)


    for row in range(26):
        for column in range(34):
            color = BLACK
            pygame.draw.rect(screen,color,[(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])


    pygame.display.flip()
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    running = False
