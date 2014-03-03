import sys
import pygame
from pygame.locals import *

OLIVE = (107, 142, 35)
BLACK = (0, 0, 0)
BLUE = (0, 0, 205)
GREY = (105, 105, 105)
BROWN = (139, 69, 19)
menu_YELLOW = (255, 255, 0)

class menu(object):
    """

    for all menus, to display info about other objects and make decisions

    """
    def __init__(self, tile, menu_width = 0, menu_height = 0, menu_pos = [0,0], menu_surface = pygame.Surface((2,2)), menu_line_width = 3):
        self.tile = tile
        self.menu_width = menu_width
        self.menu_height = menu_height
        self.menu_surface = menu_surface
        self.menu_pos = menu_pos
        self.menu_line_width = menu_line_width

    def get_menu_pos(self, tile_height):
        self.menu_pos[0] = self.tile.screen_pos[0]
        self.menu_pos[1] = self.tile.screen_pos[1] - tile_height  
        
    def draw_menu(self, tile_height, screen):
        self.get_menu_pos(tile_height)
        self.surface = pygame.Surface((self.menu_width, self.menu_height))
        pygame.draw.rect(self.surface, menu_YELLOW, [0, 0, self.menu_width, self.menu_height]) #[x,y,width height]
        pointlist = [[0 ,0], [self.menu_width, 0], [self.menu_width, self.menu_height], [0, self.menu_height], [0, 0]]
        pygame.draw.lines(self.surface, BLACK, False, pointlist, self.menu_line_width)
        screen.blit(self.surface, self.menu_pos)
       
class tile_menu(menu):
    """
    
    child class for menus specific to showing tile info and making tile related decisions
    
    """
    
    def __init__(self, tile, menu_width = 0, menu_height = 0):
        menu.__init__(self, tile, menu_width, menu_height)
        
        

