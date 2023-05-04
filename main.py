import pygame,time
import control,view,model



x=pygame.time.Clock()
while True:
    x.tick(75)
    control.control()
    model.go()
    view.draw()
