import pygame
import control,view,model



while True:
    control.control()
    model.go()
    view.draw()