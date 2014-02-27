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

def zoom_in(tiles_per_side, screen_width, screen_height, tiles_per_side_GLOBAL, topleft_grid_onscreen, toolbar_height, tile_list, screen,
            line_width):
    tiles_per_side = tiles_per_side/2
    if tiles_per_side < 3:
        tiles_per_side = 3
    tile_width, tile_height = reassign_tile_variables(screen_width, screen_height, tiles_per_side)
    tile_list = get_new_tile_list(tiles_per_side_GLOBAL, topleft_grid_onscreen, tile_width, tile_height, toolbar_height, tile_list, screen,
                              line_width, tiles_per_side)
    return tile_list, tile_width, tile_height, tiles_per_side
    
def zoom_out(tiles_per_side, screen_width, screen_height, tiles_per_side_GLOBAL, topleft_grid_onscreen, toolbar_height, tile_list, screen,
             line_width):
    tiles_per_side = 2*tiles_per_side
    if tiles_per_side > tiles_per_side_GLOBAL:
        tiles_per_side = tiles_per_side_GLOBAL
    tile_width, tile_height = reassign_tile_variables(screen_width, screen_height, tiles_per_side)
    tile_list = get_new_tile_list(tiles_per_side_GLOBAL, topleft_grid_onscreen, tile_width, tile_height, toolbar_height, tile_list, screen,
                              line_width, tiles_per_side)
    return tile_list, tile_width, tile_height, tiles_per_side

def get_new_tile_list(tiles_per_side_GLO, topleft_grid_onscreen, tile_width, tile_height, toolbar_height, tile_list, screen, line_width,
                  tiles_per_side):
    
    top_left_screen_pos_x = (-1)*(topleft_grid_onscreen[0])*(tile_width)
    top_left_screen_pos_y = (-1)*(topleft_grid_onscreen[1])*(tile_height)
    
   #set top corner of tile_positions with new zoom/scroll
    coord_trans = [] #arrary of the top left corner of screen coords of each tile in the corresponding grid coords
    for j in range(0, tiles_per_side_GLO):
        coord_trans_in = []
        for i in range(0, tiles_per_side_GLO):
            coord = [top_left_screen_pos_x + (tile_width)*(i), top_left_screen_pos_y + (tile_height)*(j) + toolbar_height]
            coord_trans_in.append(coord)
        coord_trans.append(coord_trans_in)

    screen.fill(BROWN)
    
    new_tile_list = []
    for j in range(0, tiles_per_side_GLO):
        tile_list_in = tile_list[j]
        new_tile_list_in = []
        for i in range(0, tiles_per_side_GLO):
            tile = tile_list_in[i]
            tile.screen_pos = coord_trans[i][j]
            tile.draw_tile(screen, tile_width, tile_height, line_width, BLACK)
            new_tile_list_in.append(tile)
        new_tile_list.append(new_tile_list_in)
        
    return new_tile_list

def reassign_tile_variables(screen_width, screen_height, tiles_per_side):
    tile_width = (((screen_width)/tiles_per_side))
    tile_height = (((screen_height)/tiles_per_side))
    return (tile_width, tile_height)
