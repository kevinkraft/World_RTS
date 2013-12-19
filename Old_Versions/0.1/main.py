#World_RTS
#Version: 0.1
#
#Kevin Maguire
#15/12/13
#
#Add:
#  highlight tile (done)
#  print tiles to map (done)
#  grid (done)
#  maybe add xy coords onto screen
#  Menu when tile is clicked
#  Menu which is specific to that tile. 

import sys
import pygame
from pygame.locals import *
import the_map

"""

game parameters

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
HIGHLIGHT_BLUE = (0, 191, 255)
line_width = 3
simple_map = [[2, 2, 1, 1, 1, 1, 1, 1, 0, 0],[2, 2, 1, 1, 1, 1, 1, 1, 0, 0],[2, 2, 1, 1, 1, 1, 1, 1, 0, 0],
              [2, 2, 1, 1, 1, 1, 1, 1, 0, 0],[2, 2, 1, 1, 0, 1, 1, 1, 0, 0],[2, 2, 1, 1, 1, 0, 1, 1, 0, 0],
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
            tile = the_map.tile(coord_trans[i][j], [i,j], simple_map[i][j]) #scree_pos, gird_pos, terrain_type, (opt) surface
            tile.draw_tile(screen, tile_width, tile_height, line_width, BLACK)
            tile_list_in.append(tile)
        tile_list.append(tile_list_in)
        
    #Display some text
    #font = pygame.font.Font(None, 36)
    #text = font.render("Hello There", 1, (10, 10, 10))
    #textpos = text.get_rect()
    #textpos.centerx = background.get_rect().centerx
    #background.blit(text, textpos)

    pygame.display.flip()

    #Event loop
    while 1:

        #redraw tiles with highlight
        for j in range(0, len(tile_list)):
            tile_list_in = tile_list[j]
            for i in range(0, len(tile_list_in)):
                tile = tile_list_in[i]
                if tile.surface.get_rect(topleft = tile.screen_pos).collidepoint(pygame.mouse.get_pos()):
                    line_colour = HIGHLIGHT_BLUE
                    grid_line_width = 2*(line_width)
                else:
                    line_colour = BLACK
                    grid_line_width = line_width
                tile.draw_tile(screen, tile_width, tile_height, grid_line_width, line_colour)
        pygame.display.flip()

        #events
        for event in pygame.event.get():
            #quit game
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        

main()

