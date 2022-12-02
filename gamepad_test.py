# reference:
# https://note.com/npaka/n/n7b799597e706
import pygame
from pygame.locals import *

pygame.joystick.init()
try:
   joystick = pygame.joystick.Joystick(0)
   joystick.init()
   print('Game pad name:', joystick.get_name())
   print('Nuber of buttons :', joystick.get_numbuttons())
except pygame.error:
   print('error not connect game pad')

pygame.init()

print('Press any buttons of game pad')

while True:
   for e in pygame.event.get():
       if e.type == pygame.locals.JOYAXISMOTION:
           print('control key:', joystick.get_axis(0), joystick.get_axis(1))
       elif e.type == pygame.locals.JOYBUTTONDOWN:
           print('button '+str(e.button)+' is pressed')
       elif e.type == pygame.locals.JOYBUTTONUP:
           print('button '+str(e.button)+' is released')
