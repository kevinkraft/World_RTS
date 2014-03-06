#World_RTS
#Version: 0.6
#
#Kevin Maguire
#15/12/13
#
#Add:
#  maybe add xy coords onto screen
#  Menu when tile is clicked
#  Menu which is specific to that tile. 
#  Zoom(done) and scroll(done)
#    start with making new bigger map size, 30x30 (done)
#    make tiles per side a variable of zoom (done)
#    use top left corner of screen and tiles per side as the two zoom variables (done)
#    screen_pos of all tiles are adjusted to new values of tile width and height (done)
#  Tile menus
#    might need to make tile_width and tile_height an atribute of a tile so that it can be called by menus, currently its a once off variable t     hat is the same for all tiles, as it should be (no, just used tile width and height when using draw_menus)
#    the menu will have a size based on the tile size when it was created and will change with zoom 
#    menu close button (done)
#    menu close X on the tile
#    menu darker, larger yellow border (done)
#    populate menu 
#    CURRENT SYSTEM FOR CHANING SIZE OF MENU WHEN ZOOM CHANGES DOESNT WORK AT ALL
#      far out zoom, menu too small, close in zoom menu way too big
#      why not just give them a mixed size for all time? it doesnt need to depend on the zoom, it just has to be in the right place
#
#Problem:
#  small problem with bottom toolbar disappearing for larger screen sizes(fixed)
#  still cant zoom into one tile without it being slow, disabled for now
#  menu tries to open when zoom is clicked, as there is sometimes a time surface printed behind the zoom buttons, to fix just add in boolian exception to the tile menu if statement(fixed)

import sys
import pygame
from pygame.locals import *
import the_map
import menus

"""

game parameters

"""
toolbar_height = 40#70
screen_width = 480#1300 
screen_height = 480#575
screen_height_toolbar = screen_height + 2*toolbar_height
tiles_per_side_GLOBAL = 30#10
OLIVE = (107, 142, 35)
BLACK = (0, 0, 0)
BLUE = (0, 0, 205)
GREY = (105, 105, 105)
HIGHLIGHT_BLUE = (0, 191, 255)
BROWN = (139, 69, 19)
WHITE = (255, 255, 255)
menu_YELLOW = (255, 255, 0)
line_width = 2
menu_width = 112
menu_height = 112
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
    pygame.FULLSCREEN#pygame.display.set_mode((screen_width, screen_height_toolbar))
    pygame.display.set_caption('World RTS')
    pygame.display.toggle_fullscreen

    #set top corner of tile_positions with initial zoom
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
            
    #Display some text
    #font = pygame.font.Font(None, 36)
    #text = font.render("Hello There", 1, (10, 10, 10))
    #textpos = text.get_rect()
    #textpos.centerx = background.get_rect().centerx
    #background.blit(text, textpos)

    #set up zoom
    topleft_grid_onscreen = [0, 0]
    font = pygame.font.Font(None, 50)
    zoom_in_text = font.render("+", 1, BLACK)
    zoom_out_text = font.render("-", 1, BLACK)
    zoom_in_textpos = zoom_in_text.get_rect()
    zoom_out_textpos = zoom_out_text.get_rect()
    zoom_in_x = screen_width - screen_width/4 + 70 
    zoom_in_y = screen_height_toolbar - 2*toolbar_height/3 #toolbar_height/2
    zoom_out_x = screen_width - screen_width/4 + 100
    zoom_out_y = screen_height_toolbar - 2*toolbar_height/3 + 3 #toolbar_height/2
    zoom_in_textpos.centerx = zoom_in_x
    zoom_in_textpos.centery = zoom_in_y
    zoom_out_textpos.centerx = zoom_out_x
    zoom_out_textpos.centery = zoom_out_y
    button_width = 25 #only clicking in the center of the button makes it work

    #set up menus
    menu_list = []

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

        screen.fill(BROWN)

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

        #draw menus
        for menu in menu_list:
            menu.draw_menu(tile_height, tile_width, screen)
            #redraw tiles with associated menus with a thicker yellow border
            menu.tile.draw_tile(screen, tile_width, tile_height, (7/2)*(line_width), menu_YELLOW)

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

                #close menu if tile is clicked again
                deleted_menu = False
                for menu in menu_list:
                    if menu.tile.surface.get_rect(topleft = menu.tile.screen_pos).collidepoint(pygame.mouse.get_pos()):
                        menu.tile.has_menu = False
                        menu_list.remove(menu)
                        deleted_menu = True #so it doesnt create the menu again as soon as its been made

                #make tile menu if tile clicked
                for j in range(0, len(tile_list)):
                    tile_list_in = tile_list[j]
                    for i in range(0, len(tile_list_in)):
                        tile = tile_list_in[i]
                        if (
                            tile.surface.get_rect(topleft = tile.screen_pos).collidepoint(pygame.mouse.get_pos()) and
                            zoom_in_textpos.collidepoint(pygame.mouse.get_pos()) == 0 and
                            zoom_out_textpos.collidepoint(pygame.mouse.get_pos()) == 0 and
                            tile.has_menu == False and
                            deleted_menu == False
                            ):
                            menu = menus.tile_menu(tile, menu_width, menu_height)
                            menu_list.append(menu)
                    
                #zoom in
                if zoom_in_textpos.collidepoint(pygame.mouse.get_pos()):
                    print ("ZOOM IN")
                    tile_width, tile_height, tiles_per_side  = the_map.zoom_in(tiles_per_side, screen_width, screen_height,
                                                                               tiles_per_side_GLOBAL, topleft_grid_onscreen,
                                                                               toolbar_height, tile_list, screen, line_width)

                #zoom out
                if zoom_out_textpos.collidepoint(pygame.mouse.get_pos()):
                    print ("ZOOM OUT")
                    tile_width, tile_height, tiles_per_side = the_map.zoom_out(tiles_per_side, screen_width, screen_height,
                                                                               tiles_per_side_GLOBAL, topleft_grid_onscreen,
                                                                               toolbar_height, tile_list, screen, line_width)

            #scroll
            if event.type == pygame.KEYDOWN:
                #up
                if event.key == pygame.K_w:
                    topleft_grid_onscreen[1] = topleft_grid_onscreen[1] - 1  
                #down
                if event.key == pygame.K_s:
                    topleft_grid_onscreen[1] = topleft_grid_onscreen[1] + 1  
                #left
                if event.key == pygame.K_a:
                    topleft_grid_onscreen[0] = topleft_grid_onscreen[0] - 1  
                #right
                if event.key == pygame.K_d:
                    topleft_grid_onscreen[0] = topleft_grid_onscreen[0] + 1  
                the_map.get_new_tile_list(tiles_per_side_GLOBAL, topleft_grid_onscreen, tile_width, tile_height, toolbar_height,
                                          tile_list, screen, line_width, tiles_per_side)


        pygame.display.flip()

main()

