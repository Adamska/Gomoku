class Referee:
    
    def __init__(self, five_breakable = 1, double_trois = 1, prise = 1):

	# set attribut use for bonus, possibilitie to disable the rules?
	self.PtsPlayer1 = 0
	self.PtsPlayer2 = 0
	self.fiveC = five_breakable
	self.DoubleT = double_trois
	self.Prise = prise

    # Return the player 1 points
    def getPtsPlayer1(self):
	return self.PtsPlayer1

    # Return the player 2 points
    def getPtsPlayer2(self):
	return self.PtsPlayer2

    # Return 1 if the five is breakable in one direction
    def check_five(self, sizeX, sizeY, token, x, y, value, enemy, dir):

        max = 0
        good = 0

        if dir == "hori":
            while (x > 0 and token[y][x - 1].player == value):
                x -= 1
            while (x <= sizeX - 1 and token[y][x].player == value):
                if ((y > 0 and y < sizeY - 2 and token[y - 1][x].player == enemy
                    and token[y + 1][x].player == value and token[y + 2][x].player == 0)
                or (y > 1 and y < sizeY - 1 and token[y - 1][x].player == value
                    and token[y - 2][x].player == 0 and token[y + 1][x].player == enemy)):
                    good = 0
                else:
                    good += 1
                max = max if (good < max) else good
                x += 1
            if max < 5:
                return 1
        
        elif dir == "verti":
            while (y > 0 and token[y - 1][x].player == value):
                y -= 1
            while (y <= sizeY - 1 and token[y][x].player == value):
                if ((x > 0 and x < sizeX - 2 and token[y][x - 1].player == enemy
                    and token[y][x + 1].player == value and token[y][x + 2].player == 0)
                or (x > 1 and x < sizeX - 1 and token[y][x - 1].player == value
                    and token[y][x - 2].player == 0 and token[y][x + 1].player == enemy)):
                    good = 0
                else:
                    good += 1
                max = max if (good < max) else good
                y += 1
            if max < 5:
                return 1
        
        elif dir == "diagLeft":
            while (x > 0 and y > 0 and token[y - 1][x - 1].player == value):
                x -= 1
                y -= 1
            while (x <= sizeX - 1 and y <= sizeY - 1 and token[y][x].player == value):
                if ((y > 0 and y < sizeY - 2 and x > 1 and x < sizeX - 1
                    and token[y - 1][x + 1].player == enemy and token[y + 1][x - 1].player == value
                    and token[y + 2][x - 2].player == 0)
                or (y > 1 and y < sizeY - 1 and x > 0 and x < sizeX - 2
                    and token[y - 1][x + 1].player == value and token[y - 2][x + 2].player == 0
                    and token[y + 1][x - 1].player == enemy)):
                    good = 0
                else:
                    good += 1
                max = max if (good < max) else good
                x += 1
                y += 1
            if max < 5:
                return 1
        
        elif dir == "diagRight":
            while (x > 0 and y < sizeY - 2 and token[y + 1][x - 1].player == value):
                x -= 1
                y += 1
            while (x <= sizeX - 1 and y >= 0 and token[y][x].player == value):
                if ((y > 0 and y < sizeY - 2 and x > 0 and x < sizeX - 2 and
                    token[y - 1][x - 1].player == enemy and token[y + 1][x + 1].player == value
                    and token[y + 2][x + 2].player == 0)
                or (y > 1 and y < sizeY - 1 and x > 1 and x < sizeX - 2 and
                    token[y - 1][x - 1].player == value and token[y - 2][x - 2].player == 0
                    and token[y + 1][x + 1].player == enemy)):
                    good = 0
                else:
                    good += 1
                max = max if (good < max) else good
                x += 1
                y -= 1
            if max < 5:
                return 1
 
        return 0

    # Return 1 if the five is breakable
    def five_breakable(self, sizeX, sizeY, token, x, y, value):
        enemy = 2 if (value == 1) else 1

        # Horizontale
        if ((self.check_five(sizeX, sizeY, token, x, y, value, enemy, "hori") == 0)
        
        # verticale
        or (self.check_five(sizeX, sizeY, token, x, y, value, enemy, "verti") == 0)
	
        # Diagonale Left
        or (self.check_five(sizeX, sizeY, token, x, y, value, enemy, "diagLeft") == 0)

        # Diagonale Right
        or (self.check_five(sizeX, sizeY, token, x, y, value, enemy, "diagRight") == 0)):
	    return 0
        return 1
    
    def double_trois(self, sizeX, sizeY, token, x, y, value):
        nb_free = 0

        #horizontale
        if ((x < sizeX - 3 and x > 0 and token[y][x + 1].player == value and token[y][x + 2].player == value
                and token[y][x + 3].player == 0 and token[y][x - 1].player == 0)
        or (x < sizeX - 1 and x > 2 and token[y][x - 1].player == value and token[y][x - 2].player == value
                and token[y][x - 3].player == 0 and token[y][x + 1].player == 0)
        or (x < sizeX - 2 and x > 1 and token[y][x - 1].player == value and token[y][x + 1].player == value
                and token[y][x - 2].player == 0 and token[y][x + 2].player == 0)
        or (x < sizeX - 4 and x > 0 and token[y][x - 1].player == 0 and token[y][x + 1].player == 0
                and token[y][x + 2].player == value and token[y][x + 3].player == value and token[y][x + 4].player == 0)
        or (x < sizeX - 2 and x > 2 and token[y][x + 1].player == value and token[y][x + 2].player == 0
                and token[y][x - 1].player == 0 and token[y][x - 2].player == value and token[y][x - 3].player == 0)
        or (x < sizeX - 1 and x > 3 and token[y][x + 1].player == 0 and token[y][x - 1].player == value
                and token[y][x - 2].player == 0 and token[y][x - 3].player == value and token[y][x - 4].player == 0)
        or (x < sizeX - 4 and x > 0 and token[y][x - 1].player == 0 and token[y][x + 1].player == value
                and token[y][x + 2].player == 0 and token[y][x + 3].player == value and token[y][x + 4].player == 0)
        or (x < sizeX - 3 and x > 1 and token[y][x - 1].player == value and token[y][x - 2].player == 0
                and token[y][x + 1].player == 0 and token[y][x + 2].player == value and token[y][x + 3].player == 0)
        or (x < sizeX - 1 and x > 3 and token[y][x + 1].player == 0 and token[y][x - 1].player == 0
                and token[y][x - 2].player == value and token[y][x - 3].player == value and token[y][x - 4].player == 0)):
            nb_free += 1
       
        #verticale
        if ((y < sizeY - 3 and y > 0 and token[y + 1][x].player == value and token[y + 2][x].player == value
                and token[y + 3][x].player == 0 and token[y - 1][x].player == 0)
        or (y < sizeY - 1 and y > 2 and token[y - 1][x].player == value and token[y - 2][x].player == value
                and token[y - 3][x].player == 0 and token[y + 1][x].player == 0)
        or (y < sizeY - 2 and y > 1 and token[y - 1][x].player == value and token[y + 1][x].player == value
                and token[y - 2][x].player == 0 and token[y + 2][x].player == 0)
        or (y < sizeX - 4 and y > 0 and token[y - 1][x].player == 0 and token[y + 1][x].player == 0
                and token[y + 2][x].player == value and token[y + 3][x].player == value and token[y + 4][x].player == 0)
        or (y < sizeY - 2 and y > 2 and token[y + 1][x].player == value and token[y + 2][x].player == 0
                and token[y - 1][x].player == 0 and token[y - 2][x].player == value and token[y - 3][x].player == 0)
        or (y < sizeY - 1 and y > 3 and token[y + 1][x].player == 0 and token[y - 1][x].player == value
                and token[y - 2][x].player == 0 and token[y - 3][x].player == value and token[y - 4][x].player == 0)
        or (y < sizeY - 4 and y > 0 and token[y - 1][x].player == 0 and token[y + 1][x].player == value
                and token[y + 2][x].player == 0 and token[y + 3][x].player == value and token[y + 4][x].player == 0)
        or (y < sizeY - 3 and y > 1 and token[y - 1][x].player == value and token[y - 2][x].player == 0
                and token[y + 1][x].player == 0 and token[y + 2][x].player == value and token[y + 3][x].player == 0)
        or (y < sizeY - 1 and y > 3 and token[y + 1][x].player == 0 and token[y - 1][x].player == 0
                and token[y - 2][x].player == value and token[y - 3][x].player == value and token[y - 4][x].player == 0)):
            nb_free += 1

        #diagonale UR & DL
        if ((y < sizeY - 1 and y > 2 and x < sizeX - 3 and x > 0 and token[y - 1][x + 1].player == value and token[y - 2][x + 2].player == value
                and token[y - 3][x + 3].player == 0 and token[y + 1][x - 1].player == 0)
        or (y < sizeY - 3 and y > 0 and x < sizeX - 1 and x > 2 and token[y + 1][x - 1].player == value and token[y + 2][x - 2].player == value
                and token[y + 3][x - 3].player == 0 and token[y - 1][x + 1].player == 0)
        or (y < sizeY - 2 and y > 1 and x < sizeX - 2 and x > 1 and token[y + 1][x - 1].player == value and token[y - 1][x + 1].player == value
                and token[y + 2][x - 2].player == 0 and token[y - 2][x + 2].player == 0)
        or (y < sizeY - 4 and y > 0 and x < sizeX - 1 and x > 3 and token[y - 1][x + 1].player == 0 and token[y + 1][x - 1].player == 0
                and token[y + 2][x - 2].player == value and token[y + 3][x - 3].player == value and token[y + 4][x - 4].player == 0)
        or (y < sizeY - 2 and y > 2 and x < sizeX - 3 and x > 1 and token[y - 1][x + 1].player == 0 and token[y - 2][x + 2].player == value
                and token[y - 3][x + 3].player == 0 and token[y + 1][x - 1].player == value and token[y + 2][x - 2].player == 0)
        or (y < sizeY - 1 and y > 3 and x < sizeX - 4 and x > 0 and token[y + 1][x - 1].player == 0 and token[y - 1][x + 1].player == value
                and token[y - 2][x + 2].player == 0 and token[y - 3][x + 3].player == value and token[y - 4][x + 4].player == 0)
        or (y < sizeY - 4 and y > 0 and x < sizeX - 1 and x > 3 and token[y - 1][x + 1].player == 0 and token[y + 1][x - 1].player == value
                and token[y + 2][x - 2].player == 0 and token[y + 3][x - 3].player == value and token[y + 4][x - 4].player == 0)
        or (y < sizeY - 3 and y > 1 and x < sizeX - 2 and x > 2 and token[y - 1][x + 1].player == value and token[y - 2][x + 2].player == 0
                and token[y + 1][x - 1].player == 0 and token[y + 2][x - 2].player == value and token[y + 3][x - 3].player == 0)
        or (y < sizeY - 1 and y > 3 and x < sizeX - 4 and x > 0 and token[y + 1][x - 1].player == 0 and token[y - 1][x + 1].player == 0
                and token[y - 2][x + 2].player == value and token[y - 3][x + 3].player == value and token[y - 4][x + 4].player == 0)):
            nb_free += 1

       #diagonale UL & DR
        if ((y < sizeY - 3 and y > 0 and x < sizeX - 3 and x > 0 and token[y + 1][x + 1].player == value and token[y + 2][x + 2].player == value
                and token[y + 3][x + 3].player == 0 and token[y - 1][x - 1].player == 0)
        or (y < sizeY - 1 and y > 2 and x < sizeX - 1 and x > 2 and token[y - 1][x - 1].player == value and token[y - 2][x - 2].player == value
                and token[y - 3][x - 3].player == 0 and token[y + 1][x + 1].player == 0)
        or (y < sizeY - 2 and y > 1 and x < sizeX - 2 and x > 1 and token[y - 1][x - 1].player == value and token[y + 1][x + 1].player == value
                and token[y - 2][x - 2].player == 0 and token[y + 2][x + 2].player == 0)
        or (y < sizeY - 4 and y > 0 and x < sizeX - 4 and x > 0 and token[y - 1][x - 1].player == 0 and token[y + 1][x + 1].player == 0
                and token[y + 2][x + 2].player == value and token[y + 3][x + 3].player == value and token[y + 4][x + 4].player == 0)
        or (y < sizeY - 2 and y > 2 and x < sizeX - 2 and x > 2 and token[y - 1][x - 1].player == 0 and token[y - 2][x - 2].player == value
                and token[y - 3][x - 3].player == 0 and token[y + 1][x + 1].player == value and token[y + 2][x + 2].player == 0)
        or (y < sizeY - 1 and y > 3 and x < sizeX - 1 and x > 3 and token[y + 1][x + 1].player == 0 and token[y - 1][x - 1].player == value
                and token[y - 2][x - 2].player == 0 and token[y - 3][x - 3].player == value and token[y - 4][x - 4].player == 0)
        or (y < sizeY - 4 and y > 0 and x < sizeX - 4 and x > 0 and token[y - 1][x - 1].player == 0 and token[y + 1][x + 1].player == value
                and token[y + 2][x + 2].player == 0 and token[y + 3][x + 3].player == value and token[y + 4][x + 4].player == 0)
        or (y < sizeY - 3 and y > 1 and x < sizeX - 3 and x > 1 and token[y - 1][x - 1].player == value and token[y - 2][x - 2].player == 0
                and token[y + 1][x + 1].player == 0 and token[y + 2][x + 2].player == value and token[y + 3][x + 3].player == 0)
        or (y < sizeY - 1 and y > 3 and x < sizeX - 1 and x > 3 and token[y + 1][x + 1].player == 0 and token[y - 1][x - 1].player == 0
                and token[y - 2][x - 2].player == value and token[y - 3][x - 3].player == value and token[y - 4][x - 4].player == 0)):
            nb_free += 1

        if nb_free >= 2:
            return 0
        return 1

    def test_prise(self, sizeX, sizeY, token, x, y, valX, valY, value):
	enemy = 1
	if value == 1:
	    enemy = 2

	if (token[y + valY][x + valX].player == enemy and \
		token[y + 2 * valY][x + 2 * valX].player == enemy and \
		token[y + 3 * valY][x + 3 * valX].player == value):
		return 1
	return 0
	    
    # Check if the move is a prise
    def is_prise(self, sizeX, sizeY, token, x, y, value):

	# Right, Left
	if (x < sizeX - 3 and self.test_prise(sizeX, sizeY, token, x, y, 1, 0, value) == 1):
	    return 1
	if (x > 2 and self.test_prise(sizeX, sizeY, token, x, y, -1, 0, value) == 1):
	    return 1
	
        # Up, Down
	if (y > 2 and self.test_prise(sizeX, sizeY, token, x, y, 0, -1, value) == 1):
	    return 1
	if (y < sizeY - 3 and self.test_prise(sizeX, sizeY, token, x, y, 0, 1, value) == 1):
	    return 1

	# Up Left, Down Left
	if (y > 2 and x > 2 and self.test_prise(sizeX, sizeY, token, x, y, -1, -1, value) == 1):
	    return 1
	if (y < sizeY - 3 and x > 2 and self.test_prise(sizeX, sizeY, token, x, y, -1, 1, value) == 1):
	    return 1

	# Up Right, Down Right
	if (y > 2 and x < sizeX - 3 and self.test_prise(sizeX, sizeY, token, x, y, 1, -1, value) == 1):
	    return 1
	if (y < sizeY - 3 and x < sizeX - 3 and self.test_prise(sizeX, sizeY, token, x, y, 1, 1, value) == 1):
	    return 1
	return 0

    # Check the number of pieces in one specific direction
    def browse_in_direction(self, token, x, y, value, dir):
        save = (x, y)

        count = 0
	
        # Test left and right
        if (dir == "hori"):
            while x >= 0 and token[y][x].player == value:
                x -= 1
                count += 1
            x = save[0] + 1
            while x < len(token[y]) and token[y][x].player == value:
                x += 1
                count += 1
            if count >= 5:
                return 1
            return 0

	# Test up and down
        elif (dir == "verti"):
            while y >= 0 and token[y][x].player == value:
                y -= 1
                count += 1
            y = save[1] + 1
            while y < len(token) and token[y][x].player == value:
                y += 1
                count += 1
            if count >= 5:
                return 1
            return 0

	# Test up-left and down-right
        elif (dir == "left-diag"):
            while x >= 0 and y >= 0 and token[y][x].player == value:
                x -= 1
                y -= 1
                count += 1
            x = save[0] + 1
            y = save[1] + 1
            while y < len(token) - 1 and x <= len(token[y]) - 1 and token[y][x].player == value:
                x += 1
                y += 1
                count += 1
            if count >= 5:
                return 1
            return 0

        # Test up-right and down-left
        elif (dir == "right-diag"):
            while x >= 0 and y < len(token) and token[y][x].player == value:
                x -= 1
                y += 1
                count += 1
            x = save[0] + 1
            y = save[1] - 1
            while x < len(token[y]) and y >= 0 and token[y][x].player == value:
                x += 1
                y -= 1
                count += 1
            if count >= 5:
                return 1
            return 0


    # Check if the token is aligned with four others
    def is_win(self, sizeX, sizeY, token, x, y, value):

	token[y][x].player = value

	# Test left and Right
        if self.browse_in_direction(token, x, y, value, "hori") == 1:
            return 1

	# Test up and down
        if self.browse_in_direction(token, x, y, value, "verti") == 1:
            return 1

	# Test up-left and down-right
        if self.browse_in_direction(token, x, y, value, "left-diag") == 1:
            return 1

	# Test up-right and down-left
	if self.browse_in_direction(token, x, y, value, "right-diag") == 1:
            return 1

	token[y][x].player = 0
        return 0

    # function who judge if the move is possible. return 1 if possible, else 0
    def Judge(self, sizeX, sizeY, token, x, y, player):
	if self.DoubleT == 1 and self.double_trois(sizeX, sizeY, token, x, y, player) == 0:
	    return -1
	if self.Prise == 1 and self.is_prise(sizeX, sizeY, token, x, y, player) == 1:
	    if player == 1:
	        self.PtsPlayer1 = self.PtsPlayer1 + 2
		if self.PtsPlayer1 == 10: return 3
	    else:
	        self.PtsPlayer2 = self.PtsPlayer2 + 2
		if self.PtsPlayer2 == 10: return 4
	    return 2
	return 1

