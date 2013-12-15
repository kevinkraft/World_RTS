#World_RTS
#Version: 0.0
#
#Kevin Maguire
#15/12/13
#
#Add:
#  highlight tile
#  print tiles to map


import sys
import pygame
from pygame.locals import *
import the_map

"""

sim parameters

"""
screen_width = 480
screen_height = 480
tiles_per_side = 10
tile_width = (((screen_width)/tiles_per_side))
print tile_width
tile_height = (((screen_height)/tiles_per_side))
OLIVE = (107, 142, 35)
BLACK = (0, 0, 0)
line_width = 2
simple_map = [[2, 2, 1, 1, 1, 1, 1, 1, 0, 0],[2, 2, 1, 1, 1, 1, 1, 1, 0, 0],[2, 2, 1, 1, 1, 1, 1, 1, 0, 0],
              [2, 2, 1, 1, 1, 1, 1, 1, 0, 0],[2, 2, 1, 1, 1, 1, 1, 1, 0, 0],[2, 2, 1, 1, 1, 1, 1, 1, 0, 0],
              [2, 2, 1, 1, 1, 1, 1, 1, 0, 0],[2, 2, 1, 1, 1, 1, 1, 1, 0, 0],[2, 2, 1, 1, 1, 1, 1, 1, 0, 0],
              [2, 2, 1, 1, 1, 1, 1, 1, 0, 0]]

"""

initialize

"""
def main():
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('World RTS')
    

    #make tiles
    tile_list = []
    for i in range(1, tiles_per_side + 1):
        for j in range(1, tiles_per_side + 1):
            tile.tile()


    #background = pygame.Surface(screen.get_size())
    #background = background.convert()
    #background.fill(OLIVE) #temporary green olive drab - 107-142-35
    screen.fill(OLIVE) 
    draw_lines(screen)
    
    

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
                
        #mos_x, mos_y = pygame.mouse.get_pos()
        

    #screen.blit(background, (0, 0))
    pygame.display.flip()


def draw_lines(screen):
    pointlist = []
    for i in range(0, tiles_per_side + 1):
        shift = (tile_width)*(i)
        pointlist = [[shift, 0], [shift, screen_height]]
        pygame.draw.lines(screen, BLACK, False, pointlist, line_width)
    for i in range(0, tiles_per_side + 1):
        shift = (tile_height)*(i)
        pointlist = [[0, shift], [screen_width, shift]]
        pygame.draw.lines(screen, BLACK, False, pointlist, line_width)

def highlight_square():
    #add this
    return
    

main()

