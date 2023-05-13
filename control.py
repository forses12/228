import pygame

import model


def control():
    event=pygame.event.get()
    for z in event:
        if z.type==pygame.QUIT:
            exit()
        if z.type==pygame.KEYDOWN and z.key==pygame.K_UP:
            model.defender(0)
        elif z.type==pygame.KEYDOWN and z.key==pygame.K_DOWN:
            model.defender(1)
        elif z.type == pygame.KEYDOWN and z.key == pygame.K_LEFT:
            model.defender(2)
        elif z.type==pygame.KEYDOWN and z.key==pygame.K_RIGHT:
            model.defender(3)
