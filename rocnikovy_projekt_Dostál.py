import pygame
from pygame.locals import *
import random

pygame.init()

clock = pygame.time.Clock()
fps = 60

šířka_obrazovky = 864
výška_obrazovky = 936

obrazovka = pygame.display.set_mode((šířka_obrazovky, výška_obrazovky))
pygame.display.set_caption('Flappy Bird')

# definice fontu
font = pygame.font.SysFont('Bauhaus 93', 60)

# definice barev
bílá = (255, 255, 255)

# Definování herních proměnných
posun_pozadí = 0
rychlost_posunu = 4
létání = False
prohra = False
trubka_mezera = 150
trubka_frekvence = 1500 #milisekundy
poslední_trubka = pygame.time.get_ticks() - trubka_frekvence
score = 0
trubka_překonání = False

# Načtení obrázků
pozadí = pygame.image.load('img/bg.png')
pozadí_obrázek = pygame.image.load('img/ground.png')
tlačítko_obrázek = pygame.image.load('img/restart.png')

def vykreslení_textu (text, font, text_barva, x, y):
    obrázek = font.render(text, True, text_barva)
    obrazovka.blit(obrázek, (x, y))

def reset_hry():
    trubka_skupina.empty()
    flappy.rect.x = 100
    flappy.rect.y = int(výška_obrazovky / 2)
    score = 0
    return score


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
        self.zmáčknuto = False

    def update(self):
        if létání == True:   
            # gravitace
            self.vel += 0.5
            if self.vel > 8:
                self.vel = 8
            if self.rect.bottom < 768:
                self.rect.y += int(self.vel)
            if prohra == False:
                # jump
                if pygame.mouse.get_pressed()[0] == 1 and self.zmáčknuto == False:
                    self.zmáčknuto = True
                    self.vel = -10
                if pygame.mouse.get_pressed()[0] == 0:
                    self.zmáčknuto = False

                # Animace
                self.počítadlo += 1
                prodleva_machání = 5

                if self.počítadlo > prodleva_machání:
                    self.počítadlo = 0
                    self.index += 1
                    if self.index >= len(self.obrázky):
                        self.index = 0
                self.image = self.obrázky[self.index]

                # rotace ptáka
                self.image = pygame.transform.rotate(self.obrázky[self.index], self.vel * -2)
            else:
                self.image = pygame.transform.rotate(self.obrázky[self.index], -90)




class Trubka(pygame.sprite.Sprite):
    def __init__(self, x, y, pozice):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/pipe.png')
        self.rect = self.image.get_rect()
        # pozice 1 je z vrchu, -1 ze spodu
        if pozice == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - int(trubka_mezera / 2)]
        if pozice == -1:
            self.rect.topleft = [x, y + int(trubka_mezera / 2)]
    def update(self):
        self.rect.x -= rychlost_posunu
        if self.rect.right < 0:
            self.kill()


class Tlačítko():
    def __init__(self, x, y, obrázek):
        self.obrázek = obrázek
        self.rect = self.obrázek.get_rect()
        self.rect.topleft = (x, y)


    def vykreslení(self):

        akce = False

        #získání pozice myši
        pozice_myši = pygame.mouse.get_pos()

        #kontrola jestli myš je nad tlačítkem
        if self.rect.collidepoint(pozice_myši):
            if pygame.mouse.get_pressed()[0] == 1:
                akce = True

        #vykreslení tlačítka
        obrazovka.blit(self.obrázek, (self.rect.x, self.rect.y))

        return akce

pták_skupina = pygame.sprite.Group()
trubka_skupina = pygame.sprite.Group()

flappy = Pták(100, int(výška_obrazovky / 2))

pták_skupina.add(flappy)


#vytvoření instance restartovacího tlačítka
tlačítko = Tlačítko(šířka_obrazovky // 2 - 50, výška_obrazovky // 2 - 100, tlačítko_obrázek)


pokračování = True
while pokračování:

    clock.tick(fps)

    # Kreslení pozadí
    obrazovka.blit(pozadí, (0,0))

    pták_skupina.draw(obrazovka)
    pták_skupina.update()
    trubka_skupina.draw(obrazovka)

    #nakreslení země
    obrazovka.blit(pozadí_obrázek, (posun_pozadí,768))

    # kontrola score
    if len(trubka_skupina) > 0:
        if pták_skupina.sprites()[0].rect.left > trubka_skupina.sprites()[0].rect.left and pták_skupina.sprites()[0].rect.right < trubka_skupina.sprites()[0].rect.right and trubka_překonání == False:
            trubka_překonání = True
        if trubka_překonání == True:
            if pták_skupina.sprites()[0].rect.left > trubka_skupina.sprites()[0].rect.right:
                score += 1
                trubka_překonání = False

    vykreslení_textu(str(score), font, bílá, int(šířka_obrazovky / 2), 20)
    #kolize
    if pygame.sprite.groupcollide(pták_skupina, trubka_skupina, False, False) or flappy.rect.top < 0:
        prohra = True
    # kontrola jestli pták spadnul na zem
    if flappy.rect.bottom >= 768:
        prohra = True
        létání = False

    if prohra == False and létání == True:

        # generace nových trubek
        čas_teď = pygame.time.get_ticks()
        if čas_teď - poslední_trubka > trubka_frekvence:
            trubka_výška = random.randint(-100, 100)
            spodní_trubky = Trubka(šířka_obrazovky, int(výška_obrazovky / 2) + trubka_výška, -1)
            vrchní_trubky = Trubka(šířka_obrazovky, int(výška_obrazovky / 2) + trubka_výška, 1)
            trubka_skupina.add(spodní_trubky)
            trubka_skupina.add(vrchní_trubky)
            poslední_trubka = čas_teď
        # Kreslení a posun pozadí
        posun_pozadí -= rychlost_posunu
        if abs(posun_pozadí) > 35:
            posun_pozadí = 0
        trubka_skupina.update()

    # kontrola konce hry a restartu
    if prohra == True:
        if tlačítko.vykreslení() == True:
            prohra = False
            score = reset_hry()




    for událost in pygame.event.get():
        if událost.type == pygame.QUIT:
            pokračování = False
        if událost.type == pygame.MOUSEBUTTONDOWN and létání == False and prohra == False:
            létání = True
    pygame.display.update()

pygame.quit()
