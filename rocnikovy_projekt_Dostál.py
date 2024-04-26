import pygame

pygame.init()

width=600
height=300
screen=pygame.display.set_mode((width, height))

lets_continue=True

while lets_continue:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            lets_continue=False


pygame.quit()
