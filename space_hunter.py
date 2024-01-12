# Space Invader game using python pygame
# Originally reated by Meezan malek
# Edited into something different enough to not infringe on copyright by Nuclear Pasta

import pygame
import random
import math
from pygame import mixer
from pathlib import Path
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
player_icon = pygame.image.load(PLAYER_SPRITES[0])
player_lives = LIVES
playerX = 370
playerY = 480
changedX = 0
playerSpeed = PLAYER_SPEED

player_mode = playerClasses.bounty.sid

max_points = SMAX_POINTS
high_score = 0

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

def show_score(x,y):
    score = font.render(f'Score: {score_value}({high_score})', True, (255, 255, 255))
    screen.blit(score, (x, y))
    needed = font.render(f'Needed: {max_points}', True, (255, 255, 255))
    screen.blit(needed, (x, y + 30))

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


enemy_sprite = pygame.image.load(ENEMY_SPRITES[0])

def createEnemies(enmax: int):
    for i in range(enmax):
        enemyImg.append(enemy_sprite)
        enemyX.append(random.randint(0, 736))
        enemyY.append(random.randint(50, 150))
        enemyX_change.append(4)
        enemyY_change.append(40)


def reloadEnemies(enmax):
    enemyX.clear()
    enemyY.clear()
    createEnemies(enmax)

def reloadEnemySprites(enmax):
    enemyImg.clear()
    for i in range(enmax): enemyImg.append(enemy_sprite)


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
bullet_icon = pygame.image.load(BULLET_SPRITES[0])
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
    if player_mode == 'normal':
        if distance < 27: return True
    elif player_mode == 'heavy': 
        if distance < 49: return True
    elif player_mode == 'tri': 
        if distance < 57: return True
    return False


running = True
should_quit = False; should_breset = False; should_creset = False
add_score = False; VAL_TO_ADD = 1; sval_added = VAL_TO_ADD; should_mas = True
artiloss = False

def basicreset():
    global score_value
    global max_points
    #global sval_added
    global player_lives
    global player_mode
    global artiloss

    #if sval_added != VAL_TO_ADD: complreset(); return
    score_value = 0
    max_points = SMAX_POINTS
    player_lives = LIVES
    player_mode = 'normal'
    artiloss = False
    num_of_enemies = ENEMIES_NUM
    reloadEnemies(num_of_enemies)


def complreset():
    global score_value
    global max_points
    global sval_added
    global player_lives
    global player_mode
    global artiloss

    score_value = 0
    max_points = SMAX_POINTS
    sval_added = VAL_TO_ADD
    player_lives = LIVES
    player_mode = 'normal'
    artiloss = False
    num_of_enemies = ENEMIES_NUM
    reloadEnemies(num_of_enemies)



if Path('resetsave.txt').exists():
    os.remove('resetsave.txt')
    os.remove(SAVEFILE)

if not Path(SAVEFILE).exists():
    print('save file not detected, new one created')
    with open(SAVEFILE, 'xt') as efi: efi.write('')

def save():
    with open(SAVEFILE, 'wt') as ofi:
        if score_value > high_score:
            ofi.write(f'''hscore:{score_value}
mpoints:{max_points}
pmode:{player_mode}
plives:{player_lives}
px:{playerX}
py:{playerY}
byc:{bulletY_changed}
enum:{num_of_enemies}
ex:{enemyX}
ey:{enemyY}''')
        else:
            ofi.write(f'''hscore:{high_score}
mpoints:{max_points}
pmode:{player_mode}
plives:{player_lives}
px:{playerX}
py:{playerY}
byc:{bulletY_changed}
enum:{num_of_enemies}
ex:{enemyX}
ey:{enemyY}''')
    print('all data saved!')

def recall(data: str):
    with open(SAVEFILE, 'rt') as ifi:
        savi = ifi.read()
        if savi == '': return 0
        ssavi = savi.split('\n')
        for sa in ssavi:
            ssa = sa.split(':')
            if ssa[0] == data:
                return ssa[1]


high_score = int(recall('hscore'))
player_mode = recall('pmode')
#if RECALLALL:
    #max_points = int(recall('mpoints'))
    #player_lives = int(recall('plives'))
    #bulletY_changed = int(recall('byc'))
    #num_of_enemies = int(recall('enum'))
# main game loop
while running:

    if should_quit: save(); break
    if should_breset: should_breset = False; basicreset()
    if should_creset: should_creset = False; complreset()

    screen.fill((0, 0, 0))  # background
    screen.blit(backgroungImg, (0, 0))

    if player_lives == 0 or artiloss: game_over(); show_credits(200,350); break

    if player_mode == 'normal': player_icon = playerClasses.bounty.asSprite; bullet_icon = pygame.image.load(BULLET_SPRITES[0]); enemy_sprite = playerClasses.bounty.enSprite; reloadEnemySprites(num_of_enemies)

    if player_mode == 'heavy': player_icon = playerClasses.police.asSprite; bullet_icon = pygame.image.load(BULLET_SPRITES[0]); enemy_sprite = playerClasses.police.enSprite; reloadEnemySprites(num_of_enemies)

    if player_mode == 'tri': player_icon = playerClasses.trilo.asSprite; bullet_icon = pygame.image.load(BULLET_SPRITES[0]); enemy_sprite = playerClasses.trilo.enSprite; reloadEnemySprites(num_of_enemies)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('game was quit!')
            save()
            running = False

        # player movement functionally
        if event.type == pygame.KEYDOWN:
            #print("you preesed a key")

            if event.key == pygame.K_ESCAPE: should_quit = True

            #if event.key == pygame.K_r: should_breset = True
            #if event.key == pygame.K_y: should_creset = True

            #if event.key == pygame.K_TAB: artiloss = True; game_over(); show_credits(300,350)

            #if event.key == pygame.K_p and not add_score: add_score = True
            #elif event.key == pygame.K_p and add_score: add_score = False

            if event.key == pygame.K_LEFT or event.key == pygame.K_a: print("left key pressed"); changedX = -playerSpeed

            if event.key == pygame.K_RIGHT or event.key == pygame.K_d: print("right key pressed"); changedX = playerSpeed

            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound(MUSICS[1])
                    if MUSIC_CONFIG['shoot']: bullet_sound.play()
                    bulletX = playerX
                    bullet_state = "fired"
                    print('bullet fired!')
            
            if event.key == pygame.K_1: print(f'player sprite is now {playerClasses.bounty.asSprite}'); player_mode = playerClasses.bounty.sid
            if event.key == pygame.K_2: print(f'player sprite is now {playerClasses.police.asSprite}'); player_mode = playerClasses.police.sid
            if event.key == pygame.K_3: print(f'player sprite is now {playerClasses.police.asSprite}'); player_mode = playerClasses.trilo.sid

        if event.type == pygame.KEYUP and (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d):
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
            reloadEnemies(num_of_enemies); player_lives -= 1
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

    if bullet_state == "fired":
        bullet(bulletX, bulletY)
        bulletY -= bulletY_changed

    if score_value >= max_points:
        max_points *= 2
        num_of_enemies += 2 
        bulletY_changed += 1
        reloadEnemies(num_of_enemies)

    if add_score:
        score_value += sval_added
        if should_mas: sval_added *= 2

    show_score(10,10)
    show_lives(10, 70)

    player(playerX, playerY)
    pygame.display.update()
    if should_quit: pygame.quit()