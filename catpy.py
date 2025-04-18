import pygame, sys

pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

DISPLAYSURF =  pygame.display.set_mode((600,600),0,32)
pygame.display.set_caption('catBomb')

BLACK = (0, 0, 0)

cat_image = pygame.image.load('cat.png')
bomb_image = pygame.image.load('bomb.png')

cat = cat_imgae.get_rect(centerx=300, bottom=600)
bomb = bomb_image.get_rect(left=100, top=100)
