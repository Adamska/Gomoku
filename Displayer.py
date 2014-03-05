import pygame

class Displayer:

    def __init__(self, sizeX, sizeY, square, tr, tb, md, mu, w1, w2, wia, bt, rt, marge):

	# set attribut
	self.marge = marge;
	self.sizeX = sizeX;
	self.sizeY = sizeY;
        self.square = square
        self.tokenred = tr
        self.tokenblue = tb
        self.blue_trans = bt
        self.red_trans = rt
        self.winp1 = w1
        self.winp2 = w2
        self.winia = wia
        self.mu = mu    # Menu up
        self.md = md    # Menu down
        self.margin = pygame.Surface((5, (self.sizeY + 1) * self.square.get_size()[1] + self.marge * 2))
	self.margin.fill((0, 0, 0))
        self.finish = 0

        # Get size of the window. 400 is add for menu
        self.size = width, height = 406 + (sizeX + 1) * square.get_size()[0] + marge * 2,\
		(sizeY + 1) * square.get_size()[1] + marge * 2

        self.screen = pygame.display.set_mode(self.size, pygame.DOUBLEBUF, 32)
        self.screen.fill((0, 0, 0))
        self.display_game_menu()

    # refresh the window
    def refresh(self):
        pygame.display.flip()

    # Display time of IA turn
    def display_time(self, time):
        begin = (self.sizeX + 1) * self.square.get_size()[0] + 2 * self.marge + 10, 700
        tmp = time;

        if tmp == 0:
            list = "0"
        else:
            list = ""
        while tmp != 0:
            list = str(tmp % 10) + list
            tmp /= 10

        list = "IA turn time : " + list + " ms"
        my_font = pygame.font.SysFont("kinari", 20)
        label = my_font.render(list, 1, (255, 255, 255))
        self.screen.blit(label, begin)
        

    
    # Draw picture for the winner
    def draw_finish(self, player):
        if player == 1:
            img = self.winp1
        elif player == 2:
            img = self.winp2
        else:
            img = self.winia
        
        self.screen = pygame.display.set_mode(img.get_size())
        self.screen.blit(img, (0, 0))
        pygame.display.flip()
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                    self.screen = pygame.display.set_mode(self.size, pygame.DOUBLEBUF, 32)
                    self.display_game_menu()
                    return 1
                elif (event.type == pygame.KEYDOWN
                or event.type == pygame.MOUSEBUTTONDOWN
                or event.type == pygame.QUIT):
                    self.finish = 1
                    return 0
            pygame.time.wait(10)

    # Draw game menu
    def display_game_menu(self):
	self.screen.blit(self.mu, ((self.sizeX + 1) * self.square.get_size()[0] + 10,
	    6, 400, self.sizeY * self.square.get_size()[1]))

	if self.sizeY > 15:
  	    self.screen.blit(self.md, ((self.sizeX + 1)* self.square.get_size()[0] + 10,
	        6 + (self.sizeY + 1) * self.square.get_size()[1] - self.md.get_size()[1],
		        self.md.get_size()[0], self.md.get_size()[1]))


    # Draw tokens already won
    def draw_taken_captures(self, pts1, pts2):
        player = 1

        while pts1 > 0:
            posx = self.sizeX * self.square.get_size()[0] + 230 * (player - 1) + 85
            posy = 300 + pts1 * 35
            self.screen.blit(self.tokenred, (posx, posy, self.tokenred.get_size()[0], self.tokenred.get_size()[1]))
            self.screen.blit(self.tokenred, (posx + 70, posy, self.tokenred.get_size()[0], self.tokenred.get_size()[1]))
            pts1 -= 2;

        while pts2 > 0:
            player = 2
            posx = self.sizeX * self.square.get_size()[0] + 230 * (player - 1) + 85
            posy = 300 + pts2 * 35
            self.screen.blit(self.tokenblue, (posx, posy, self.tokenblue.get_size()[0], self.tokenblue.get_size()[1]))
            self.screen.blit(self.tokenblue, (posx + 70, posy, self.tokenblue.get_size()[0], self.tokenblue.get_size()[1]))
            pts2 -= 2;

    # Highlight the player name when it's his turn
    def draw_turn(self, P1, P2, P1_s, P2_s, pts1, pts2, player):
        self.display_game_menu()
        self.draw_taken_captures(pts1, pts2)
        if player % 2 == 0:
            self.screen.blit(P2, ((self.sizeX + 1) * self.square.get_size()[0] + 235, 271))
            self.screen.blit(P1_s, ((self.sizeX + 1) * self.square.get_size()[0], 225))
        else:
            self.screen.blit(P2_s, ((self.sizeX + 1) * self.square.get_size()[0] + 192, 225))
            self.screen.blit(P1, ((self.sizeX + 1) * self.square.get_size()[0] + 11, 271))
        self.screen.blit(self.margin, ((self.sizeX + 1) * self.square.get_size()[0] + self.marge, 0))
        self.screen.blit(self.margin, (405 + (self.sizeX + 1) * self.square.get_size()[0] + self.marge, 0))
        self.refresh()

    def draw_token(self, token):
	y = 0
	while y < len(token):
            x = 0
            while x < len(token[y]):
                if token[y][x].player != 0:

                    # center token in the pente
                    if token[y][x].player == 1:
                        self.screen.blit(self.tokenred, (self.marge +  x * self.square.get_size()[0] + \
                        (self.square.get_size()[0] - self.tokenred.get_size()[0] / 2),\
                        self.marge + y * self.square.get_size()[1] + (self.square.get_size()[1] -\
                        self.tokenred.get_size()[1] / 2), self.tokenred.get_size()[0],\
                        self.tokenred.get_size()[1]))
                    else:
                        self.screen.blit(self.tokenblue, (self.marge +  x * self.square.get_size()[0] + \
                        (self.square.get_size()[0] - self.tokenblue.get_size()[0] / 2),\
                        self.marge + y * self.square.get_size()[1] + (self.square.get_size()[1] -\
                        self.tokenblue.get_size()[1] / 2), self.tokenblue.get_size()[0],\
                        self.tokenblue.get_size()[1]))
                x += 1
	    y += 1

    def draw_background(self):
        j = self.marge
        while j < self.square.get_size()[1] * (self.sizeY + 1):
	     i = self.marge
             while i < self.square.get_size()[0] * (self.sizeX + 1):
         	    self.screen.blit(self.square, (i, j, self.square.get_size()[0],\
			    self.square.get_size()[1]))
		    i = i + self.square.get_size()[0]
	     j = j + self.square.get_size()[1]

    # print two points for the player who had succeed in prise
    def add_prise(self, player, ptsplayer1, ptsplayer2):
        posx = self.sizeX * self.square.get_size()[0] + 230 * (player - 1) + 85
        if player == 1:
	    posy = 300 + ptsplayer1 * 35
        else:
	    posy = 300 + ptsplayer2 * 35

	if player == 1:
	    self.screen.blit(self.tokenred, (posx, posy, self.tokenred.get_size()[0], self.tokenred.get_size()[1]))
	    self.screen.blit(self.tokenred, (posx + 70, posy, self.tokenred.get_size()[0], self.tokenred.get_size()[1]))
	    ptsplayer1 += 2;
	else:
	    self.screen.blit(self.tokenblue, (posx, posy, self.tokenblue.get_size()[0], self.tokenblue.get_size()[1]))
	    self.screen.blit(self.tokenblue, (posx + 70, posy, self.tokenblue.get_size()[0], self.tokenblue.get_size()[1]))
	    ptsplayer2 += 2;

    def test_prise(self, sizeX, sizeY, token, x, y, valX, valY, value):
	enemy = 1
	if value == 1:
	    enemy = 2

	if (token[y + valY][x + valX].player == enemy and \
		token[y + 2 * valY][x + 2 * valX].player == enemy and \
		token[y + 3 * valY][x + 3 * valX].player == value):
		return 1
	return 0

    def display_actual_player(self, player, token, end):
        mousex, mousey = pygame.mouse.get_pos()
        mousex = (mousex - self.tokenred.get_size()[0] / 2) / self.square.get_size()[0]
        mousey = (mousey - self.tokenred.get_size()[1] / 2) / self.square.get_size()[1]
        if (mousex < 0 or mousex > self.sizeX - 1
        or  mousey < 0 or mousey > self.sizeY - 1
        or token[mousey][mousex].player != 0
        or end == 1):
            return
        case = (self.marge + mousex * self.square.get_size()[0] +
               (self.square.get_size()[0] - self.tokenred.get_size()[0] / 2),
                self.marge + mousey * self.square.get_size()[1] +
               (self.square.get_size()[1] - self.tokenred.get_size()[1] / 2))

        self.draw_background()
        self.draw_token(token)
        if player % 2 == 0:
            self.screen.blit(self.red_trans, case)
        else:
            self.screen.blit(self.blue_trans, case)
        self.refresh()
