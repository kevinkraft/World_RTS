import sys
import pygame
from pygame.locals import *

"""

All game spries

"""

OLIVE = (107, 142, 35)
BLACK = (0, 0, 0)
BLUE = (0, 0, 205)
GREY = (105, 105, 105)
BROWN = (139, 69, 19)
menu_YELLOW = (255, 255, 0)
dark_YELLOW = (204,204,0)

class sprite(object):
    """

    for all sprites

    """
    def __init__(self, pos, sprite_type, sprite_tile, HP = 0, img = pygame.image.load('Images/Sprites/villager.png'),
                 img_surface = pygame.Surface((2,2))):        
        self.pos = pos
        self.sprite_type = sprite_type
        self.HP = HP
        self.set_parameters(1)
        self.img = img
        self.sprite_tile = sprite_tile
        
    def set_parameters(self, sprite_type):
        #villager
        if sprite_type == 1:
            self.HP = 100
            self.img = pygame.image.load('Images/Sprites/villager.png')
            self.img 

    def draw_sprite(self):
        self.sprite_tile.surface.blit(self.img, (0,0))
        
