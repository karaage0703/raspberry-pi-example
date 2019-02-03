#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import time
import os
import sys

pygame.init()

size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
print ("Framebuffer size: %d x %d" % (size[0], size[1]))
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
sysfont = pygame.font.SysFont(None, 200)
fpsclock = pygame.time.Clock()

hello = sysfont.render("Alpabet Game", False, (0,0,0))

def screen_opening():
    screen.fill((255,255,255))
    screen.blit(hello, (size[0]/5 , size[1]/3))
    pygame.display.update()

def display_word(word):
    print(word)
    display_word = sysfont.render(word, False, (0,0,0))

    screen.fill((255,255,255))
    screen.blit(display_word, (size[0]/4 , size[1]/3))
    pygame.display.update()

if __name__ == '__main__':
    screen_opening()

    while True:
        fpsclock.tick(10)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_a:
                    display_word('alligator')

                if event.key == K_b:
                    display_word('bear')

                if event.key == K_c:
                    display_word('cat')

                if event.key == K_d:
                    display_word('dog')

                if event.key == K_e:
                    display_word('elephant')

                if event.key == K_f:
                    display_word('fish')

                if event.key == K_g:
                    display_word('grapes')

                if event.key == K_h:
                    display_word('hat')

                if event.key == K_i:
                    display_word('ice cream')

                if event.key == K_j:
                    display_word('juice')

                if event.key == K_k:
                    display_word('koala')

                if event.key == K_l:
                    display_word('lion')

                if event.key == K_m:
                    display_word('monkey')

                if event.key == K_n:
                    display_word('nuts')

                if event.key == K_o:
                    display_word('orange')

                if event.key == K_p:
                    display_word('penguin')

                if event.key == K_q:
                    display_word('queeen')

                if event.key == K_r:
                    display_word('rabbit')

                if event.key == K_s:
                    display_word('star')

                if event.key == K_t:
                    display_word('train')

                if event.key == K_u:
                    display_word('umbrella')

                if event.key == K_v:
                    display_word('violin')

                if event.key == K_w:
                    display_word('watch')

                if event.key == K_x:
                    display_word('xylophone')

                if event.key == K_y:
                    display_word('yacht')

                if event.key == K_z:
                    display_word('zebra')

                if event.key == K_ESCAPE:
                    sys.exit()