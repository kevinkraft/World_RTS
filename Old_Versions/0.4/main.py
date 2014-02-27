#World_RTS
#Version: 0.4
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
#  Zoom and scroll
#    start with making new bigger map size, 30x30 (done)
#    make tiles per side a variable of zoom (done)
#    use top left corner of screen and tiles per side as the two zoom variables
#      The screen_pos atribute of a tile will be reassigned for tiles which will apear on screen, and called to print that tile to the screen.        the screen_pos atribute for those tiles not on the screen will not be reassigned after zoom but will not be called(done)
#    Need to change the value of tile width and height in some function(done)
#    reassign tile.screen_pos in main event loop, or maybe in zoom function(done)
#    The tile highlight loop uses tile.surface so we need to remake the surfaces before we get to tile highlight(done)
#      To solve this we can redraw the tiles without a highlight in the zoom function before tile highlight loop(done)
#    write function that makes a zoom_tile_list of those tiles to be displayed on screen(done)
#    then scroll will be the reassignment of zoom_top_left_corner
#  on screen time(done)
#  add tool bars to bottom and top
#
#Problems:
#  in the_map.py coord is not the (i,j)th coord of coord_trans so program fails when we try to get zoom_tile_list when topleft_grid doesn't equ   al [0, 0] (fixed)
#  Scroll is messed up. when you move one way it doesn't print the tiles which are not printed in the original zoom, seems to move diagonaly in   stead of up down left right. BIG PROBLEMS. 
import sys
import pygame
from pygame.locals import *
import the_map

