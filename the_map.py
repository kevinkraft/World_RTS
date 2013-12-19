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
        pygame.draw.rect(self.surface, colour, [0, 0, tile_width, tile_height])
        pointlist = [[0 ,0], [tile_width, 0], [tile_width, tile_height], [0, tile_height], [0, 0]]
        pygame.draw.lines(self.surface, line_colour, False, pointlist, line_width)
        screen.blit(self.surface, self.screen_pos)

