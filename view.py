import pygame,random

screen=pygame.display.set_mode([800,600])
import model
def draw():
    screen.fill([0,0,0])
    screen.blit(model.f,model.a.topleft)
    pygame.display.flip()
