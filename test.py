# coding=utf-8


import pygame
import sys, math
import time
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((800,600))
myfont = pygame.font.Font(None,50)
text = "hhh，大撒子"
white = 255,255,255
blue = 0,0,255
textImage = myfont.render("Hello dasazi", True, white)
pygame.display.set_caption('Drawing Rectangles')
pos_x = 0
pos_y = 0
vel_x = 2
vel_y = 1


while True:
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            sys.exit()
    screen.fill(blue)
    screen.blit(textImage, (100, 100))
    pygame.display.update()
    color = 255,255,0
    position = 300,250
    radius = 100
    width = 10
    # pygame.draw.circle(screen,color,position,radius,width)
    # pygame.display.update()

    pos_x += vel_x
    pos_y += vel_y

    if pos_x > 600 or pos_x < 0:
        vel_x = -vel_x
    if pos_y > 500 or pos_y < 0:
        vel_y = -vel_y

    color = 255,255,0
    width = 0
    pos = pos_x, pos_y, 200, 100
    pygame.draw.rect(screen, color, pos, width)
    start_angle = math.radians(0)
    end_angle = math.radians(360)
    arc_color = 222,222,222
    arc_pos = 10,110,100,150
    pygame.draw.arc(screen, arc_color, arc_pos, start_angle, end_angle, 8)
    pygame.display.update()
    time.sleep(0.005)


