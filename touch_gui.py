#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import time
import os
import sys

# GUI Setting from here------
pygame.init()
pygame.mouse.set_visible(1)

size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
print ("Framebuffer size: %d x %d" % (size[0], size[1]))
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
title_font = pygame.font.Font(os.path.join('/usr/share/fonts/truetype/fonts-japanese-gothic.ttf'), 48)
body_font = pygame.font.Font(os.path.join('/usr/share/fonts/truetype/fonts-japanese-gothic.ttf'), 32)
fpsclock = pygame.time.Clock()
# ----------- GUI

def make_button(text, xpo, ypo, height, width, colour):
    label=body_font.render(str(text), 1, (colour))
    screen.blit(label,(xpo,ypo))
    pygame.draw.rect(screen, (255,255,255), (xpo-10,ypo-10,width,height),3)

def screen_clear():
    screen.fill((0,0,0))
    pygame.display.update()

def screen_opening():
    title = title_font.render(u'オープニング', True, (255,255,255))
    screen.fill((0,0,0))
    screen.blit(title, (30,100))
    pygame.display.update()
    time.sleep(3)
    screen_clear()

def screen_home():
    global hmi_state
    hmi_state = HOME_STATE

    screen.fill((0,0,0))

    make_button(u"ボタン1", 100, 100 , 55, 300, (255,255,255))
    make_button(u"ボタン2", 100, 200 , 55, 300, (255,255,255))
    make_button(u"ボタン3", 100, 300 , 55, 300, (255,255,255))

    pygame.display.update()

def on_touch():
    # get the position that was touched
    touch_pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
    #  x_min                 x_max   y_min                y_max
    # shutter button event
    if 100 <= touch_pos[0] <= 400 and 95 <= touch_pos[1] <=160:
        return 'button1' 

    # gan button event
    if 100 <= touch_pos[0] <= 400 and 195 <= touch_pos[1] <=260:
        return 'button2'

    # digi2ana button event
    if 100 <= touch_pos[0] <= 400 and 295 <= touch_pos[1] <=360:
        return 'button3' 

if __name__ == '__main__':
    screen_opening()

    screen_home()

    while True:
        fpsclock.tick(10)
        for event in pygame.event.get():
            #if event.type == pygame.MOUSEBUTTONDOWN or event.type == MOUSEMOTION:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                #print(pos) #for checking
                pygame.draw.circle(screen, (255,255,255), pos, 2, 0) #for debugging purposes - adds a small dot where the screen is pressed
                pygame.display.update()

                button = on_touch() 
                if button == 'button1':
                    print('button1')
                    # event of button1
                if button == 'button2':
                    print('button2')
                    # event of button2
                if button == 'button3':
                    print('button3')
                    # event of button3

            #ensure there is always a safe way to end the program if the touch screen fails
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
