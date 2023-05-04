import math_utils

import pygame,random

screen=pygame.display.set_mode([800,600])
import model
def draw():

    a=math_utils.get_angle_by_point(model.small_rect.center, [model.small_rect.centerx + model.speed_x, model.small_rect.centery + model.speed_y])
    povorot=pygame.transform.rotate(model.image, a)
    big_rect=pygame.Rect([10,10],povorot.get_size())
    big_rect.x=model.small_rect.x
    big_rect.y=model.small_rect.y

    def fireball():
        if  model.speed_x<0:
            big_rect.left=model.small_rect.left
        else:
            big_rect.right=model.small_rect.right
        if model.speed_y>0:
            big_rect.bottom=model.small_rect.bottom
        else:
            big_rect.top=model.small_rect.top

    fireball()


    screen.fill([0,0,0])
    screen.blit(povorot, big_rect)
    # pygame.draw.rect(screen, [255,255,255], model.small_rect, 1)
    # pygame.draw.rect(screen,[255,255,255],big_rect,1)

    pygame.display.flip()
