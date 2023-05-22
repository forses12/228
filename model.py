import pygame

image = pygame.image.load('vbfgnhfjmk.png')
image = pygame.transform.scale(image, [202 / 3.3,202])
small_rect = pygame.Rect([10, 200], [image.get_width(), image.get_width()])
screen = pygame.display.get_surface()
ice_rect = pygame.Rect([0, 200], [50, 50])

speed_x = 5
speed_y = -5
heart=3

def take_screen():
    if screen.get_width()==800:
        pygame.display.set_mode([0,0],flags=pygame.FULLSCREEN)
    else:
        pygame.display.set_mode([800, 600])
def go():
    global small_rect, speed_x, speed_y,heart
    small_rect.x += speed_x
    small_rect.y += speed_y

    if small_rect.right >= screen.get_width() and speed_x > 0:
        speed_x = -speed_x
        heart-=1
    elif small_rect.x <= 0 and speed_x < 0:
        speed_x = -speed_x
        heart-=1
    if small_rect.bottom >= screen.get_height() and speed_y > 0:
        speed_y = -speed_y
        heart-=1
    elif small_rect.y <= 0 and speed_y < 0:
        speed_y = -speed_y
        heart-=1


    if heart<1:
        exit()

    if small_rect.right >= screen.get_width()-60 and speed_x > 0 and ice_rect.left==screen.get_width()-60:
        speed_x = -speed_x
    elif small_rect.x <= 60 and speed_x < 0 and ice_rect.right==60:
        speed_x = -speed_x
    if small_rect.bottom >= screen.get_height()-60 and speed_y > 0 and ice_rect.top==screen.get_height()-60:
        speed_y = -speed_y
    elif small_rect.y <= 60 and speed_y < 0 and ice_rect.bottom==60:
        speed_y = -speed_y


def defender(f):
    if f == 0:
        ice_rect.w = screen.get_width()
        ice_rect.h = 60
        ice_rect.y = 0
        ice_rect.x = 0
    elif f == 1:
        ice_rect.w = screen.get_width()
        ice_rect.h = 60
        ice_rect.y = screen.get_height() - 60
        ice_rect.x=0
    elif f == 2:
        ice_rect.w = 60
        ice_rect.h = screen.get_height()
        ice_rect.y = 0
        ice_rect.x=0
    elif f == 3:
        ice_rect.w = 60
        ice_rect.h = screen.get_height()
        ice_rect.y = 0
        ice_rect.x = screen.get_width()-60
