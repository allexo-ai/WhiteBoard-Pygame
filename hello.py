import pygame
from pygame.constants import MOUSEBUTTONDOWN

# Porneste programul
pygame.init()

# Creeaza fereastra programului
screen = pygame.display.set_mode((1920, 1017))

# Nume si iconita
pygame.display.set_caption("Tabla Alba")
icon = pygame.image.load("whiteboard.png")
pygame.display.set_icon(icon)

# Creeaza creionul, radiera si X-ul
pencilImg = pygame.image.load('pencil.png')
pencilX = 800
pencilY = 910

eraserImg = pygame.image.load('eraser.png')
eraserX = 900
eraserY = 910

crossImg = pygame.image.load('cross.png')
crossX = 1000
crossY = 910

def pencil():
    screen.blit(pencilImg, (pencilX, pencilY))

def eraser():
    screen.blit(eraserImg, (eraserX, eraserY))

def cross():
    screen.blit(crossImg, (crossX, crossY))

z = 0

# Verifica daca programul este oprit de utilizator
running = True
while running:
    # Seteaza culoarea de fundal (alb)
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


# Afiseaza creionul, radiera si X-ul
    pencil()
    eraser()
    cross()

# Afiseaza ecranul
    pygame.display.update()