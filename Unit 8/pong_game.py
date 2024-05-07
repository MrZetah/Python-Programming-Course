import pygame
import random
pygame.font.init()

WIDTH, HEIGHT = 900, 500   #All caps because they won't change in program
WIN = pygame.display.set_mode((WIDTH, HEIGHT))   #Creates main display window or display surface
pygame.display.set_caption("Basic Pong Game") #Set title of game window

BOUNCE_COUNT_FONT = pygame.font.SysFont('comicsans', 20)   #Create variables with font information for text
LOSER_FONT = pygame.font.SysFont('comicsans', 100)

#Settings
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
FPS = 60
PADDLE_HEIGHT = 15
PADDLE_WIDTH =100
paddle_x = WIDTH//2
paddle_y = HEIGHT-50
ball_x = WIDTH//2
ball_y = 20
BALL_HEIGHT = 15
BALL_WIDTH =15
PADDLE_VEL = 10
ball_vel_x = 0
ball_max_x_vel = 5
ball_vel_y = 3
bounce_count = 0

paddle = pygame.Rect(paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)  #Create two objects
ball = pygame.Rect(ball_x, ball_y, BALL_WIDTH, BALL_HEIGHT)


def paddle_movement(keys_pressed, paddle):
    if keys_pressed[pygame.K_LEFT] and paddle.x > 0:
        paddle.x -= PADDLE_VEL
    if keys_pressed[pygame.K_RIGHT] and paddle.x + PADDLE_WIDTH < WIDTH:
        paddle.x += PADDLE_VEL

def ball_movement(keys_pressed, ball, paddle):
    global ball_vel_x
    global ball_vel_y
    global bounce_count
    if ball.x + BALL_WIDTH > WIDTH:
        ball_vel_x *= -1
    if ball.x < 0:
        ball_vel_x *= -1
    if ball.y < 0:
        ball_vel_y *= -1


    #if paddle.colliderect(ball):   This will detect a collision between objects. It would work with random x velocities, but it won't work for controlled hits.

    if ball.y + BALL_HEIGHT > paddle.y and ball.y + BALL_HEIGHT < paddle.y + PADDLE_HEIGHT:  #Deleting the second condition will make the ball come back up if it passes under the paddle
        if ball.x + BALL_WIDTH > paddle.x and ball.x < paddle.x + PADDLE_WIDTH:
            ball_vel_y *= -1
            ball_vel_x = ((ball.x + BALL_WIDTH//2) - paddle.x)/PADDLE_WIDTH * ball_max_x_vel * 2 - ball_max_x_vel
            #ball_vel_x = random.randint(1, ball_max_x_vel)  this is much easier to code than the line above
            bounce_count = bounce_count + 1



def draw_window(paddle, bounce_count):
    #global bounce_count
    WIN.fill(WHITE)
    bounce_count_text = BOUNCE_COUNT_FONT.render("Bounces: " + str(bounce_count), 1, BLACK)
    WIN.blit(bounce_count_text, (10, 10))
    pygame.draw.rect(WIN, BLUE, paddle)
    pygame.draw.rect(WIN, RED, ball)
    pygame.display.update()

def game_over():
    draw_text = LOSER_FONT.render("Game Over", 1, BLACK)
    WIN.blit(draw_text, (WIDTH//2 - draw_text.get_width()//2, HEIGHT//2 - draw_text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(5000)

def main():
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():  #checks for different events
            if event.type == pygame.QUIT:
                run = False


        keys_pressed = pygame.key.get_pressed()
        paddle_movement(keys_pressed, paddle)
        ball_data = ball_movement(keys_pressed, ball, paddle)
        ball.x += ball_vel_x
        ball.y += ball_vel_y

        if ball.y > HEIGHT:
            game_over()
            break

        draw_window(paddle, bounce_count)

    pygame.quit()

if __name__ == "__main__":
    main()
