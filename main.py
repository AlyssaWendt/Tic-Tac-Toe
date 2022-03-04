import pygame, sys
from pygame.locals import *
import math

# this class holds the data on what the game will look like
class Design:
  WIDTH = 600
  HEIGHT = 600
  BKG = (34, 100, 186)
  LINE_COLOR = (43, 186, 214)
  BOARD_ROWS = 15
  Board_COL = 15
  SQUARE_SIZE = 200
  LINE_WIDTH = 15
  SPACE = 55
  
  
  pygame.init()
    
    
  def show_screen(): 
    pygame.display.set_caption("Alyssa's Awesome Sauce Tic Tac Toe Game")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(BKG)
 

  def draw_board():
    # horizontal lines
    pygame.line(screen, LINE_COLOR, (0,SQUARE_SIZE),(SQUARE_SIZE, WIDTH))
    pygame.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH )

    # vertical lines
    pygame.line(screen, LINE_COLOR, (SQUARE_SIZE,0),(SQUARE_SIZE, HEIGHT))
    pygame.line(screen, LINE_COLOR, (0, 2 *  SQUARE_SIZE ), ( 2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH )

    


# this class holds the data on how the game will act 
class Functionality:
  
  def mainloop():
    while True:
	    for event in pygame.event.get():
		    if event.type == pygame.QUIT:
			    sys.exit()