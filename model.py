import pygame

f = pygame.image.load('Без имени.png')
f=pygame.transform.scale(f,[200,200/3.3])
a=pygame.Rect([10,10],[f.get_height(),f.get_height()])
screen=pygame.display.get_surface()

v=2
g=2
def go():
    global a,v,g
    a.x+=v
    a.y+=g
    if a.right>=screen.get_width() and v>0:
        v=-v
    elif  a.x<=0 and v<0:
        v=-v
    if a.bottom>=screen.get_height() and g>0:
        g=-g
    elif  a.y<=0 and g<0:
        g=-g

