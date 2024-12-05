# pygame demo 1 - draw one image

# 1 - Import packages
import pygame
from pygame.locals import *
import sys

# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
 
# 4 - Load assets: image(s), sound(s),  etc.
x1 = 125
y1 = 225
rect1 = pygame.Rect(x1, y1, 50, 50)

x2 = 100
y2 = 200
rect2 = pygame.Rect(x2, y2, 100, 100)

# 5 - Initialize variables

 
# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end the program 
        if event.type == pygame.QUIT:           
            pygame.quit()  
            sys.exit()
        
        '''This will pull the mouse coordinates only at the time of the mouse click'''
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Check for left mouse button
                rect1.x, rect1.y = pygame.mouse.get_pos()
            rect1.x -= 25   # This math puts the center of the object at the mouse click, not the top left
            rect1.y -= 25    # You may want to pull the width and height of your object and divide it by 2 instead of hard coding the values in
            
        '''This will continually get the coordinates of the mouse as long as it is being pressed'''
        if pygame.mouse.get_pressed()[0]:  # 0 for left button
            rect2.x, rect2.y = pygame.mouse.get_pos()
            rect2.x -= 50
            rect2.y -= 50

    # 8  Do any "per frame" actions
    
    # 9 - Clear the window
    window.fill(BLACK)
    
    # 10 - Draw all window elements
    pygame.draw.rect(window, GREEN, rect2)  # Notice, this rectangle will move with your mouse continually
    pygame.draw.rect(window, RED, rect1)    # This rectangle will only move on the initial click
    

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait
