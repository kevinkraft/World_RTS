import sys
import pygame
from pygame.locals import *

OLIVE = (107, 142, 35)
BLACK = (0, 0, 0)
BLUE = (0, 0, 205)
GREY = (105, 105, 105)
BROWN = (139, 69, 19)


class tile(object):
    """

    for map tiles, to contain everything to do with a tile, resources, sprites etc.

    """
    def __init__(self, screen_pos, grid_pos, terrain_type, tile_surface = pygame.Surface((2,2))): #temporary tile_surface, reassigned later
        self.screen_pos = screen_pos
        self.grid_pos = grid_pos
        self.terrain_type = terrain_type
        self.surface = tile_surface

    def get_colour(self):
        if self.terrain_type == 0:
            colour = BLUE
        if self.terrain_type == 1: 
            colour = OLIVE
        if self.terrain_type == 2:            
            colour = GREY
        return colour

    def draw_tile(self, screen, tile_width, tile_height, line_width, line_colour): #includes highlight
        self.surface = pygame.Surface((tile_width, tile_height))
        colour = self.get_colour()
        pygame.draw.rect(self.surface, colour, [0, 0, tile_width, tile_height]) #[x,y,width height]
        pointlist = [[0 ,0], [tile_width, 0], [tile_width, tile_height], [0, tile_height], [0, 0]]
        pygame.draw.lines(self.surface, line_colour, False, pointlist, line_width)
        screen.blit(self.surface, self.screen_pos)

def zoom_in(tiles_per_side, tiles_per_side_GLOBAL, topleft_grid, tile_list, screen_width, screen_height, screen, line_width, toolbar_height):
    tiles_per_side = tiles_per_side/2
    if tiles_per_side == 0:
        tiles_per_side = 1
    tile_width, tile_height = reassign_tile_variables(screen_width, screen_height, tiles_per_side)
    zoom_tile_list = get_zoom_tile_list(topleft_grid, tiles_per_side, tile_list, tile_width, tile_height, screen, line_width, toolbar_height)
    return (tiles_per_side, zoom_tile_list, tile_width, tile_height) 

def zoom_out(tiles_per_side, tiles_per_side_GLOBAL, topleft_grid, tile_list, screen_width, screen_height, screen, line_width, toolbar_height):
    tiles_per_side = 2*tiles_per_side
    if tiles_per_side > tiles_per_side_GLOBAL:
        tiles_per_side = tiles_per_side_GLOBAL
    tile_width, tile_height = reassign_tile_variables(screen_width, screen_height, tiles_per_side)
    zoom_tile_list = get_zoom_tile_list(topleft_grid, tiles_per_side, tile_list, tile_width, tile_height, screen, line_width, toolbar_height)
    return (tiles_per_side, zoom_tile_list, tile_width, tile_height) 

def reassign_tile_variables(screen_width, screen_height, tiles_per_side):
    tile_width = (((screen_width)/tiles_per_side))
    tile_height = (((screen_height)/tiles_per_side))
    return (tile_width, tile_height)

def get_zoom_tile_list(topleft_grid, tiles_per_side, tile_list, tile_width, tile_height, screen, line_width, toolbar_height):
    
    #set top corner of tile pos
    coord_trans = [] #screen_pos of tiles in array which does not represent the grid pos of the tiles used
    for j in range(topleft_grid[1], tiles_per_side + topleft_grid[1]):
        #print "first j is %i" %j
        coord_trans_in = []
        for i in range(topleft_grid[0], tiles_per_side + topleft_grid[0]):
            #print "first i is %i" %i
            coord = [(tile_width)*(i), (tile_height)*(j) + toolbar_height] #THIS IS NOT THE (i, j)TH COORD OF coord_trans
            coord_trans_in.append(coord)
        coord_trans.append(coord_trans_in)
    print coord_trans
    print len(coord_trans)
    print len(coord_trans[0])
    
    #fill screen to cover up rounding error which causes the old screen to be visible behind the new screen 
    screen.fill(BROWN) 
    
    zoom_tile_list = []
    i = 0
    j = 0
    for k in range(topleft_grid[1], tiles_per_side + topleft_grid[1]):
        print "j is %i" %j
        #print "second k is %i" %k
        tile_list_in = tile_list[k]
        zoom_tile_list_in = []
        for l in range(topleft_grid[0], tiles_per_side + topleft_grid[0]):
            print "i is %i" %i
            #print "second l is %i" %l
            tile = tile_list_in[l]
            tile.screen_pos = coord_trans[i][j]
            tile.draw_tile(screen, tile_width, tile_height, line_width, BLACK)
            zoom_tile_list_in.append(tile)
            i += 1
        zoom_tile_list.append(zoom_tile_list_in)
        i = 0
        j += 1

    ##################################################################
    #this is another attempt, it doesnt work 
    #screen.fill(BROWN)
    ##coord_trans = [] #screen_pos of tiles in array which does not represent the grid pos of the tiles used
    #zoom_tile_list = []
    #for j in range(topleft_grid[1], tiles_per_side + topleft_grid[1]):
    #    #coord_trans_in = [] 
    #    tile_list_in = tile_list[j]
    #    zoom_tile_list_in = []
    #    print "j is %i" %j
    #    for i in range(topleft_grid[0], tiles_per_side + topleft_grid[0]):
    #        coord = [(tile_width)*(i), (tile_height)*(j) + toolbar_height]
    #        #coord_trans_in.append(coord)
    #        print "i is %i" %i
    #        tile = tile_list_in[i]
    #        tile.screen_pos = coord
    #        tile.draw_tile(screen, tile_width, tile_height, line_width, BLACK)
    #        zoom_tile_list_in.append(tile)   
    #    #coord_trans.append(coord_trans_in)
    ##print coord_trans
    ##print len(coord_trans)
    ##print len(coord_trans[0])
    
    pygame.display.flip()

    print "done"
    return zoom_tile_list
