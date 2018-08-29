import sys
import math
import random
import numpy as np
import pygame
from pygame.locals import *

pygame.init()
surf = pygame.display.set_mode((800, 600))
surf.fill((10, 10, 10))

points = [] # associer a chaque point une couleur, puis calculer pour chaque pixel la distance euclidienne au points (math.sqrt(((a1-b1)**2) + (a2-b2)**2))
pix = pygame.PixelArray(surf)

pygame.display.set_caption('Voronoi Diagram')

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            posx, posy = pygame.mouse.get_pos()
            points.append([np.array([posx, posy]), (random.randint(1, 254), random.randint(1, 254), random.randint(1, 254))])
            pygame.draw.circle(surf, (255, 255, 255), (posx, posy), 3, 3)

            if points.__len__() == 1:
                for x, y in [(x, y) for x in range(surf.get_size()[0]) for y in range(surf.get_size()[1])]:
                    if pix[x, y] == surf.map_rgb((255, 255, 255)):
                        pix[x, y] = (255, 255, 255)
                    else:
                        pix[x, y] = points[0][1]
            else:
                for x, y in [(x, y) for x in range(surf.get_size()[0]) for y in range(surf.get_size()[1])]:
                    if pix[x, y] == surf.map_rgb((255, 255, 255)):
                        pass
                    else:
                        pix[x, y] = 0

        if event.type == QUIT:
            del pix
            pygame.quit()
            sys.exit()
    pygame.display.update()
