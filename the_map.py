import sys
import pygame
from pygame.locals import *

OLIVE = (107, 142, 35)
BLACK = (0, 0, 0)
BLUE = (0, 0, 205)
GREY = (105, 105, 105)



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

def zoom_in(tiles_per_side, tiles_per_side_GLOBAL, topleft_grid, tile_list):
    tiles_per_side = tiles_per_side/2
    if tiles_per_side == 0:
        tiles_per_side = 1
    zoom_tile_list = get_zoom_tile_list(topleft_grid, tile_list)
    return (tiles_per_side, tile_list)

def zoom_out(tiles_per_side, tiles_per_side_GLOBAL, topleft_grid, tile_list):
    tiles_per_side = 2*tiles_per_side
    if tiles_per_side > tiles_per_side_GLOBAL:
        tiles_per_side = tiles_per_side_GLOBAL
    zoom_tile_list = get_zoom_tile_list(topleft_grid, tile_list)
    return (tiles_per_side, tile_list)

def get_zoom_tile_list(topleft_grid, tile_list):
    return tile_list
