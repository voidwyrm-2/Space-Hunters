import pygame




def checkXkeys(keyevent, *keys):
    for i in keys:
        if keyevent == pygame.K_ESCAPE: return True
    return False