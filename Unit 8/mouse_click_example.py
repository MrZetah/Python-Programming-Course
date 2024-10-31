# Pygame Template

# 1 - import packages
import pygame
from pygame.locals import *
import sys
pygame.font.init()
import random

class MyRect(pygame.Rect):
    '''Create my own Rect class that inherits from pygame's Rect class, but adds attributes for this particular game'''
    def __init__(self, left, top, width, height, x_vel, y_vel):
        super().__init__(left, top, width, height)
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.clicked = True

def main():
    #2 - Define constants
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    WINDOW_WIDTH = 640
    WINDOW_HEIGHT = 480
    FPS = 30
    target_size = 20
    targets = []        # create an emtpy list to store target rects and their corresponding x and y velocities and whether they have been hit or not
    score = 0
    SCORE_FONT = pygame.font.SysFont('comicsans', 20)   #Create variables with font information for text
    GAME_OVER_FONT = pygame.font.SysFont('comicsans', 100)
    
    #3 - Initialize the world
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    

    #4 - Load assets: images, sounds, etc.
    for i in range(0, 25):
        x = random.randint(0, WINDOW_WIDTH - target_size)
        y = random.randint(0, WINDOW_HEIGHT - target_size)
        x_vel = random.randint(-8, 8)
        y_vel = random.randint(-8, 8)
        target_rect = MyRect(x, y, target_size, target_size, x_vel, y_vel)  # Set attributes of Rect object including velocities
        targets.append(target_rect)   # Store target rect with speed variables. Set 3rd index to True until it gets hit by mouse
        

    #5 - Initialize variables

    #6 - Define functions
    def game_over():
        draw_text = GAME_OVER_FONT.render("Score: " + str(score), 1, WHITE)
        window.blit(draw_text, (WINDOW_WIDTH//2 - draw_text.get_width()//2, WINDOW_HEIGHT//2 - draw_text.get_height()//2))
        pygame.display.update()
        pygame.time.delay(5000)
        pygame.quit()


    #7 - Loop forever
    while True:

        #8 Check for and handle events
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                for target in targets:
                    if target.collidepoint(event.pos) and target.clicked == True:   # Check to see if mouse clicks on a target that hasn't been hit yet
                        score += abs(target.x_vel)+ abs(target.y_vel)   # add together absolute value of x and y velocity - faster moving targets are worth more points
                        target.clicked = False       # This prevents the rect object from being drawn to the screen or re-clicked once it has been hit
        if pygame.time.get_ticks()/1000 > 10:
            game_over()
            
        #9 - Do any "per frame" actions (move objects, add or remove items)
        for target in targets:
            target.x += target.x_vel   # Move each rect object by its x and y velocity
            target.y += target.y_vel
            
            # Check each target to see if it has hit a wall and flip it's x, y direction if it has
            if target.x < 0:
                target.x_vel *= -1
            if target.x > WINDOW_WIDTH - target_size:
                target.x_vel *= -1
            if target.y < 0:
                target.y_vel *= -1
            if target.y > WINDOW_HEIGHT - target_size:
                target.y_vel *= -1
                
        #10 - Clear the window
        window.fill(BLACK)

        #11 - Draw all window elements
        for target in targets:
            if target.clicked:
                # Only print rect objects that haven't been hit yet.
                pygame.draw.rect(window, BLUE, target)   
        
        score_text = SCORE_FONT.render("Score: " + str(score), 1, WHITE)
        window.blit(score_text, (10, 10))
        #12 - Update the window
        pygame.display.update()

        #13 - Set frame rate to slow things down
        clock.tick(FPS)


if __name__ == "__main__":
    main()



