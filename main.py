import pygame, sys
from pygame.locals import *
import math

# this class holds the data on what the game will look like
class Design:
  def __init__(self):
    pygame.init()
    pygame.display.set_caption("Alyssa's Awesome Sauce Tic Tac Toe Game")
    
  def show_screen():    
    WIDTH = 600
    HEIGHT = 600
    BKG = (66, 144, 245) 
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(BKG)
    pygame.display.flip()

# this class holds the data on how the game will act 
class Functionality:
  
  def mainloop():
    while True:
	    for event in pygame.event.get():
		    if event.type == pygame.QUIT:
			    sys.exit()