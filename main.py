#World_RTS
#Version: 0.0
#
#Kevin Maguire
#15/12/13
#

import sys
import pygame
from pygame.locals import *

"""

sim parameters

"""
screen_width = 640
screen_height = 480
tile_width = int(round((screen_width)/10))
tile_height = int(round((screen_height)/10))
OLIVE = (107, 142, 35)
BLACK = (0, 0, 0)
line_width = 2

"""

initialize

"""
def main():
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('World RTS')
    
    #background = pygame.Surface(screen.get_size())
    #background = background.convert()
    #background.fill(OLIVE) #temporary green olive drab - 107-142-35
    screen.fill(OLIVE) 
    
    #lines
    #pointlist = ((0, 0), (200, 200))
    pointlist = [[0,0],[0, screen_height]]
    for i in range() 
    #pointlist = [[0,0], [0,480], [tile_width, 480], [tile_width, 0]]
    pygame.draw.lines(screen, BLACK, False, pointlist, line_width)


    #Display some text
    #font = pygame.font.Font(None, 36)
    #text = font.render("Hello There", 1, (10, 10, 10))
    #textpos = text.get_rect()
    #textpos.centerx = background.get_rect().centerx
    #background.blit(text, textpos)

    #Blit everything to the screen
    #screen.blit(background, (0, 0))
    pygame.display.flip()

    #Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    #screen.blit(background, (0, 0))
                pygame.display.flip()


main()
