import pygame




def checkXkeys(keyevent, *keys):
    for i in keys:
        if keyevent == pygame.K_ESCAPE: return True
    return False


def log(data):
    with open('logs.txt', 'at') as lf: lf.write(data + '\n')

def clearfile(path):
    with open(path, 'wt') as lf: lf.write('')