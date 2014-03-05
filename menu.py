#!/usr/bin/env python2.7

import pygame
from pygame import QUIT, KEYDOWN, K_UP, K_ESCAPE, K_DOWN, K_RETURN, K_LEFT, K_RIGHT, DOUBLEBUF, K_TAB
import sys
import game

class Menu:

    def __init__(self):

        screen = pygame.display.set_mode((1280, 1024), DOUBLEBUF, 32)
        # Load pictures for the Menu 
        try:
            self.main_bg = pygame.image.load("img/Menu/main_background.png").convert()
            self.play = pygame.image.load("img/Menu/play.png").convert_alpha() 
            self.settings = pygame.image.load("img/Menu/settings.png").convert_alpha()
            self.quit = pygame.image.load("img/Menu/quit.png").convert_alpha()

            self.settings_bg = pygame.image.load("img/Menu/settings_background.png").convert()

            self.map_size = pygame.image.load("img/Menu/map_size.png").convert_alpha()
            self.up = pygame.image.load("img/Menu/up.png").convert_alpha()
            self.up_s = pygame.image.load("img/Menu/up_s.png").convert_alpha()
            self.down = pygame.image.load("img/Menu/down.png").convert_alpha()
            self.down_s = pygame.image.load("img/Menu/down_s.png").convert_alpha()
            self.rules = pygame.image.load("img/Menu/rules.png").convert_alpha()
            self.mode = pygame.image.load("img/Menu/mode.png").convert_alpha()
            self.double_3 = pygame.image.load("img/Menu/double three.png").convert_alpha()
            self.five_brk = pygame.image.load("img/Menu/five breakable.png").convert_alpha()
            self.capture = pygame.image.load("img/Menu/capture.png").convert_alpha()
            self.vs_ai = pygame.image.load("img/Menu/versus_AI.png").convert_alpha()
            self.two_players = pygame.image.load("img/Menu/2_players.png").convert_alpha()
            self.save = pygame.image.load("img/Menu/save.png").convert_alpha()
            self.go_back = pygame.image.load("img/Menu/go_back.png").convert_alpha()
            
            self.nb = []
            self.nb.append(pygame.image.load("img/Menu/zero.png").convert_alpha())
            self.nb.append(pygame.image.load("img/Menu/one.png").convert_alpha())
            self.nb.append(pygame.image.load("img/Menu/two.png").convert_alpha())
            self.nb.append(pygame.image.load("img/Menu/three.png").convert_alpha())
            self.nb.append(pygame.image.load("img/Menu/four.png").convert_alpha())
            self.nb.append(pygame.image.load("img/Menu/five.png").convert_alpha())
            self.nb.append(pygame.image.load("img/Menu/six.png").convert_alpha())
            self.nb.append(pygame.image.load("img/Menu/seven.png").convert_alpha())
            self.nb.append(pygame.image.load("img/Menu/eight.png").convert_alpha())
            self.nb.append(pygame.image.load("img/Menu/nine.png").convert_alpha())
            
            self.nb_s = []
            self.nb_s.append(pygame.image.load("img/Menu/zero_s.png").convert_alpha())
            self.nb_s.append(pygame.image.load("img/Menu/one_s.png").convert_alpha())
            self.nb_s.append(pygame.image.load("img/Menu/two_s.png").convert_alpha())
            self.nb_s.append(pygame.image.load("img/Menu/three_s.png").convert_alpha())
            self.nb_s.append(pygame.image.load("img/Menu/four_s.png").convert_alpha())
            self.nb_s.append(pygame.image.load("img/Menu/five_s.png").convert_alpha())
            self.nb_s.append(pygame.image.load("img/Menu/six_s.png").convert_alpha())
            self.nb_s.append(pygame.image.load("img/Menu/seven_s.png").convert_alpha())
            self.nb_s.append(pygame.image.load("img/Menu/eight_s.png").convert_alpha())
            self.nb_s.append(pygame.image.load("img/Menu/nine_s.png").convert_alpha())

            self.tick = pygame.image.load("img/Menu/tick.png").convert_alpha()
        except pygame.error(), message:
            raise SystemExit, message
        
        # Create Game instance
        self.Game = game.Game()

    # Display an int with pictures loaded
    def display_nbr(self, screen, nbr):
        tmp = self.Game.size
        list = []
        while tmp != 0:
            list.insert(0, tmp % 10)
            tmp /= 10
        
        i = 0
        if nbr == 0:
            for n in list:
                screen.blit(self.nb[n], (800 + (i * self.nb[0].get_size()[0]), 400))
                i += 1
        else:
            for n in list:
                screen.blit(self.nb_s[n], (800 + (i * self.nb[0].get_size()[0]), 400))
                i += 1

    def save_option(self):
        try:
            with open('config', 'w+') as file:
                file.write('####################################################\n' +
                           '#                                                  #\n' +
                           '#  Configuration file for the parameters of gomoku #\n' +
                           '#                                                  #\n' +
                           '####################################################\n\n' +

                           '####################################################\n' +
                           '# First parameter : rule Double Three              #\n' +
                           '# 0 : rule desactivated                            #\n' +
                           '# 1 : rule activated                               #\n' +
                           '####################################################\n')
                file.write(str(self.Game.rule_2b3))

                file.write('\n\n####################################################\n' +
                               '# Second parameter : rule Five Breakable           #\n' +
                               '# 0 : rule desactivated                            #\n' +
                               '# 1 : rule activated                               #\n' +
                               '####################################################\n')
                file.write(str(self.Game.rule_5brk))
                
                file.write('\n\n####################################################\n' +
                               '# Third parameter : rule Capture                   #\n' +
                               '# 0 : rule desactivated                            #\n' +
                               '# 1 : rule activated                               #\n' +
                               '####################################################\n')
                file.write(str(self.Game.rule_capt))
                
                file.write('\n\n####################################################\n' +
                               '# Fourth parameter : Game Mode                     #\n' +
                               '# 0 : 2 Player Mode                                #\n' +
                               '# 1 : Player versus IA Mode                        #\n' +
                               '####################################################\n')
                file.write(str(self.Game.IA))
                
                file.write('\n\n####################################################\n' +
                               '# Fifth parameter : Map Size                       #\n' +
                               '# minimum : 12                                     #\n' +
                               '# maximum : 50                                     #\n' +
                                '####################################################\n')
                file.write(str(self.Game.size))
                
                file.write('\n\n####################################################\n' +
                               '# sixth parameter : Select Mode (Menu)             #\n' +
                               '# 0 : keyboard                                     #\n' +
                               '# 1 : mouse                                        #\n' +
                               '# 2 : both                                         #\n' +
                               '####################################################\n')
                file.write(str(self.Game.select))

                file.write('\n\n####################################################\n' +
                               '# seventh parameter : Map Skin                     #\n' +
                               '# 0 : skin 1                                       #\n' +
                               '# 1 : skin 2                                       #\n' +
                               '# 2 : skin 3                                       #\n' +
                               '####################################################\n')
                file.write(str(self.Game.skins))

                file.write('\n\n####################################################\n' +
                               '# eighth parameter : Red Token Skin                #\n' +
                               '# 0 : skin 1                                       #\n' +
                               '# 1 : skin 2                                       #\n' +
                               '# 2 : skin 3                                       #\n' +
                               '####################################################\n')
                file.write(str(self.Game.skinr))

                file.write('\n\n####################################################\n' +
                               '# eighth parameter : Blue Token Skin               #\n' +
                               '# 0 : skin 1                                       #\n' +
                               '# 1 : skin 2                                       #\n' +
                               '# 2 : skin 3                                       #\n' +
                               '####################################################\n')
                file.write(str(self.Game.skinb))

                file.write('\n\n####################################################\n' +
                               '# ninth parameter : Display current position       #\n' +
                               '# 0 : no                                           #\n' +
                               '# 1 : yes                                          #\n' +
                               '####################################################\n')
                file.write(str(self.Game.actual))

        except:
            return
 
    # Move along the menu and do actions in function of the mouse click and the mouse position
    def check_case_mouse(self, mouse):
        
        # Music management
        if mouse[0] in range(5, 5 + self.Game.arrow_left_on.get_size()[0])\
        and mouse[1] in range(18, 18 + self.Game.arrow_left_on.get_size()[1])\
        and self.Game.sound_play == 1:
            pygame.mixer.music.stop()
            if self.Game.cur_music == 0:
                 self.Game.cur_music = len(self.Game.titles) - 1
            else:
                self.Game.cur_music -= 1
            self.Game.put_music()

        if mouse[0] in range(10 + self.Game.arrow_left_on.get_size()[0], 10 +\
                self.Game.arrow_left_on.get_size()[0] + self.Game.sound_on.get_size()[0])\
        and mouse[1] in range(5, 5 + self.Game.sound_on.get_size()[1]):
            self.Game.sound_play = 1 - self.Game.sound_play
            if self.Game.sound_play == 0:
                pygame.mixer.music.pause()
            else: 
                pygame.mixer.music.unpause()
        
        if mouse[0] in range(15 + self.Game.arrow_left_on.get_size()[0] +\
                self.Game.sound_on.get_size()[0], 15 +\
                self.Game.sound_on.get_size()[0] + self.Game.sound_on.get_size()[0] +\
                self.Game.arrow_right_on.get_size()[0])\
        and mouse[1] in range(18, 18 + self.Game.arrow_right_on.get_size()[1])\
        and self.Game.sound_play == 1:
            pygame.mixer.music.stop()
            if self.Game.cur_music == len(self.Game.titles) - 1:
                self.Game.cur_music = 0
            else:
                self.Game.cur_music += 1
            self.Game.put_music()

        # Main menu
        if self.menu == 0:
            # Play
            if mouse[0] in range(403, 403 + self.play.get_size()[0])\
            and mouse[1] in range(378, 378 + self.play.get_size()[1]):
                self.Game.launch_game(self.Game.size, self.Game.size)
                screen = pygame.display.set_mode((1280, 1024), DOUBLEBUF, 32)
            
            # Settings
            elif mouse[0] in range(376, 376 + self.settings.get_size()[0])\
            and mouse[1] in range(645, 645 + self.settings.get_size()[1]):
                self.menu = 1
                self.pos = 0

            # Quit
            elif mouse[0] in range(985, 985 + self.quit.get_size()[0])\
            and mouse[1] in range(890, 890 + self.quit.get_size()[1]):
                sys.exit()
        

        # Settings menu        
        else:
            # Map size options
            if mouse[0] in range(129, 129 + self.map_size.get_size()[0])\
            and mouse[1] in range(381, 381 + self.map_size.get_size()[1]):
                self.Game.size = 19

            # Down the map size
            if mouse[0] in range(700, 700 + self.down.get_size()[0])\
            and mouse[1] in range(415, 415 + self.down.get_size()[1]):
                if self.Game.size > 12:
                    self.Game.size -= 1
            # Up the map size
            if mouse[0] in range(991, 991 + self.up.get_size()[0])\
            and mouse[1] in range(406, 406 + self.up.get_size()[1]):
                if self.Game.size < 50:
                    self.Game.size += 1

            # Rules options
            elif mouse[0] in range(128, 128 + self.rules.get_size()[0])\
            and mouse[1] in range(537, 537 + self.rules.get_size()[1]):
                if self.Game.rule_2b3 == 1 and self.Game.rule_5brk == 1\
                and self.Game.rule_capt == 1:
                     self.Game.rule_2b3 = 0
                     self.Game.rule_5brk = 0
                     self.Game.rule_capt = 0
                else:
                    self.Game.rule_2b3 = 1
                    self.Game.rule_5brk = 1
                    self.Game.rule_capt = 1
               
            # Double Three
            elif mouse[0] in range(516, 792 + self.tick.get_size()[0] + 10)\
            and mouse[1] in range(582, 582 + self.double_3.get_size()[1]):
                self.Game.rule_2b3 = 1 - self.Game.rule_2b3
            # Five Breakable
            elif mouse[0] in range(877, 1192 + self.tick.get_size()[0] + 10)\
            and mouse[1] in range(579, 579 + self.five_brk.get_size()[1]):
                self.Game.rule_5brk = 1 - self.Game.rule_5brk
            # Capture
            elif mouse[0] in range(516, 792 + self.tick.get_size()[0] + 10)\
            and mouse[1] in range(644, 644 + self.capture.get_size()[1]):
                self.Game.rule_capt = 1 - self.Game.rule_capt

            # Game mode options
            elif mouse[0] in range(129, 129 + self.mode.get_size()[0])\
            and mouse[1] in range(705, 705 + self.mode.get_size()[1]):
                self.Game.IA = 1 - self.Game.IA
            # Versus AI
            elif mouse[0] in range(551, 792 + self.tick.get_size()[0] + 10)\
            and mouse[1] in range(755, 755 + self.vs_ai.get_size()[1]):
                self.Game.IA = 1
            # Two Players
            elif mouse[0] in range(971, 1192 + self.tick.get_size()[0] + 10)\
            and mouse[1] in range(743, 743 + self.two_players.get_size()[1]):
                self.Game.IA = 0

            # Save button
            elif mouse[0] in range(659, 659 + self.save.get_size()[0] + 10)\
            and mouse[1] in range(921, 921 + self.save.get_size()[1]):
                self.save_option()

            # Go back button
            elif mouse[0] in range(959, 959 + self.go_back.get_size()[0] + 10)\
            and mouse[1] in range(908, 908 + self.go_back.get_size()[1]):
                self.menu = 0
                self.hori = 0 
                self.pos = 0

    # Move along the menu and do actions for some key pressed
    def check_key(self, key):
        if key == K_ESCAPE:
            sys.exit()
        elif key == K_RETURN:
            if self.menu == 0:
                if self.pos == 0:
                    self.Game.launch_game(self.Game.size, self.Game.size)
                    screen = pygame.display.set_mode((1280, 1024), DOUBLEBUF, 32)
                elif self.pos == 1:
                    self.menu = 1
                    self.pos = 0
                else: sys.exit()
            else:
                if self.pos == 1:
                    if self.hori == 0:
                        self.Game.rule_2b3 = 1 - self.Game.rule_2b3
                    elif self.hori == 1:
                        self.Game.rule_5brk = 1 - self.Game.rule_5brk
                    else:
                        self.Game.rule_capt = 1 - self.Game.rule_capt
                elif self.pos == 2:
                    if self.hori == 0:
                        self.Game.IA = 1
                    else:
                        self.Game.IA = 0
                elif self.pos == 3:
                    if self.hori == 0:
                        self.save_option()
                    else:
                        self.menu = 0
                        self.hori = 0 
                        self.pos = 0
        elif key == K_UP:
            if self.pos > 0:
                self.pos -= 1
                self.hori = 0
        elif key == K_DOWN:
            if self.pos < 2 + self.menu:
                self.pos += 1
                self.hori = 0
        elif key == K_LEFT:
            if self.menu == 1 and self.pos in (1, 2, 3) and self.hori > 0:
                self.hori -= 1
            elif self.menu == 1 and self.pos == 0 and self.Game.size > 12:
                self.Game.size -= 1
        elif key == K_RIGHT:
            if self.menu == 1 and ((self.pos in (1, 2) and self.hori < 2)
            or (self.pos == 3 and self.hori < 1)):
                self.hori += 1
            elif self.menu == 1 and self.pos == 0 and self.Game.size < 50:
                self.Game.size += 1
        # Music management 
        elif key == pygame.K_s:
            self.Game.sound_play = 1 - self.Game.sound_play
            if self.Game.sound_play == 0:
                pygame.mixer.music.pause()
            else: 
                pygame.mixer.music.unpause()
        elif key == pygame.K_d and self.Game.sound_play == 1:
            pygame.mixer.music.stop()
            if self.Game.cur_music == len(self.Game.titles) - 1:
                self.Game.cur_music = 0
            else:
                self.Game.cur_music += 1
            self.Game.put_music(1)
        elif key == pygame.K_q and self.Game.sound_play == 1:
            pygame.mixer.music.stop()
            if self.Game.cur_music == 0:
                 self.Game.cur_music = len(self.Game.titles) - 1
            else:
                self.Game.cur_music -= 1
            self.Game.put_music(1)


    # Display the menu according to the the menu and the position where we are                
    def draw_everything(self, screen):
        
        if self.menu == 0:
            screen.blit(self.main_bg, self.main_bg.get_rect())
        else:
            screen.blit(self.settings_bg, self.settings_bg.get_rect())
       
        mouse = pygame.mouse.get_pos()

        # For keyboard use 
        if self.Game.select in (0, 2): 
            # Main menu
            if self.menu == 0:
                # Play Button
                if self.pos == 0:
                    screen.blit(self.play, (403, 378))
                # Settings Button
                elif self.pos == 1:
                    screen.blit(self.settings, (376, 645))
                # Quit
                elif self.pos >= 2:
                    screen.blit(self.quit, (985, 890))

            # Settings menu        
            else:
                # Map size options
                self.display_nbr(screen, 0)
                if self.pos == 0:
                    screen.blit(self.map_size, (129, 381))
                    self.display_nbr(screen, 1)

                # Rules options
                elif self.pos == 1:
                    screen.blit(self.rules, (128, 537))
                    if self.hori == 0:
                        screen.blit(self.double_3, (516, 582))
                    elif self.hori == 1:
                        screen.blit(self.five_brk, (877, 579))
                    else:
                        screen.blit(self.capture, (516, 644))

                # Game mode options
                elif self.pos == 2:
                    screen.blit(self.mode, (129, 705))
                    if self.hori == 0:
                        screen.blit(self.vs_ai, (551, 755))
                    else:
                        screen.blit(self.two_players, (971, 743))
               
               # Go back and Save button
                elif self.pos == 3:
                    # Save button
                    if self.hori == 0:
                        screen.blit(self.save, (659, 921))
                    # Go back button
                    else:
                        screen.blit(self.go_back, (959, 908))
       
        # For mouse use
        if self.Game.select in (1, 2): 
            # Main menu
            if self.menu == 0:
                # Play Button
                if mouse[0] in range(403, 403 + self.play.get_size()[0])\
                and mouse[1] in range(378, 378 + self.play.get_size()[1]):
                    screen.blit(self.play, (403, 378))
                # Settings Button
                elif mouse[0] in range(376, 376 + self.settings.get_size()[0])\
                and mouse[1] in range(645, 645 + self.settings.get_size()[1]):
                    screen.blit(self.settings, (376, 645))
                # Quit
                elif mouse[0] in range(985, 985 + self.quit.get_size()[0])\
                and mouse[1] in range(890, 890 + self.quit.get_size()[1]):
                    screen.blit(self.quit, (985, 890))

            # Settings menu        
            else:
                # Map size options

                # up and down arrows
                screen.blit(self.down, (700, 415))
                screen.blit(self.up, (1000, 415))

                # Numbers (size
                self.display_nbr(screen, 0)

                # Map size title
                if mouse[0] in range(129, 129 + self.map_size.get_size()[0])\
                and mouse[1] in range(381, 381 + self.map_size.get_size()[1]):
                    self.display_nbr(screen, 1)
                    screen.blit(self.map_size, (129, 381))
                 
                # Down arrow selected
                if mouse[0] in range(700, 700 + self.down.get_size()[0])\
                and mouse[1] in range(415, 415 + self.down.get_size()[1]):
                    screen.blit(self.down_s, (692, 406))
                    self.display_nbr(screen, 1)

                # Up arrow selected
                if mouse[0] in range(991, 991 + self.up.get_size()[0])\
                and mouse[1] in range(406, 406 + self.up.get_size()[1]):
                    screen.blit(self.up_s, (991, 406))
                    self.display_nbr(screen, 1)

                # Rules options
                elif mouse[0] in range(128, 128 + self.rules.get_size()[0])\
                and mouse[1] in range(537, 537 + self.rules.get_size()[1]):
                    screen.blit(self.rules, (128, 537))
                # Double Three
                elif mouse[0] in range(516, 792 + self.tick.get_size()[0] + 10)\
                and mouse[1] in range(582, 582 + self.double_3.get_size()[1]):
                    screen.blit(self.double_3, (516, 582))
                    screen.blit(self.rules, (128, 537))
                # Five Breakable
                elif mouse[0] in range(877, 1192 + self.tick.get_size()[0] + 10)\
                and mouse[1] in range(579, 579 + self.five_brk.get_size()[1]):
                    screen.blit(self.five_brk, (877, 579))
                    screen.blit(self.rules, (128, 537))
                # Capture
                elif mouse[0] in range(516, 792 + self.tick.get_size()[0] + 10)\
                and mouse[1] in range(644, 644 + self.capture.get_size()[1]):
                    screen.blit(self.capture, (516, 644))
                    screen.blit(self.rules, (128, 537))

                # Game mode options
                elif mouse[0] in range(129, 129 + self.mode.get_size()[0])\
                and mouse[1] in range(705, 705 + self.mode.get_size()[1]):
                    screen.blit(self.mode, (129, 705))
                # versus AI
                elif mouse[0] in range(551, 792 + self.tick.get_size()[0] + 10)\
                and mouse[1] in range(755, 755 + self.vs_ai.get_size()[1]):
                    screen.blit(self.vs_ai, (551, 755))
                    screen.blit(self.mode, (129, 705))
                # Two Players
                elif mouse[0] in range(971, 1192 + self.tick.get_size()[0] + 10)\
                and mouse[1] in range(743, 743 + self.two_players.get_size()[1]):
                    screen.blit(self.two_players, (971, 743))
                    screen.blit(self.mode, (129, 705))
 
                # Save button
                elif mouse[0] in range(659, 659 + self.save.get_size()[0] + 10)\
                and mouse[1] in range(921, 921 + self.save.get_size()[1]):
                    screen.blit(self.save, (659, 921))

                # Go back button
                elif mouse[0] in range(959, 959 + self.go_back.get_size()[0] + 10)\
                and mouse[1] in range(908, 908 + self.go_back.get_size()[1]):
                    screen.blit(self.go_back, (959, 908))

        if self.menu == 1:
            # Display or not the ticks in boxes according to the associated variable
            if self.Game.rule_2b3 == 1:
                screen.blit(self.tick, (792, 607))
            if self.Game.rule_5brk == 1:
                screen.blit(self.tick, (1192, 607))
            if self.Game.rule_capt == 1:
                screen.blit(self.tick, (792, 663))
            if self.Game.IA == 1:
                screen.blit(self.tick, (792, 773))
            else:
                screen.blit(self.tick, (1192, 773))
        if self.Game.sound_play == 1:
            screen.blit(self.Game.arrow_left_on, (5, 18))
            screen.blit(self.Game.sound_on, (self.Game.arrow_left_on.get_size()[0] + 10, 5))
            screen.blit(self.Game.arrow_right_on, (self.Game.arrow_right_on.get_size()[0] +
                self.Game.sound_on.get_size()[0] + 15, 18))
        else:
            screen.blit(self.Game.arrow_left_off, (5, 18))
            screen.blit(self.Game.sound_off, (self.Game.arrow_left_on.get_size()[0] + 10, 5))
            screen.blit(self.Game.arrow_right_off, (self.Game.arrow_right_on.get_size()[0] +
                self.Game.sound_on.get_size()[0] + 15, 18))

        x = self.Game.arrow_left_on.get_size()[0] + self.Game.arrow_right_on.get_size()[0]\
            + self.Game.sound_on.get_size()[0] + 20
        my_font = pygame.font.SysFont("kinari", 20)
        name = self.Game.titles[self.Game.cur_music]
        if self.menu == 0 and len(name) > 130:
            name, x = self.Game.find_x(x, 130, name, my_font)
        elif self.menu == 1 and len(name) > 100:
            name, x = self.Game.find_x(x, 100, name, my_font)
        label = my_font.render(name, 1, (255, 200, 200))
        screen.blit(label, (x, 22))


    # Display and manage the menu
    def draw_menu(self):
        screen = pygame.display.set_mode((1280, 1024), DOUBLEBUF, 32)

        self.menu = 0       # menu  0 : Main menu ; 1 : Settings menu
        self.pos = 0        # position (line) where we are in the menu
        self.hori = 0       # column where we are in the position
        # Menu loop
        while 1:
            self.Game.put_music()
            # Event management : move and select options in the menu
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_TAB:
                        if self.Game.select == 2:
                            self.Game.select = 0
                        else:
                            self.Game.select += 1
                    elif self.Game.select in (0, 2):
                        self.check_key(event.key)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and self.Game.select in (1, 2): 
                        self.check_case_mouse(event.pos)

            # Display the menu according to the the menu and the position where we are                
            self.draw_everything(screen)
            pygame.display.flip()
