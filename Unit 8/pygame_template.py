# Pygame Template

# 1 - import packages
import pygame
from pygame.locals import *
import sys
pygame.font.init()

def main():
    #2 - Define constants
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    WINDOW_WIDTH = 640
    WINDOW_HEIGHT = 480
    FPS = 30

    #3 - Initialize the world
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    
    # Display Instructions
    duration = 10000
    INSTRUCTIONS_FONT = pygame.font.SysFont('comicsans', 20)
    start_ticks = pygame.time.get_ticks()
    should_break = False
    while pygame.time.get_ticks() - start_ticks < duration:
        if should_break:
            break
        window.fill(WHITE)
        instructions = ['Created by _____________',
        'Press enter to skip at any time',
        'Explain how to play your game here',
        'Break up instructions so they fit on screen.',
        'Add more items to this list if necessary.']
        for i, instruction in enumerate(instructions):
            draw_text = INSTRUCTIONS_FONT.render(instruction, 1, BLACK)
            window.blit(draw_text, (WINDOW_WIDTH//2 - draw_text.get_width()//2, 100 + i *50))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    should_break = True
                    break
        pygame.display.update()
    window.fill(BLACK)

    #4 - Load assets: images, sounds, etc.

    #5 - Initialize variables

    #6 - Define functions


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


        #9 - Do any "per frame" actions (move objects, add or remove items)

        #10 - Clear the window
        window.fill(BLACK)

        #11 - Draw all window elements

        #12 - Update the window
        pygame.display.update()

        #13 - Set frame rate to slow things down
        clock.tick(FPS)


if __name__ == "__main__":
    main()



