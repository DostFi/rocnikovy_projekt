import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps = 60

šířka_obrazovky = 864
výška_obrazovky = 936

obrazovka = pygame.display.set_mode((šířka_obrazovky, výška_obrazovky))
pygame.display.set_caption('Flappy Bird')

# Definování herních proměnných
posun_pozadí = 0
rychlost_posunu = 4
létání = False
prohra = False

# Načtení obrázků
pozadí = pygame.image.load('img/bg.png')
pozadí_obrázek = pygame.image.load('img/ground.png')


class Pták(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.obrázky = []
        self.index = 0
        self.počítadlo = 0
        for číslo in range(1, 4):
            obr = pygame.image.load(f'img/bird{číslo}.png')
            self.obrázky.append(obr)
        self.image = self.obrázky[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.vel = 0
        self.clicked = False

    def update(self):
     if létání == True:   
        #gravitace
        self.vel += 0.5
        if self.vel > 8:
            self.vel = 8
        if self.rect.bottom < 768:
            self.rect.y += int(self.vel)
        if prohra == False:
            #jump
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.vel = -10
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

            # Animace
            self.počítadlo += 1
            prodleva_machání = 5

            if self.počítadlo > prodleva_machání:
                self.počítadlo = 0
                self.index += 1
                if self.index >= len(self.obrázky):
                    self.index = 0
            self.image = self.obrázky[self.index]  # Update current image

            #rotace ptáka
            self.image = pygame.transform.rotate(self.obrázky[self.index], self.vel * -2)
        else:
            self.image = pygame.transform.rotate(self.obrázky[self.index], -90)






pták_skupina = pygame.sprite.Group()

flappy = Pták(100, int(výška_obrazovky / 2))

pták_skupina.add(flappy)

pokračování = True
while pokračování:

    clock.tick(fps)

    # Kreslení pozadí
    obrazovka.blit(pozadí, (0,0))

    pták_skupina.draw(obrazovka)
    pták_skupina.update()
    #nakreslení země
    obrazovka.blit(pozadí_obrázek, (posun_pozadí,768))

    # kontrola jestli pták spadnul na zem
    if flappy.rect.bottom > 768:
        prohra = True
        létání = False

    if prohra == False:
        # Kreslení a posun pozadí
        posun_pozadí -= rychlost_posunu
        if abs(posun_pozadí) > 35:
            posun_pozadí = 0

    for událost in pygame.event.get():
        if událost.type == pygame.QUIT:
            pokračování = False
        if událost.type == pygame.MOUSEBUTTONDOWN and létání == False and prohra == False:
            létání = True
    pygame.display.update()

pygame.quit()
