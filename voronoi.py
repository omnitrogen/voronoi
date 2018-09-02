import sys
import random
import math
import pygame
from pygame.locals import QUIT

pygame.init()
size = (400, 400)
surf = pygame.display.set_mode((size[0], size[1]))
surf.fill((100, 100, 100))
points = []
pygame.display.set_caption('Voronoi Diagram')

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            posx, posy = pygame.mouse.get_pos()
            points.append([[posx, posy], (random.randint(1, 254), random.randint(1, 254), random.randint(1, 254))])
            pygame.draw.circle(surf, (255, 255, 255), (posx, posy), 5, 1)
            for x, y in [(x, y) for x in range(size[0]) for y in range(size[1])]:
                if surf.get_at((x, y))[:-1] != (255, 255, 255):
                    surf.set_at((x, y), min([(math.sqrt((x - i[0][0])**2 + (y - i[0][1])**2), i[1]) for i in points])[1])

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()