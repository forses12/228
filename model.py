import pygame

a=pygame.Rect([10,10],[50,50])
screen=pygame.display.get_surface()

def go():
    global a,v
    v=2
    a.x+=v
    if a.right>=screen.get_width() and v>0:
        v=-v
    elif  a.x<=0 and v<0:
        v=-v

