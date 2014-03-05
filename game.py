#!/usr/bin/env python2.7

import random
import sys, pygame, os
import Referee
import Displayer
import case
import Minmax
import copy

class Game:

    def __init__(self):
        # Load img, we need it here for size of img
        try:
            self.twob3_icon = pygame.image.load("img/2b3.png").convert()
            self.square = pygame.image.load("img/square3.png")    # one case
            self.square2 = pygame.image.load("img/square.png")    # one case
            self.square3 = pygame.image.load("img/square2.png")    # one case
            self.tr = pygame.image.load("img/red.png") 	        # Player 1 skin 1
            self.rt = pygame.image.load("img/red_t.png") 	# Player 1 transparency skin 1
            self.tb = pygame.image.load("img/blue.png")	        # Player 2 skin 1
            self.bt = pygame.image.load("img/blue_t.png")	# Player 2 transparency skin 1
            self.tr2 = pygame.image.load("img/red2.png") 	# Player 1 skin 2
            self.rt2 = pygame.image.load("img/red2_t.png") 	# Player 1 transparency skin 2
            self.tb2 = pygame.image.load("img/blue2.png")	# Player 2 skin 2
            self.bt2 = pygame.image.load("img/blue2_t.png")	# Player 2 transparency skin 2
            self.tr3 = pygame.image.load("img/red3.png")        # Player 1 skin 3
            self.rt3 = pygame.image.load("img/red3_t.png") 	# Player 1 transparency skin 3
            self.tb3 = pygame.image.load("img/blue3.png")       # Player 2 skin 3
            self.bt3 = pygame.image.load("img/blue3_t.png")	# Player 2 transparency skin 3
            self.md = pygame.image.load("img/gomoku_menu_down.png").convert_alpha() # Menu down
            self.mu = pygame.image.load("img/gomoku_menu_up.png") # Menu up
            self.w1 = pygame.image.load("img/samourai-player1.png").convert() # Win Player 1
            self.w2 = pygame.image.load("img/samourai-player2.png").convert() # Win Player 2
            self.wia = pygame.image.load("img/samourai-IA.png").convert() # Win IA
            self.turnp1 = pygame.image.load("img/Menu/Player_one.png").convert_alpha() # Player 1 turn
            self.turnp1_s = pygame.image.load("img/Menu/Player_one_s.png").convert_alpha() # Player 1 turn
            self.turnp2 = pygame.image.load("img/Menu/Player_two.png").convert_alpha() # Player 2 / IA turn 
            self.turnp2_s = pygame.image.load("img/Menu/Player_two_s.png").convert_alpha() # Player 2 / IA turn 
            self.sound_on = pygame.image.load("img/sound.png").convert_alpha()
            self.sound_off = pygame.image.load("img/soundoff.png").convert_alpha()
            self.arrow_right_on = pygame.image.load("img/arrow_right.png").convert_alpha()
            self.arrow_right_off = pygame.image.load("img/arrow_right_off.png").convert_alpha()
            self.arrow_left_on = pygame.image.load("img/arrow_left.png").convert_alpha()
            self.arrow_left_off = pygame.image.load("img/arrow_left_off.png").convert_alpha()
            self.sound_play = 1
        except pygame.error(), message:
            raise SystemExit, message 
        # Init values for the rules, the mode, and the map size
        self.init("config")
        self.create_playlist()
        self.clock = pygame.time.Clock()
        self.deepIA = 1
        self.cut = 0
        self.offset = 0
        self.wait = 0
  
    def find_x(self, x, length, name, font):
        if self.wait == 200:
            self.cut = 0
            self.offset = 0
        if len(name) - (length + self.cut) > 0:
            label = font.render(name[self.cut], 1, (255, 200, 200))
            limit = label.get_size()[0]
            if self.offset == limit:
                self.offset = 0
                self.cut += 1
            else:
                self.offset += 1
            name = name[self.cut:length + self.cut]
            self.wait = 0 
        else:
            self.wait += 1 
            name = name[self.cut:]
        return name, x - self.offset

    # put a new music is there is not
    def put_music(self, actual=0):
        if self.sound_play == 1 and self.titles is not []:
            if pygame.mixer.music.get_busy() == False:
                if actual == 0:
                    if self.cur_music == len(self.titles) - 1:
                        self.cur_music = 0
                    else:
                        self.cur_music += 1
                name = self.titles[self.cur_music]
                try:    
                    pygame.mixer.music.load("music/" + name)
                    pygame.mixer.music.play() 
                except:
                    if self.cur_music == len(self.titles) - 1:
                        self.cur_music = 0
                    else:
                        self.cur_music += 1
                    self.put_music()
                
    # Initialize a playlist
    def create_playlist(self):
        try:
            self.titles = os.listdir("music")
        except:
            self.titles = []
        self.cur_music = 0
        random.shuffle(self.titles)
    
    # Put the content of a file in a list
    def myreadline(self, file):
        conf = []

        for line in file:
            line = line.rstrip('\n')
            if line and line[0] not in ('#', ' ', '\t', '\0'):
                conf.append(line)
        return conf

    # Read the initial paremeters in a config file
    def init(self, config):
        try:
            with open(config, 'r') as file:
                conf = self.myreadline(file)
                try:
                    line = conf[0] 
                    self.rule_2b3 = int(line)
                    if self.rule_2b3 not in (0, 1):
                        self.rule_2b3 = 1
                except:
                    self.rule_2b3 = 1
                
                try:
                    line = conf[1] 
                    self.rule_5brk = int(line)
                    if self.rule_5brk not in (0, 1):
                        self.rule_5brk = 1
                except:
                    self.rule_5brk = 1

                try:
                    line = conf[2] 
                    self.rule_capt = int(line)
                    if self.rule_capt not in (0, 1):
                        self.rule_capt = 1
                except:
                    self.rule_capt = 1

                try:
                    line = conf[3] 
                    self.IA = int(line)
                    if self.IA not in (0, 1):
                        self.IA = 1
                except:
                    self.IA = 1

                try:
                    line = conf[4] 
                    self.size = int(line)
                    if self.size not in range(12, 50):
                        self.size = 19
                except:
                    self.size = 19
                
                try:
                    line = conf[5] 
                    self.select = int(line)
                    if self.select not in (0, 1, 2):
                        self.select = 2
                except:
                    self.select = 2

                try:
                    line = conf[6] 
                    self.skins = int(line)
                    if self.skins not in (0, 1, 2):
                        self.skins = 0
                    if self.skins == 0:
                        self.skinsquare = self.square
                    elif self.skins == 1:
                        self.skinsquare = self.square2
                    elif self.skins == 2:
                        self.skinsquare = self.square3
                except:
                    self.skinsquare = self.square
                    self.skins = 0
                
                try:
                    line = conf[7] 
                    self.skinr = int(line)
                    if self.skinr not in (0, 1, 2):
                        self.skinr = 0
                    if self.skinr == 0:
                        self.skinred = self.tr
                        self.skinred_t = self.rt
                    elif self.skinr == 1:
                        self.skinred = self.tr2
                        self.skinred_t = self.rt2
                    elif self.skinr == 2:
                        self.skinred = self.tr3
                        self.skinred_t = self.rt3
                except:
                    self.skinred = self.tr
                    self.skinred_t = self.rt
                    self.skinr = 0

                try:
                    line = conf[8] 
                    self.skinb = int(line)
                    if self.skinb not in (0, 1, 2):
                        self.skinb = 0
                    if self.skinb == 0:
                        self.skinblue = self.tb
                        self.skinblue_t = self.bt
                    elif self.skinb == 1:
                        self.skinblue = self.tb2
                        self.skinblue_t = self.bt2
                    elif self.skinb == 2:
                        self.skinblue = self.tb3
                        self.skinblue_t = self.bt3
                except:
                    self.skinblue = self.tb
                    self.skinblue_t = self.bt
                    self.skinb = 0

                try:
                    line = conf[9]
                    self.actual = int(line)
                    if self.actual not in (0, 1):
                        self.actual = 1
                except:
                    self.actual = 1

        except IOError:
            self.rule_2b3 = 1
            self.rule_5brk = 1
            self.rule_capt = 1
            self.IA = 1
            self.size = 19
            self.select = 2
            self.skinsquare = self.square
            self.skins = 0
            self.skinred = self.tr
            self.skinred_t = self.rt
            self.skinr = 0
            self.skinblue = self.tb
            self.skinblue_t = self.bt
            self.skinb = 0
            self.actual = 1

    # Delete pair to display
    def delete_pair(self, sizeX, sizeY, token, x, y, value, Display):

	# Right, Left
	if (x < sizeX - 3 and Display.test_prise(sizeX, sizeY, token, x, y, 1, 0, value) == 1):
            self.histo.append([y, x + 1, 0, token[y][x + 1].player, self.turn])
	    token[y][x + 1].player = 0
            self.histo.append([y, x + 2, 0, token[y][x + 2].player, self.turn])
	    token[y][x + 2].player = 0
        elif (x > 2 and Display.test_prise(sizeX, sizeY, token, x, y, -1, 0, value) == 1):
            self.histo.append([y, x - 1, 0, token[y][x - 1].player, self.turn])
	    token[y][x - 1].player = 0
            self.histo.append([y, x - 2, 0, token[y][x - 2].player, self.turn])
	    token[y][x - 2].player = 0

	# Up, Down
	elif (y > 2 and Display.test_prise(sizeX, sizeY, token, x, y, 0, -1, value) == 1):
            self.histo.append([y - 1, x, 0, token[y - 1][x].player, self.turn])
	    token[y - 1][x].player = 0
            self.histo.append([y - 2, x, 0, token[y - 2][x].player, self.turn])
	    token[y - 2][x].player = 0
	elif (y < sizeY - 3 and Display.test_prise(sizeX, sizeY, token, x, y, 0, 1, value) == 1):
            self.histo.append([y + 1, x, 0, token[y + 1][x].player, self.turn])
	    token[y + 1][x].player = 0
            self.histo.append([y + 2, x, 0, token[y + 2][x].player, self.turn])
	    token[y + 2][x].player = 0

	# Up Left, Down Left
	elif (y > 2 and x > 2 and Display.test_prise(sizeX, sizeY, token, x, y, -1, -1, value) == 1):
            self.histo.append([y - 1, x - 1, 0, token[y - 1][x - 1].player, self.turn])
	    token[y - 1][x - 1].player = 0
            self.histo.append([y - 2, x - 2, 0, token[y - 2][x - 2].player, self.turn])
	    token[y - 2][x - 2].player = 0
	elif (y < sizeY - 3 and x > 2 and Display.test_prise(sizeX, sizeY, token, x, y, -1, 1, value) == 1):
            self.histo.append([y + 1, x - 1, 0, token[y + 1][x - 1].player, self.turn])
	    token[y + 1][x - 1].player = 0
            self.histo.append([y + 2, x - 2, 0, token[y + 2][x - 2].player, self.turn])
	    token[y + 2][x - 2].player = 0

	# Up Right, Down Right
	elif (y > 2 and x < sizeX - 3 and Display.test_prise(sizeX, sizeY, token, x, y, 1, -1, value) == 1):
            self.histo.append([y - 1, x + 1, 0, token[y - 1][x + 1].player, self.turn])
	    token[y - 1][x + 1].player = 0
            self.histo.append([y - 2, x + 2, 0, token[y - 2][x + 2].player, self.turn])
	    token[y - 2][x + 2].player = 0
	elif (y < sizeY - 3 and x < sizeX - 3 and Display.test_prise(sizeX, sizeY, token, x, y, 1, 1, value) == 1):
            self.histo.append([y + 1, x + 1, 0, token[y + 1][x + 1].player, self.turn])
	    token[y + 1][x + 1].player = 0
            self.histo.append([y + 2, x + 2, 0, token[y + 2][x + 2].player, self.turn])
	    token[y + 2][x + 2].player = 0
	return 0

    #return 0 if the move is impossible
    def add_token(self, event, token, player, square_size, sizeX, sizeY, Judge, Display):
        x = (event.pos[0] - (square_size / 2)) / square_size
        y = (event.pos[1] - (square_size / 2)) / square_size

        if token[y][x].player == 0:
    	    ret = Judge.Judge(sizeX, sizeY, token, x, y, player + 1)
	    if ret == 0: return 0
            elif ret == -1 :
                Display.screen.blit(self.twob3_icon, ((sizeX + 1) * square_size / 2 - self.twob3_icon.get_size()[0] / 2 + Display.marge, (sizeY + 1) * square_size / 2 - self.twob3_icon.get_size()[1] / 2 + Display.marge))
                Display.refresh()
                while 1:
                    for events in pygame.event.get():
                        if (events.type == pygame.MOUSEBUTTONDOWN
                        or  events.type == pygame.KEYDOWN):
                            return 0
                        elif events.type == pygame.QUIT:
                            sys.exit()
                    pygame.time.wait(10) 
	    elif ret == 2:
	        Display.add_prise(player + 1, Judge.getPtsPlayer1(), Judge.getPtsPlayer2())
	        self.delete_pair(sizeX, sizeY, token, x, y, player + 1, Display)
	    elif ret == 3 or ret == 4: 
                Display.add_prise(player + 1, Judge.getPtsPlayer1(), Judge.getPtsPlayer2())
	        self.delete_pair(sizeX, sizeY, token, x, y, player + 1, Display)
                self.histo.append([y, x, player + 1, 0, self.turn])
                token[y][x].player = player + 1
                self.histo.append([y, x, player + 1, 0, self.turn])
	        Display.draw_finish(player + 1)
                self.end = 1
	        return 2
	    elif Judge.is_win(sizeX, sizeY, token, x, y, player + 1) == 1 and\
	         self.rule_5brk == 0 or self.rule_5brk == 1 and Judge.five_breakable(sizeX, sizeY, token, x, y, player + 1) == 0:
                self.histo.append([y, x, player + 1, 0, self.turn])
	        Display.draw_finish(player + 1)
                self.end = 1
                return 2
            token[y][x].player = player + 1
            self.histo.append([y, x, player + 1, 0, self.turn])
	    Display.draw_background()
            Display.draw_token(token)
            Display.refresh()
	    return 1
        return 0

    # Go back before the last play
    def go_last_play(self, token, Display, Judge, player):
        ret = 1
        while (len(self.histo) > 0 and self.histo[-1][4] == self.turn - 1):
            if self.histo[-1][2] == 0:
                if self.histo[-1][3] == 1:
                    Judge.PtsPlayer2 -= 1
                else:
                    Judge.PtsPlayer1 -= 1
            token[self.histo[-1][0]][self.histo[-1][1]].player = self.histo[-1][3]
            self.histo.pop()
            ret = 0
        if ret == 0:
            self.turn -= 1
            Display.draw_turn(self.turnp1, self.turnp2,
                    self.turnp1_s, self.turnp2_s,
                    Judge.getPtsPlayer1(), Judge.getPtsPlayer2(), player + 1)
            Display.draw_background()
            Display.draw_token(token)
            Display.refresh()
            if self.end == 1:
                self.end = 0
            if self.IA == 1 and len(self.histo) > 0 and self.histo[-1][2] == 1:
                self.go_last_play(token, Display, Judge, player - 1)
        return ret

    def music_elem(self, begin, Display, my_font):
        if self.sound_play == 1:
            Display.screen.blit(self.arrow_left_on, (begin - 30, 230))
            Display.screen.blit(self.sound_on, (self.arrow_left_on.get_size()[0] + begin - 20, 217))
            Display.screen.blit(self.arrow_right_on, (self.arrow_right_on.get_size()[0] +
                self.sound_on.get_size()[0] + begin - 15, 230))
        else:
            Display.screen.blit(self.arrow_left_off, (begin - 30, 230))
            Display.screen.blit(self.sound_off, (self.arrow_left_on.get_size()[0] + begin - 20, 217))
            Display.screen.blit(self.arrow_right_off, (self.arrow_right_on.get_size()[0] +
                self.sound_on.get_size()[0] + begin - 15, 230))

        name = self.titles[self.cur_music]
        name, new = self.find_x(begin + self.arrow_right_on.get_size()[0] +\
                    self.sound_on.get_size()[0] + self.arrow_left_off.get_size()[0] - 5, 35, name, my_font)
        label = my_font.render(name, 1, (255, 200, 200))
        Display.screen.blit(label, (new, 232))


    def launch_game(self, sizeX, sizeY):
        # Marge of the window
        marge = 5

        # Create IA Minmax
        minmax = Minmax.Minmax(self.rule_5brk, self.rule_2b3, self.rule_capt)
        
        # Create token list
        token = [[case.Case(x, y, 0) for x in range(sizeX)] for y in range(sizeY)]

        # Create Referee
        Judge = Referee.Referee(self.rule_5brk, self.rule_2b3, self.rule_capt);

        # Create displayer
        Display = Displayer.Displayer(sizeX, sizeY, self.skinsquare, self.skinred,
                self.skinblue, self.md, self.mu, self.w1, self.w2, self.wia,
                self.skinblue_t, self.skinred_t, marge)

        # Container for historic
        self.histo = []
        self.turn = 0
        self.end = 0

        Display.draw_background()
        pygame.display.flip()

        # Music variable
        ax = (sizeX + 1) * self.square.get_size()[0] + 40
        my_font = pygame.font.SysFont("kinari", 20)
        self.offset = 0
        self.cut = 0

        time = 0
        player = 0;
        Display.draw_turn(self.turnp1, self.turnp2, self.turnp1_s,
                self.turnp2_s, 0, 0, player)
        Display.refresh()
        while 1:
            self.put_music()
            if self.actual == 1:
                 Display.display_actual_player(player, token, self.end)
            for event in pygame.event.get():         
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
                    # Historic
                    elif event.key == pygame.K_BACKSPACE:
                        if self.go_last_play(token, Display, Judge, player) == 0 and player > 0:
                            player -= 1
                    # (Des)Activate current position
                    elif event.key == pygame.K_LCTRL:
                        self.actual = 1 - self.actual
                        Display.draw_background()
                        Display.draw_token(token)
                        Display.refresh()
                    # Change deepIA level
                    elif event.key == pygame.K_KP_PLUS:
                        if self.deepIA < 5:
                            self.deepIA += 2
                    elif event.key == pygame.K_KP_MINUS:
                        if self.deepIA > 1:
                            self.deepIA -= 2
                    # Music management 
                    elif event.key == pygame.K_s:
                        self.sound_play = 1 - self.sound_play
                        if self.sound_play == 0:
                            pygame.mixer.music.pause()
                        else: 
                            pygame.mixer.music.unpause()
                    elif event.key == pygame.K_d and self.sound_play == 1:
                        pygame.mixer.music.stop()
                        if self.cur_music == len(self.titles) - 1:
                            self.cur_music = 0
                        else:
                            self.cur_music += 1
                        self.put_music(1)
                    elif event.key == pygame.K_q and self.sound_play == 1:
                        pygame.mixer.music.stop()
                        if self.cur_music == 0:
                             self.cur_music = len(self.titles) - 1
                        else:
                            self.cur_music -= 1
                        self.put_music(1)

                    # Change skin
                    elif event.key in (pygame.K_KP1, pygame.K_KP2, pygame.K_KP3,
                                       pygame.K_KP4, pygame.K_KP5, pygame.K_KP6,
                                       pygame.K_KP7, pygame.K_KP8, pygame.K_KP9):
                        if event.key == pygame.K_KP1:
                            Display.square = self.square
                            self.skins = 0
                        elif event.key == pygame.K_KP2:
                            Display.square = self.square2
                            self.skins = 1
                        elif event.key == pygame.K_KP3:
                            Display.square = self.square3
                            self.skins = 2
                        elif event.key == pygame.K_KP4:
                            Display.tokenred = self.tr
                            Display.red_trans = self.rt
                            self.skinr = 0
                        elif event.key == pygame.K_KP5:
                            Display.tokenred = self.tr2
                            Display.red_trans = self.rt2
                            self.skinr = 1
                        elif event.key == pygame.K_KP6:
                            Display.tokenred = self.tr3
                            Display.red_trans = self.rt3
                            self.skinr = 2
                        elif event.key == pygame.K_KP7:
                            Display.tokenblue = self.tb
                            Display.blue_trans = self.bt
                            self.skinb = 0
                        elif event.key == pygame.K_KP8:
                            Display.tokenblue = self.tb2
                            Display.blue_trans = self.bt2
                            self.skinb = 1
                        elif event.key == pygame.K_KP9:
                            Display.tokenblue = self.tb3
                            Display.blue_trans = self.bt3
                            self.skinb = 2
                        
                        Display.draw_turn(self.turnp1, self.turnp2, self.turnp1_s,
                                self.turnp2_s, Judge.getPtsPlayer1(), Judge.getPtsPlayer2(),
                                player)
                        Display.draw_background()
                        Display.draw_token(token)
                        Display.refresh()

                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1\
                        and event.pos[0] < sizeX * self.square.get_size()[0] + marge * 2\
                        and event.pos[0] > self.square.get_size()[0] / 2\
                        and event.pos[1] < sizeY * self.square.get_size()[1] + marge * 2\
                        and event.pos[1] > self.square.get_size()[1] / 2\
                        and self.end == 0:
                            test = self.add_token(event, token, player % 2,\
                                    self.square.get_size()[0], sizeX, sizeY, Judge, Display) 
                            
                            if test == 1:
                                if self.IA == 1:
                                    Display.draw_turn(self.turnp1, self.turnp2,
                                            self.turnp1_s, self.turnp2_s,
                                            Judge.getPtsPlayer1(), Judge.getPtsPlayer2(), 1)
                                    map = [[case.Case(x, y, token[y][x]) for x in range(sizeX)] for y in range(sizeY)]                            
                                    self.clock.tick()
                                    res = minmax.evaluation(map, self.deepIA, Judge)
                                    time = self.clock.tick()
                                    if Judge.is_win(sizeX, sizeY, token, res[0], res[1], 2) == 1:
                                        if Display.draw_finish(0) == 0:
                                            return
                                        self.end = 1
    	                            retpair = Judge.Judge(sizeX, sizeY, token, res[0], res[1], 2)
                                    if retpair > 1:
	                                Display.add_prise(2, Judge.getPtsPlayer1(), Judge.getPtsPlayer2())
	                                self.delete_pair(sizeX, sizeY, token, res[0], res[1], 2, Display)
                                        if retpair == 4:
                                            self.histo.append([y, x, player + 1, 0, self.turn])
                                            token[y][x].player = 2
                                            self.histo.append([y, x, player + 1, 0, self.turn])
	                                    Display.draw_finish(3)
                                            self.end = 1
	                                    return
                                    token[res[1]][res[0]].player = 2
                                    self.turn += 1 
                                    self.histo.append([res[1], res[0], 2, 0, self.turn])
                                    Display.draw_turn(self.turnp1, self.turnp2,
                                        self.turnp1_s, self.turnp2_s,
                                        Judge.getPtsPlayer1(), Judge.getPtsPlayer2(), 0)
                                    player = 0
                                else:
                                    Display.draw_turn(self.turnp1, self.turnp2,
                                            self.turnp1_s, self.turnp2_s,
                                            Judge.getPtsPlayer1(), Judge.getPtsPlayer2(), player + 1)
                                    player += 1
	                        Display.draw_background()
                                Display.draw_token(token)
                            if test != 0 and test != -1:
                                self.turn += 1
                            if test == 2:
                                if Display.finish == 1:
                                    return
                                else:
                                    if self.IA == 0:
                                        player -= 1
                                    Display.draw_turn(self.turnp1, self.turnp2,
                                            self.turnp1_s, self.turnp2_s,
                                            Judge.getPtsPlayer1(), Judge.getPtsPlayer2(), player + 1)
                                    Display.draw_background()
                                    Display.draw_token(token)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.pos[0] in range(ax - 30, ax - 30 + self.arrow_left_on.get_size()[0])\
                    and event.pos[1] in range(230 + self.arrow_left_on.get_size()[1])\
                    and self.sound_play == 1:
                        pygame.mixer.music.stop()
                        if self.cur_music == 0:
                             self.cur_music = len(self.titles) - 1
                        else:
                            self.cur_music -= 1
                        self.put_music()

                    if event.pos[0] in range(ax - 30 + self.arrow_left_on.get_size()[0] + 5,\
                            + ax - 30 + self.arrow_left_on.get_size()[0] + 5 + \
                            self.sound_on.get_size()[0])\
                    and event.pos[1] in range(230 + self.sound_on.get_size()[1]):
                        self.sound_play = 1 - self.sound_play
                        if self.sound_play == 0:
                            pygame.mixer.music.pause()
                        else: 
                            pygame.mixer.music.unpause()

                    if event.pos[0] in range(ax - 30 + self.arrow_left_on.get_size()[0] + 10 +\
                       self.sound_on.get_size()[0], ax - 30 + self.arrow_left_on.get_size()[0] +\
                       10 + self.sound_on.get_size()[0] + self.arrow_right_on.get_size()[0])\
                    and event.pos[1] in range(230 + self.arrow_right_on.get_size()[1])\
                    and self.sound_play == 1:
                        pygame.mixer.music.stop()
                        if self.cur_music == len(self.titles) - 1:
                            self.cur_music = 0
                        else:
                            self.cur_music += 1
                        self.put_music()

            Display.draw_turn(self.turnp1, self.turnp2,
                              self.turnp1_s, self.turnp2_s,
                              Judge.getPtsPlayer1(), Judge.getPtsPlayer2(), player + 1)
            self.music_elem(ax, Display, my_font)
  	    if self.IA == 1:
                Display.display_time(time)
            Display.refresh()
            pygame.time.wait(10)
