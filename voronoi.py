import sys
import math
import random
import pygame
from pygame.locals import *

pygame.init()
surf = pygame.display.set_mode((800, 600))
surf.fill((255, 255, 255))

pointsList = [] # associer a chaque point une couleur, puis calculer pour chaque pixel la distance euclidienne au points (math.sqrt(((a1-b1)**2) + (a2-b2)**2))
graphicPointsList = []
pix = pygame.PixelArray(surf)

pygame.display.set_caption('Voronoi Diagram')

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = pygame.mouse.get_pos()
            graphicPointsList.append([surf, (255, 0, 255), (x, y), 5, 1])
            pointsList.append([x, y, (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))])
            if pointsList.__len__() == 1:
                pix[...] = pointsList[0][2]
            else:
                pix = pygame.PixelArray(surf)
                for x, y in [(x, y) for x in [i for i in range(surf.get_size()[0])] for y in [i for i in range(surf.get_size()[1])]]:
                    pix[x][y] = (200, 0, 0)
                del pix
            for elt in graphicPointsList:
                pygame.draw.circle(elt[0], elt[1], elt[2], elt[3], elt[4])

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()