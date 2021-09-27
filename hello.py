import pygame
from pygame.constants import MOUSEBUTTONDOWN, MOUSEBUTTONUP

# Starts the program
pygame.init()

# Creates program window
screen = pygame.display.set_mode((1920, 1017))

# Name and Icon
pygame.display.set_caption("Whiteboard")
icon = pygame.image.load("whiteboard.png")
pygame.display.set_icon(icon)

# Sets the background color (white)
screen.fill((255, 255, 255))

brush1 = pygame.image.load('brush1.png')
brush1 = pygame.transform.scale(brush1,(4,4))

brush2 = pygame.image.load('brush2.png')
brush2 = pygame.transform.scale(brush2,(64,64))

# Updates the screen
pygame.display.update()

# Creates images for the pencil, eraser and cross buttons 
pencilImg = pygame.image.load('pencil.png')
eraserImg = pygame.image.load('eraser.png')
crossImg = pygame.image.load('cross.png')

# Defines buttons
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
    
    def draw(self):
        action = False
        # Gets the mouse position
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action
        
# Creates buttons
pencil = Button(800, 910, pencilImg)
eraser = Button(900, 910, eraserImg)
cross = Button(1000, 910, crossImg)

penclick = 0
pendraw = 0

eraseclick = 0
erasedraw = 0

# Program Loop
running = True
while running:

    # Shows the pencil, eraser and X icons
    if pencil.draw():
        eraseclick = 0
        penclick = 1
    if eraser.draw():
        penclick = 0
        eraseclick = 1
    if cross.draw():
        penclick = 0
        eraseclick = 0
        screen.fill((255, 255, 255))

    # Gets the mouse position
    x,y = pygame.mouse.get_pos()

    # Checks if the program is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if penclick == 1:
            if event.type == MOUSEBUTTONDOWN:
                pendraw = 1
            elif event.type == MOUSEBUTTONUP:
                pendraw = 0
            if pendraw == 1:
                screen.blit(brush1,(x-2,y-2))
        if eraseclick == 1:
            if event.type == MOUSEBUTTONDOWN:
                erasedraw = 1
            elif event.type == MOUSEBUTTONUP:
                erasedraw = 0
            if erasedraw == 1:
                screen.blit(brush2,(x-32,y-32))

    # Updates the screen
    pygame.display.update()
