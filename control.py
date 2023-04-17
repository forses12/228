import pygame

def control():
    event=pygame.event.get()
    for z in event:
        if z.type==pygame.QUIT:
            exit()