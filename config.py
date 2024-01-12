import os




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
    'PoliceCruiser.png'
]

BULLET_SPRITES = [
    'BrassBullet.png'
]

ENEMY_SPRITES = [
    'Greeben-flat.png',
    'Tengen-flat.png'
]