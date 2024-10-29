# Drawing with Rect Objects Example

# 1 - import packages
import pygame
from pygame.locals import *
import sys
pygame.font.init()

def main():
    #2 - Define constants
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    WINDOW_WIDTH = 640
    WINDOW_HEIGHT = 480
    FPS = 20
    VEL_X = 5
    VEL_Y = 5
    BVEL_X = -5
    BVEL_Y = 5
    rect_x = 400
    rect_y = 200
    size = 50
    GAME_OVER_FONT = pygame.font.SysFont('comicsans', 100)

    #3 - Initialize the world
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    #4 - Load assets: images, sounds, etc.
    pygame.draw.rect(window, RED, (rect_x, rect_y, size, size))   # Disconnected rectangle and Rect object
    red_Rect = pygame.Rect(400, 200, size, size)
    
    blue_Rect = pygame.Rect(200, 100, size, size)   # Synced up rectangle and Rect object
    pygame.draw.rect(window, BLUE, blue_Rect)

    #5 - Initialize variables

    #6 - Define functions
    def game_over():
        draw_text = GAME_OVER_FONT.render("Game Over", 1, WHITE)
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
        if red_Rect.colliderect(blue_Rect):  # Check to see if the two Rect objects collide
            game_over()
            
        # Move the red rectangle, but don't move it's rect object
        if rect_x < 0:
            VEL_X = -VEL_X
        if rect_y < 0:
            VEL_Y = -VEL_Y
        if rect_y > WINDOW_HEIGHT - size:
            VEL_Y = -VEL_Y
        if rect_x > WINDOW_WIDTH - size:
            VEL_X = -VEL_X
        rect_x += VEL_X
        rect_y += VEL_Y

        # Move the blue rectangle with it's rect object
        if blue_Rect.x < 0:
            BVEL_X = -BVEL_X
        if blue_Rect.y < 0:
            BVEL_Y = -BVEL_Y
        if blue_Rect.y > WINDOW_HEIGHT - size:
            BVEL_Y = -BVEL_Y
        if blue_Rect.x > WINDOW_WIDTH - size:
            BVEL_X = -BVEL_X
        blue_Rect.x += BVEL_X
        blue_Rect.y += BVEL_Y


        #10 - Clear the window
        window.fill(BLACK)

        #11 - Draw all window elements
        pygame.draw.rect(window, RED, (rect_x, rect_y, size, size))   # Drawing the red rect
        pygame.draw.rect(window, BLUE, blue_Rect)   # Drawing the blue rect over using the blue Rect attributes
        pygame.draw.rect(window, GREEN, red_Rect)   # Drawing the Rect object that is supposed to follow the red rectangle, but doesn't
        
        #12 - Update the window
        pygame.display.update()

        #13 - Set frame rate to slow things down
        clock.tick(FPS)


if __name__ == "__main__":
    main()



