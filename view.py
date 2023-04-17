import pygame

screen=pygame.display.set_mode([800,600])
import model
def draw():
    screen.fill([0,0,0])
    pygame.draw.rect(screen,[125,53,77,],model.a)
    pygame.display.flip()
