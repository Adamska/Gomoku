#!/usr/bin/env python2.7

import pygame, os
import menu


if __name__ == '__main__':
    
    # Pygame initialisation, center the window
    pygame.init()
    os.environ['SDL_VIDEO_CENTERED'] = '1'
 
    # Create Menu and launch it
    Menu = menu.Menu()
    Menu.draw_menu() 
     
    

