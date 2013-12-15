#World_RTS
#Version: 0.1
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
tile_height = (((screen_height)/tiles_per_side))
OLIVE = (107, 142, 35)
BLACK = (0, 0, 0)
BLUE = (0, 0, 205)
GREY = (105, 105, 105)
line_width = 2
simple_map = [[2, 2, 1, 1, 1, 1, 1, 1, 0, 0],[2, 2, 1, 1, 1, 1, 1, 1, 0, 0],[2, 2, 1, 1, 1, 1, 1, 1, 0, 0],
              [2, 2, 1, 1, 1, 1, 1, 1, 0, 0],[2, 2, 1, 1, 0, 1, 1, 1, 0, 0],[2, 2, 1, 1, 1, 1, 1, 1, 0, 0],
              [2, 2, 1, 1, 1, 1, 1, 1, 0, 0],[2, 2, 1, 1, 1, 1, 1, 1, 0, 0],[2, 2, 1, 1, 1, 1, 1, 1, 0, 0],
              [2, 2, 1, 1, 1, 1, 1, 1, 0, 0]]

"""

initialize

"""
def main():
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('World RTS')

    #set top corner of tile_positions
    coord_trans = []
    for j in range(0, tiles_per_side):
        coord_trans_in = []
        for i in range(0, tiles_per_side):
            coord = [(tile_width)*(i), (tile_height)*(j)]
            coord_trans_in.append(coord)
        coord_trans.append(coord_trans_in)
    
    #make tiles
    tile_list = []
    for j in range(0, tiles_per_side):
        tile_list_in = []
        for i in range(0, tiles_per_side):
            tile = the_map.tile(coord_trans[i][j], [i,j], simple_map[i][j])
            tile.draw_tile(screen, tile_width, tile_height)
            tile_list_in.append(tile)
        tile_list.append(tile_list_in)

    #background = pygame.Surface(screen.get_size())
    #background = background.convert()
    #background.fill(OLIVE) #temporary green olive drab - 107-142-35
    screen.fill(OLIVE) 

        
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
                        

        for j in range(0, len(tile_list)):
            tile_list_in = tile_list[j] 
            for i in range(0, len(tile_list_in)):
                tile = tile_list_in[i]
                tile.draw_tile(screen, tile_width, tile_height)
        pygame.display.flip()

    pygame.display.flip()


    

main()

