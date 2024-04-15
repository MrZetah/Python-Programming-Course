# 1 - import packages
import pygame
from pygame.locals import *
import sys
import random

#2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FPS = 30
LOGO_WIDTH_HEIGHT = 100
VELOCITY = 3

#3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

#4 - Load assets: images, sounds, etc.
logo = pygame.image.load('image/logo.jpg')
logo = pygame.transform.scale(logo, (LOGO_WIDTH_HEIGHT, LOGO_WIDTH_HEIGHT))

#5 - Initialize variables
MAX_WIDTH = WINDOW_WIDTH - LOGO_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - LOGO_WIDTH_HEIGHT
logoX = random.randrange(MAX_WIDTH)
logoY = random.randrange(MAX_HEIGHT)
xSpeed = VELOCITY
ySpeed = VELOCITY

#6 - Loop forever
while True:

    #7 Check for and handle events
    for event in pygame.event.get():
        #Check to see if user has quit the game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #Press the 'q' key as an option to quit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
        #Check for other 'game' related events (collisions, key presses, mouse clicks, etc.)


    #8 - Do any "per frame" actions (move objects, add or remove items)
    if (logoX < 0) or (logoX >= MAX_WIDTH):
        xSpeed = -xSpeed
    if (logoY < 0) or (logoY >= MAX_HEIGHT):
        ySpeed = -ySpeed

    logoX = logoX + xSpeed
    logoY = logoY + ySpeed

    #9 - Clear the window
    window.fill(BLACK)

    #10 - Draw all window elements
    window.blit(logo, (logoX, logoY))

    #11 - Update the window
    pygame.display.update()

    #12 - Set frame rate to slow things down
    clock.tick(FPS)











