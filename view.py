import math

import pygame,random

screen=pygame.display.set_mode([800,600])
import model
def draw():
    #расчет угла
    if model.g<0:
        tga=model.g/model.v
        a=math.atan(tga)
        a=a*57.2958-90
    else:
        a=90
    m=pygame.transform.rotate(model.f,a)



    screen.fill([0,0,0])
    screen.blit(m,model.a.topleft)
    pygame.draw.rect(screen,[255,255,255],model.a,1)

    pygame.display.flip()
