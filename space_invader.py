# Space Invader game using python turtle module
# Created by Meezan malek

import pygame
import random
import math
from pygame import mixer
from pygamefuncs import *
from config import *

# initialize game
pygame.init()

# creating a screen
screen = pygame.display.set_mode((800, 600))  # passing width and height

# title and icon
pygame.display.set_caption("Space Hunter")
icon = pygame.image.load(SPRITES[0])
pygame.display.set_icon(icon)


pygame.font.init()


# Background image
backgroungImg = pygame.image.load(SPRITES[1])

#Background sound
if MUSIC_CONFIG['background']:
    mixer.music.load(MUSICS[0])
    mixer.music.play(-1) #play background music on loop

# defining our player
player_icon = pygame.image.load(SPRITES[2])
player_lives = LIVES
playerX = 370
playerY = 480
changedX = 0
playerSpeed = PLAYER_SPEED

max_points = SMAX_POINTS

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

def show_score(x,y):
    score = font.render("Score: "+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))

def show_lives(x,y):
    lives = font.render("Lives: "+ str(player_lives),True,(255,255,255))
    screen.blit(lives,(x,y))

#game over
def game_over():
    overfont = pygame.font.Font('freesansbold.ttf',64)
    gamefont = overfont.render("GAME OVER",True,(255,255,255))
    screen.blit(gamefont,(200,250))

def show_credits(x,y):
    font2 = pygame.font.Font('freesansbold.ttf',16)
    score = font2.render("A game somewhat created by Nuclear Pasta",True,(255,255,255))
    screen.blit(score,(x,y))

def player(x, y):
    screen.blit(player_icon, (playerX, playerY))


def createEnemies(enmax: int):
    for i in range(enmax):
        enemyImg.append(pygame.image.load(SPRITES[4]))
        enemyX.append(random.randint(0, 736))
        enemyY.append(random.randint(50, 150))
        enemyX_change.append(4)
        enemyY_change.append(40)


def reloadEnemies(enmax):
    enemyX.clear()
    enemyY.clear()
    createEnemies(enmax)


# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = ENEMIES_NUM

createEnemies(num_of_enemies)



def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def resetEnemy(eX, eY, i):
    eX[i] = random.randint(0, 736)
    eY[i] = random.randint(50, 150)

# defining our bullet
bullet_icon = pygame.image.load(SPRITES[3])
bulletX = 0
bulletY = 480
bulletY_changed = BULLET_SPEED  #bullet speed
bullet_state = "ready"


def bullet(x, y):
    global bullet_state
    bullet_state = "fired"
    screen.blit(bullet_icon, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


running = True
should_quit = False
# main game loop
while running:

    if should_quit: break

    screen.fill((0, 0, 0))  # background
    screen.blit(backgroungImg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('game was quit!')
            running = False

        # player movement functionally
        if event.type == pygame.KEYDOWN:
            #print("you preesed a key")

            if event.key == pygame.K_ESCAPE: should_quit = True

            if event.key == pygame.K_TAB:
                game_over()
                show_credits(300,350)
                break

            if event.key == pygame.K_LEFT:
                print("left key pressed")
                changedX = -playerSpeed

            if event.key == pygame.K_RIGHT:
                print("right key pressed")
                changedX = playerSpeed

            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound = mixer.Sound(MUSICS[1])
                    if MUSIC_CONFIG['shoot']: bullet_sound.play()
                    bulletX = playerX
                    bullet_state = "fired"
                    print('bullet fired!')

        if event.type == pygame.KEYUP and (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
            changedX = 0

    # player movement
    playerX += changedX
    # restricting the player inside the window
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy Movement
    for i in range(num_of_enemies):

        # Game Over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over()
            show_credits(300,350)
            break
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            if MUSIC_CONFIG['edeath']: mixer.Sound(MUSICS[2]).play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            resetEnemy(enemyX, enemyY, i)
            print('bullet hit enemy! enemy reset!')
            #enemyX[i] = random.randint(0, 736)
            #enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
        print('bullet never hit an enemy! bullet reset!')

    if bullet_state is "fired":
        bullet(bulletX, bulletY)
        bulletY -= bulletY_changed

    if score_value == max_points:
        max_points *= 2
        num_of_enemies += 2 
        bulletY_changed += 1
        reloadEnemies(num_of_enemies)

    show_score(10,10)
    show_lives(10, 40)

    player(playerX, playerY)
    pygame.display.update()
    if should_quit: pygame.quit()