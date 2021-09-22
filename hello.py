import pygame
from pygame.constants import MOUSEBUTTONDOWN

# Starts the program
pygame.init()

# Creates program window
screen = pygame.display.set_mode((1920, 1017))

# Name and Icon
pygame.display.set_caption("Whiteboard")
icon = pygame.image.load("whiteboard.png")
pygame.display.set_icon(icon)

# Creates the pencil, eraser and X icons
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

# Program Loop
running = True
while running:
    # Sets the background color (white)
    screen.fill((255, 255, 255))

    # Checks if the program is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Shows the pencil, eraser and X icons
    pencil()
    eraser()
    cross()

    # Updates the screen
    pygame.display.update()