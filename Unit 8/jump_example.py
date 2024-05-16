# Pygame Example of a jumping object

# 1 - import packages
import pygame
from pygame.locals import *
import sys

#2 - Define constants
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
PLAYER_SIZE = 40
FPS = 30
JUMP_HEIGHT = 60        # Increasing this value increases jump height, but increasing the up gravity will decrease jump height
UP_GRAVITY = 5          # These variables changes the vel_y variable
DOWN_GRAVITY = 2        # Tweak these two values until you get a realistic feel
vel_y = 0               # Initially set this variable to 0. Pressing the up key will change it later
PLAYER_VELOCITY = 6     # This is the velocity to move side to side
moving_left = False
moving_right = False    # Intially set block to not move unless left or right key are pressed

#3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

#4 - Load assets: images, sounds, etc.

#5 - Initialize variables

player = pygame.Rect(WINDOW_WIDTH//2, WINDOW_HEIGHT - PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE)

#5.5 - Functions


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
        # If the up key is pressed and the player is on the bottom of the screen, change the y velocity to intiate jump
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and player.y == WINDOW_HEIGHT - PLAYER_SIZE:  # Check to see if player is on ground before jumping
                vel_y = -JUMP_HEIGHT                                                           # a negative value moves the player up.
        #Check left and right keys to move player side to side
            if event.key == pygame.K_LEFT:
                moving_left = True
            if event.key == pygame.K_RIGHT:
                moving_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_RIGHT:
                moving_right = False

    #8 - Do any "per frame" actions (move objects, add or remove items)
    
    # If the up key is pressed, the player will move up due to the y velocity being changed
    player.y += vel_y
    if player.y < WINDOW_HEIGHT - PLAYER_SIZE and vel_y < 0:  # if the player is in the air and moving up, decrease the y velocity by the "up gravity" value 
        vel_y += UP_GRAVITY
    if player.y < WINDOW_HEIGHT - PLAYER_SIZE and vel_y >= 0:  # if the player is in the air and moving down, increase the y velocity by the "down gravity" value 
        vel_y += DOWN_GRAVITY
    if player.y >= WINDOW_HEIGHT - PLAYER_SIZE:  # When the player hits the ground, set the y velocity to 0 to stop it.
        vel_y = 0
        player.y = WINDOW_HEIGHT - PLAYER_SIZE  # This line corrects for any occurence where the player moves just below the bottom of the screen in a single frame
    
    # Move the player left and right, but not off the screen
    if moving_left == True and player.x > 0:
        player.x -= PLAYER_VELOCITY
    if moving_right == True and player.x < (WINDOW_WIDTH - PLAYER_SIZE):
        player.x += PLAYER_VELOCITY

    #9 - Clear the window
    window.fill(BLACK)

    #10 - Draw all window elements
    pygame.draw.rect(window, BLUE, player)

    #11 - Update the window
    pygame.display.update()

    #12 - Set frame rate to slow things down
    clock.tick(FPS)
