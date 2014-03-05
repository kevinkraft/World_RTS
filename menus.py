import sys
import pygame
from pygame.locals import *

OLIVE = (107, 142, 35)
BLACK = (0, 0, 0)
BLUE = (0, 0, 205)
GREY = (105, 105, 105)
BROWN = (139, 69, 19)
menu_YELLOW = (255, 255, 0)
dark_YELLOW = (204,204,0)

class menu(object):
    """

    for all menus, to display info about other objects and make decisions

    """
    def __init__(self, tile, menu_width = 0, menu_height = 0, menu_pos = [0,0], menu_surface = pygame.Surface((2,2)), menu_line_width = 10,
                 menu_multi = 0):
        #let tile know it now has a menu
        tile.has_menu = True
        self.tile = tile
        self.menu_width = menu_width
        self.menu_height = menu_height
        self.menu_surface = menu_surface
        self.menu_pos = menu_pos
        self.menu_line_width = menu_line_width

    def get_menu_pos(self, tile_width, tile_height):
        self.menu_pos[0] = self.tile.screen_pos[0] + tile_width
        self.menu_pos[1] = self.tile.screen_pos[1] + tile_height  

    def get_menu_size(self, tile_width, tile_height):
        self.menu_height = self.menu_multi*tile_height
        self.menu_width = self.menu_multi*tile_width

    def draw_menu(self, tile_height, tile_width, screen):
        self.get_menu_pos(tile_height, tile_width)
        self.surface = pygame.Surface((self.menu_width, self.menu_height))
        self.get_menu_size(tile_width, tile_height)
        pygame.draw.rect(self.surface, menu_YELLOW, [0, 0, self.menu_width, self.menu_height]) #[x,y,width height]
        pointlist = [[0 ,0], [self.menu_width, 0], [self.menu_width, self.menu_height], [0, self.menu_height], [0, 0]]
        pygame.draw.lines(self.surface, dark_YELLOW, False, pointlist, self.menu_line_width)
        screen.blit(self.surface, self.menu_pos)
       
class tile_menu(menu):
    """
    
    child class for menus specific to showing tile info and making tile related decisions
    
    """
    
    def __init__(self, tile, menu_width = 0, menu_height = 0, menu_multi = 7):
        menu.__init__(self, tile)
        self.menu_multi = menu_multi #assigns the value given in def __init__ of tile_menu  
        
        

