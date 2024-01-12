import os
import pygame




SAVEFILE = 'save.txt'

PLAYER_SPEED = 11
LIVES = 3
BULLET_SPEED = 15
ENEMIES_NUM = 6
SMAX_POINTS = 6

RECALLALL = True


MUSIC_CONFIG = {
    'background': False,
    'shoot': False,
    'edeath': False
}


#0: background music
#1: shoot sound
#2: enemy death sound
MUSICS = [
    'background.wav',
    'laser.wav',
    'explosion.wav'
]


#0: app icon
#1: background
#2: player sprite
#3: bullet sprite
#4: enemy sprite
SPRITES = [
    'SpaceHunter-42B.png',
    'background.png',
    'SpaceHunter-42B.png',
    'BrassBullet.png',
    'Greeben-flat.png'
]


PLAYER_SPRITES = [
    'SpaceHunter-42B.png',
    'PoliceCruiser.png',
    'Trinloite-J73.png'
]

BULLET_SPRITES = [
    'BrassBullet.png'
]

ENEMY_SPRITES = [
    'Greeben-flat.png',
    'Tengen-flat.png',
    'Uufoo-flat.png'
]


class playerClasses:
    class shipbase:
        sid = 'debug'
        name = 'Gunship-SA-X'
        lore = '''An oddly familiar ship'''
        slore = 'An oddly familiar ship', ''
        sdex = -1
        asSprite = pygame.image.load('SpaceHunter-42B.png')
        enSprite = pygame.image.load('SpaceHunter-42B.png')


    class bounty:
        sid = 'normal'
        name = 'Spacehunter-42B'
        lore = '''The Greeben are wanted across the galaxy!\n
        And Trex Rin is on a mission to capture them all and nab that sweet sweet paycheck!'''
        slore = 'The Greeben are wanted across the galaxy!', 'And Trex Rin is on a mission to capture them all and nab that sweet sweet paycheck!'
        sdex = 0
        asSprite = pygame.image.load(PLAYER_SPRITES[sdex])
        enSprite = pygame.image.load(ENEMY_SPRITES[sdex])
    
    class police:
        sid = 'heavy'
        name = 'PC-371' #PC -> Police Cruiser
        lore = '''The Tengen have escaped from Galactica Prison!\n
        And Ho Eo is on the case in his PC-371!'''
        slore = 'The Tengen have escaped from Galactica Prison!', 'And Ho Eo is on the case in his PC-371!'
        sdex = 1
        asSprite = pygame.image.load(PLAYER_SPRITES[sdex])
        enSprite = pygame.image.load(ENEMY_SPRITES[sdex])

    class trilo:
        sid = 'tri'
        name = 'Trinloite-J73'
        lore = '''Renound space adventurer Gen Han is in a bit of a situation!\n
        His mortal enemies, the Uufoo, have found his location and they don't look too friendly!'''
        slore = 'Renound space adventurer Gen Han is in a bit of a situation!', 'His mortal enemies, the Uufoo, have found his location and they don\'t look too friendly!'
        sdex = 2
        asSprite = pygame.image.load(PLAYER_SPRITES[sdex])
        enSprite = pygame.image.load(ENEMY_SPRITES[sdex])