import pygame,time
import control,view,model



x=pygame.time.Clock()
while True:
    x.tick(120)
    control.control()
    model.go()
    view.draw()
