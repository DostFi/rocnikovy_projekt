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

# Načtení obrázků
pozadí = pygame.image.load('img/bg.png')
pozemek_obr = pygame.image.load('img/ground.png')


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

    def update(self):

        # Animace
        self.počítadlo += 1
        prodleva_machání = 5

        if self.počítadlo > prodleva_machání:
            self.počítadlo = 0
            self.index += 1
            if self.index >= len(self.obrázky):
                self.index = 0
        self.image = self.obrázky[self.index]  # Update current image


pták_skupina = pygame.sprite.Group()

flappy = Pták(100, int(výška_obrazovky / 2))

pták_skupina.add(flappy)

běh = True
while běh:

    clock.tick(fps)

    # Kreslení pozadí
    obrazovka.blit(pozadí, (0,0))

    pták_skupina.draw(obrazovka)
    pták_skupina.update()

    # Kreslení a posun pozadí
    obrazovka.blit(pozemek_obr, (posun_pozadí,768))
    posun_pozadí -= rychlost_posunu
    if abs(posun_pozadí) > 35:
        posun_pozadí = 0

    for událost in pygame.event.get():
        if událost.type == pygame.QUIT:
            běh = False
    pygame.display.update()

pygame.quit()
