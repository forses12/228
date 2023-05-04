import pygame

image = pygame.image.load('vbfgnhfjmk.png')
image=pygame.transform.scale(image, [200 / 3.3, 200])
small_rect=pygame.Rect([10, 200], [image.get_width(), image.get_width()])
screen=pygame.display.get_surface()

speed_x=1
speed_y=-10
def go():
    global small_rect,speed_x,speed_y
    small_rect.x+=speed_x
    small_rect.y+=speed_y
    if small_rect.right>=screen.get_width() and speed_x>0:
        speed_x=-speed_x
    elif  small_rect.x<=0 and speed_x<0:
        speed_x=-speed_x
    if small_rect.bottom>=screen.get_height() and speed_y>0:
        speed_y=-speed_y
    elif  small_rect.y<=0 and speed_y<0:
        speed_y=-speed_y

