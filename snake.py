# Creating a snake game...
from tkinter import font
import pygame
import os
import random

pygame.mixer.init()

pygame.init()

#colors:-->
white =(255, 255, 255)
red = (255, 0 ,0)
black = (0, 0, 0)

# Creating window..
screen_width = 900
screen_height = 500
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Adding background image
bgimg = pygame.image.load("backgroung.jpg")
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height))

pygame.display.set_caption("Snake Game")
pygame.display.update()

clock = pygame.time.Clock()
# To add score on screen
font= pygame.font.SysFont(None, 50)
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def welcome():
    exit_game = False
    while not exit_game:
        bgimg = pygame.image.load("hm_sc.jpg")
        bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height))
        gameWindow.blit(bgimg, (0,0))
        text_screen("Snake Game By Dev", black, 260, 110)
        text_screen("Welcome to Snakes", black, 260, 350)
        text_screen("Press Space Bar To Play", black, 232, 390)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('home_screen.mp3')
                    pygame.mixer.music.play()

                    gameloop()
        pygame.display.update()
        clock.tick(60)


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

# Game Loop..
def gameloop():
    # Game specific Variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 30
    init_velocity = 3
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1
    # Check if hiscore.txt exists:
    if(not os.path.exists("hiscore.txt")):
        with open("hiscore.txt", "w") as f:
            f.write("10")

    with open("hiscore.txt", "r", encoding='utf_8') as f:
        hiscore = f.read()

    score= 0
    food_x = random.randint(0, screen_width/2)
    food_y = random.randint(0, screen_height/2)
    fps= 60
    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w", encoding='utf_8') as f:
                f.write(str(hiscore))

            # gameWindow.fill(black)
            bg_img = pygame.image.load("game-over.jpg")
            bg_img = pygame.transform.scale(bg_img, (screen_width, screen_height))
            gameWindow.blit(bg_img, (0,0))
            text_screen("Game Over! Press enter to continue..", black , 150, 350)
            text_screen("Hiscore: " + str(hiscore), black, 340, 125)
            
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            exit_game = True

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            welcome()
                    
        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_q:
                        score += 10

            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x-food_x)<10 and abs(snake_y- food_y)<10:
                score += 10
                food_x = random.randint(0, screen_width/2)
                food_y = random.randint(0, screen_height/2)
                snk_length += 5
                if score> int(hiscore):
                    hiscore = score
                    
            gameWindow.fill(white)
            gameWindow.blit(bgimg, (0,0))
            text_screen("Score: " + str(score) + "  Hiscore: "+str(hiscore), red, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()

            if snake_x<0 or snake_x> screen_width or snake_y<0 or snake_y> screen_height:
                game_over = True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()
                print("Game Over!")

            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()