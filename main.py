import pygame,time
import view,model,control



x=pygame.time.Clock()
while True:
    x.tick(75)
    control.control()
    model.go()
    view.draw()