"""

game parameters

"""
toolbar_height = 40
screen_width = 480 
screen_height = 480
screen_height_toolbar = 480 + 2*toolbar_height
tiles_per_side_GLOBAL = 30#10
OLIVE = (107, 142, 35)
BLACK = (0, 0, 0)
BLUE = (0, 0, 205)
GREY = (105, 105, 105)
HIGHLIGHT_BLUE = (0, 191, 255)
BROWN = (139, 69, 19)
WHITE = (255, 255, 255)
line_width = 3
big_map = [[2, 2, 1, 1, 1, 1, 1, 1, 0, 0, 2, 2, 1, 1, 1, 1, 1, 1, 0, 0, 2, 2, 1, 1, 1, 1, 1, 1, 0, 0],
           [2, 2, 1, 1, 1, 1, 1, 1, 0, 0, 2, 2, 1, 1, 1, 1, 1, 1, 0, 0, 2, 2, 1, 0, 0, 0, 1, 1, 0, 0],
           [2, 2, 1, 1, 0, 1, 1, 1, 0, 0, 2, 2, 1, 0, 0, 0, 1, 1, 0, 0, 2, 2, 1, 1, 1, 0, 1, 1, 0, 0],
           [2, 2, 1, 1, 0, 1, 1, 1, 0, 0, 2, 2, 1, 1, 1, 0, 1, 1, 0, 0, 2, 2, 1, 0, 0, 0, 1, 1, 0, 0],
           [2, 2, 1, 1, 0, 1, 1, 1, 0, 0, 2, 2, 1, 0, 0, 0, 1, 1, 0, 0, 2, 2, 1, 1, 1, 0, 1, 1, 0, 0],
           [2, 2, 1, 1, 1, 1, 1, 1, 0, 0, 2, 2, 1, 0, 1, 1, 1, 1, 0, 0, 2, 2, 1, 0, 0, 0, 1, 1, 0, 0],
           [2, 2, 1, 1, 1, 1, 1, 1, 0, 0, 2, 2, 1, 0, 0, 0, 1, 1, 0, 0, 2, 2, 1, 1, 1, 1, 1, 1, 0, 0],
           [2, 2, 1, 1, 1, 1, 1, 1, 0, 0, 2, 2, 1, 1, 1, 1, 1, 1, 0, 0, 2, 2, 1, 1, 1, 1, 1, 1, 0, 0],
           [2, 2, 1, 1, 1, 1, 1, 1, 0, 0, 2, 2, 1, 1, 1, 1, 1, 1, 0, 0, 2, 2, 1, 1, 1, 1, 1, 1, 0, 0],
           [2, 2, 1, 1, 1, 1, 1, 1, 0, 0, 2, 2, 1, 1, 1, 1, 1, 1, 0, 0, 2, 2, 1, 1, 1, 1, 1, 1, 0, 0],
           [2, 2, 1, 0, 1, 0, 1, 1, 0, 0, 2, 2, 1, 1, 1, 1, 1, 1, 0, 0, 2, 2, 1, 1, 1, 1, 1, 1, 0, 0],
           [2, 2, 1, 0, 1, 0, 1, 1, 0, 0, 2, 2, 1, 1, 1, 1, 1, 1, 0, 0, 2, 2, 1, 1, 1, 1, 1, 1, 0, 0],
           [2, 2, 1, 0, 0, 0, 1, 1, 0, 0, 2, 2, 1, 0, 0, 0, 1, 1, 0, 0, 2, 2, 1, 1, 1, 1, 1, 1, 0, 0],
           [2, 2, 1, 1, 1, 0, 1, 1, 0, 0, 2, 2, 1, 0, 1, 1, 1, 1, 0, 0, 2, 2, 1, 0, 1, 1, 1, 1, 0, 0],
           [2, 2, 1, 1, 1, 0, 1, 1, 0, 0, 2, 2, 1, 0, 1, 1, 1, 1, 0, 0, 2, 2, 1, 0, 1, 1, 1, 1, 0, 0],
           [2, 2, 1, 1, 1, 1, 1, 1, 0, 0, 2, 2, 1, 1, 0, 1, 1, 1, 0, 0, 2, 2, 1, 0, 0, 0, 1, 1, 0, 0],
           [2, 2, 1, 1, 1, 1, 1, 1, 0, 0, 2, 2, 1, 1, 1, 0, 1, 1, 0, 0, 2, 2, 1, 0, 1, 0, 1, 1, 0, 0],
           [2, 2, 1, 1, 1, 1, 1, 1, 0, 0, 2, 2, 1, 0, 0, 1, 1, 1, 0, 0, 2, 2, 1, 0, 0, 0, 1, 1, 0, 0],
           [2, 2, 1, 1, 1, 1, 1, 1, 0, 0, 2, 2, 1, 1, 1, 1, 1, 1, 0, 0, 2, 2, 1, 1, 1, 1, 1, 1, 0, 0],
           [2, 2, 1, 1, 1, 1, 1, 1, 0, 0, 2, 2, 1, 1, 1, 1, 1, 1, 0, 0, 2, 2, 1, 1, 1, 1, 1, 1, 0, 0],
           [2, 2, 1, 1, 1, 1, 1, 1, 0, 0, 2, 2, 1, 1, 1, 1, 1, 1, 0, 0, 2, 2, 1, 1, 1, 1, 1, 1, 0, 0],
           [2, 2, 1, 1, 1, 1, 1, 1, 0, 0, 2, 2, 1, 1, 1, 1, 1, 1, 0, 0, 2, 2, 1, 1, 1, 1, 1, 1, 0, 0],
           [2, 2, 1, 1, 1, 1, 1, 1, 0, 0, 2, 2, 1, 1, 1, 1, 1, 1, 0, 0, 2, 2, 1, 0, 0, 0, 1, 1, 0, 0],
           [2, 2, 1, 1, 1, 1, 1, 1, 0, 0, 2, 2, 1, 1, 1, 1, 1, 1, 0, 0, 2, 2, 1, 0, 1, 0, 1, 1, 0, 0],
           [2, 2, 1, 0, 0, 0, 1, 1, 0, 0, 2, 2, 1, 0, 0, 0, 1, 1, 0, 0, 2, 2, 1, 0, 0, 0, 1, 1, 0, 0],
           [2, 2, 1, 0, 1, 1, 1, 1, 0, 0, 2, 2, 1, 0, 1, 0, 1, 1, 0, 0, 2, 2, 1, 1, 1, 0, 1, 1, 0, 0],
           [2, 2, 1, 0, 1, 1, 1, 1, 0, 0, 2, 2, 1, 0, 0, 0, 1, 1, 0, 0, 2, 2, 1, 1, 1, 0, 1, 1, 0, 0],
           [2, 2, 1, 0, 1, 1, 1, 1, 0, 0, 2, 2, 1, 0, 1, 0, 1, 1, 0, 0, 2, 2, 1, 1, 1, 0, 1, 1, 0, 0],
           [2, 2, 1, 1, 1, 1, 1, 1, 0, 0, 2, 2, 1, 0, 0, 0, 1, 1, 0, 0, 2, 2, 1, 1, 1, 1, 1, 1, 0, 0],
           [2, 2, 1, 1, 1, 1, 1, 1, 0, 0, 2, 2, 1, 1, 1, 1, 1, 1, 0, 0, 2, 2, 1, 1, 1, 1, 1, 1, 0, 0]]

simple_map = [[2, 2, 1, 1, 1, 1, 1, 1, 0, 0],
              [2, 2, 1, 1, 1, 1, 1, 1, 0, 0],
              [2, 2, 1, 1, 1, 1, 1, 1, 0, 0],
              [2, 2, 1, 1, 1, 1, 1, 1, 0, 0],
              [2, 2, 1, 1, 0, 1, 1, 1, 0, 0],
              [2, 2, 1, 1, 1, 0, 1, 1, 0, 0],
              [2, 2, 1, 1, 1, 1, 1, 1, 0, 0],
              [2, 2, 1, 1, 1, 1, 1, 1, 0, 0],
              [2, 2, 1, 1, 1, 1, 1, 1, 0, 0],
              [2, 2, 1, 1, 1, 1, 1, 1, 0, 0]]
current_map = big_map

"""

initialize

"""
def main():
    tile_width = (((screen_width)/tiles_per_side_GLOBAL))
    tile_height = (((screen_height)/tiles_per_side_GLOBAL))
    tiles_per_side = tiles_per_side_GLOBAL
    
    pygame.init()
    
    screen = pygame.display.set_mode((screen_width, screen_height_toolbar))
    pygame.display.set_caption('World RTS')

    #set top corner of tile_positions with initial zoom
    zoom_top_corner = [0, 0]
    coord_trans = [] #arrary of the top left corner of screen coords of each tile in the corresponding grid coords
    for j in range(0, tiles_per_side):
        coord_trans_in = []
        for i in range(0, tiles_per_side):
            coord = [(tile_width)*(i), (tile_height)*(j) + toolbar_height]
            coord_trans_in.append(coord)
        coord_trans.append(coord_trans_in)
    
    #make tiles with initial zoom
    tile_list = []
    for j in range(0, tiles_per_side):
        tile_list_in = []
        for i in range(0, tiles_per_side):
            tile = the_map.tile(coord_trans[i][j], [i,j], current_map[i][j]) #scree_pos, gird_pos, terrain_type, (opt) surface
            tile.draw_tile(screen, tile_width, tile_height, line_width, BLACK)
            tile_list_in.append(tile)
        tile_list.append(tile_list_in)
    zoom_tile_list = tile_list
            
    #Display some text
    #font = pygame.font.Font(None, 36)
    #text = font.render("Hello There", 1, (10, 10, 10))
    #textpos = text.get_rect()
    #textpos.centerx = background.get_rect().centerx
    #background.blit(text, textpos)

    #set up zoom
    topleft_grid = [0, 0]
    font = pygame.font.Font(None, 50)
    zoom_in_text = font.render("+", 1, BLACK)
    zoom_out_text = font.render("-", 1, BLACK)
    zoom_in_textpos = zoom_in_text.get_rect()
    zoom_out_textpos = zoom_out_text.get_rect()
    zoom_in_x = screen_width - screen_width/4 + 70
    zoom_in_y = screen_height_toolbar - 2*toolbar_height/3
    zoom_out_x = screen_width - screen_width/4 + 100
    zoom_out_y = screen_height_toolbar - 2*toolbar_height/3 + 3
    zoom_in_textpos.centerx = zoom_in_x
    zoom_in_textpos.centery = zoom_in_y
    zoom_out_textpos.centerx = zoom_out_x
    zoom_out_textpos.centery = zoom_out_y
    button_width = 25 #only clicking in the center of the button makes it work
    #zoom_in_surf = pygame.Surface((button_width, button_width))
    #zoom_out_surf = pygame.Surface((button_width, button_width))
    #zoom_in_surf.get_rect(topleft = (zoom_in_x - 12, zoom_in_y - 6))
    #zoom_out_surf.get_rect(topleft = (zoom_out_x - 12, zoom_out_y - 9))

    #set up clock
    time_font = pygame.font.Font(None, 36)
    time_xpos = screen_width/15
    time_ypos = toolbar_height/2
    clock = pygame.time.Clock()
    minutes = 0
    seconds = 0
    milliseconds = 0

    pygame.display.flip()

    #Event loop
    while 1:

        #redraw tiles with highlight
        for j in range(0, len(zoom_tile_list)):
            zoom_tile_list_in = zoom_tile_list[j]
            for i in range(0, len(zoom_tile_list_in)):
                tile = zoom_tile_list_in[i]
                if tile.surface.get_rect(topleft = tile.screen_pos).collidepoint(pygame.mouse.get_pos()):
                    line_colour = HIGHLIGHT_BLUE
                    grid_line_width = 2*(line_width)
                else:
                    line_colour = BLACK
                    grid_line_width = line_width
                tile.draw_tile(screen, tile_width, tile_height, grid_line_width, line_colour)
 
        #make toolbars
        toolbar_up_rect = pygame.draw.rect(screen, BROWN, [0, 0, screen_width, toolbar_height])
        toolbar_up_rect = pygame.draw.rect(screen, BROWN, [0, screen_height + toolbar_height, screen_width, toolbar_height])
        
        #timing
        if milliseconds > 1000:
            seconds += 1
            milliseconds -= 1000
        if seconds > 60:
            minutes += 1
            seconds -= 60
        text = time_font.render(("{}:{}".format(minutes, seconds)), 1, BLACK) #text,antialiasing,colour
        textpos = text.get_rect()
        textpos.centerx = time_xpos
        textpos.centery = time_ypos
        screen.blit(text, textpos)
        milliseconds += clock.tick_busy_loop() #returns time since the last call, limits the frame rate to 60FPS

        #print zoom buttons
        pygame.draw.rect(screen, WHITE, [zoom_in_x - 12, zoom_in_y - 6, button_width, button_width])
        pygame.draw.rect(screen, WHITE, [zoom_out_x - 12, zoom_out_y - 9, button_width, button_width])
        screen.blit(zoom_in_text, zoom_in_textpos)
        screen.blit(zoom_out_text, zoom_out_textpos)

        #events
        for event in pygame.event.get():
            #quit game
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            #mouse clicks
            if event.type == pygame.MOUSEBUTTONUP:
                #zoom in
                if zoom_in_textpos.collidepoint(pygame.mouse.get_pos()):
                    tiles_per_side, zoom_tile_list, tile_width, tile_height = the_map.zoom_in(tiles_per_side,
                                                                                              tiles_per_side_GLOBAL,
                                                                                              topleft_grid,
                                                                                              tile_list,
                                                                                              screen_width,
                                                                                              screen_height, 
                                                                                              screen,
                                                                                              line_width,
                                                                                              toolbar_height)
                #zoom out
                if zoom_out_textpos.collidepoint(pygame.mouse.get_pos()):
                    tiles_per_side, zoom_tile_list, tile_width, tile_height = the_map.zoom_out(tiles_per_side,
                                                                                               tiles_per_side_GLOBAL,
                                                                                               topleft_grid,
                                                                                               tile_list,
                                                                                               screen_width,
                                                                                               screen_height,
                                                                                               screen,
                                                                                               line_width,
                                                                                               toolbar_height)

            #scroll
            if event.type == pygame.KEYDOWN:
                #up
                if event.key == pygame.K_w:
                    topleft_grid[1] = topleft_grid[1] + 1  
                #down
                if event.key == pygame.K_s:
                    topleft_grid[1] = topleft_grid[1] - 1  
                #left
                if event.key == pygame.K_a:
                    topleft_grid[0] = topleft_grid[0] + 1  
                #right
                if event.key == pygame.K_d:
                    topleft_grid[0] = topleft_grid[0] - 1  
                print topleft_grid
                
                
                #remake list with new topleft_grid and redraw
                zoom_tile_list = the_map.get_zoom_tile_list(topleft_grid,
                                                            tiles_per_side,
                                                            tile_list,
                                                            tile_width,
                                                            tile_height,
                                                            screen,
                                                            line_width,
                                                            toolbar_height)

                #################################################################
                #can do this better
                #tiles_per_side, zoom_tile_list, tile_width, tile_height = the_map.zoom_in(tiles_per_side,
                #                                                                          tiles_per_side_GLOBAL,
                #                                                                          topleft_grid,
                #                                                                          tile_list,
                #                                                                          screen_width,
                #                                                                          screen_height, 
                #                                                                          screen,
                #                                                                          line_width,
                #                                                                          toolbar_height)
                # 
                # tiles_per_side, zoom_tile_list, tile_width, tile_height = the_map.zoom_out(tiles_per_side,
                #                                                                           tiles_per_side_GLOBAL,
                #                                                                           topleft_grid,
                #                                                                           tile_list,
                #                                                                           screen_width,
                #                                                                           screen_height,
                #                                                                           screen,
                #                                                                           line_width,
                #                                                                           toolbar_height)

        pygame.display.flip()

main()

