#Test to see if you can give python screen coordinates which are negative
# Conclusion:
#  yes you can

import sys
import pygame
from pygame.locals import *
import the_map

"""

sim parameters

"""
screen_width = 480
screen_height = 480
tiles_per_side = 2
tile_width = 200
tile_height = 200

def main():
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('World RTS')
    colour = [200, 150, 200]
    pygame.draw.rect(screen, colour, [-100, -100, tile_width, tile_height]) #[x,y,width height]
    #screen.blit(surface, [200,200])

    pygame.display.update()

    #Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

main()
