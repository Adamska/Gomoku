import copy

# TODO Ne prend pas encore en compte les prise de pairs (fonction eval_weight)
class Minmax:

    def __init__(self, five_breakable = 1, double_trois = 1, prise = 1):
        self.five_breakable = five_breakable
        self.double_trois = double_trois
        self.prise = prise

    # Fonction de calcul de score pour un joueur en fonction d'une map
    def eval_weight(self, map, player, x, y, Ref):

        save_x = x
        save_y = y
        weight = 0
        tmp = 0
        if player == 2:
            weightPrise = Ref.getPtsPlayer2()
        else:
            weightPrise = Ref.getPtsPlayer1()

        # pair
        if Ref.is_prise(len(map), len(map[0]), map, x, y, player) == 1:
            weight = weightPrise * weightPrise * weightPrise * weightPrise + 1

        # right / left
        while x > 0 and map[y][x].player== player:
            x = x - 1
        if map[y][x].player!= player:
            x = x + 1
        while x < len(map[0]) and map[y][x].player== player:
            x = x + 1
            tmp = tmp + 1
        weight = weight + (tmp * tmp * tmp * tmp)

        x = save_x
        y = save_y
        tmp = 0

        # up / down
        while y > 0 and map[y][x].player== player:
            y = y - 1
        if map[y][x].player!= player:
            y = y + 1
        while y < len(map) and map[y][x].player== player:
            y = y + 1
            tmp = tmp + 1
        weight = weight + (tmp * tmp * tmp * tmp)

        x = save_x
        y = save_y
        tmp = 0

        # down / right
        while y > 0 and x > 0 and map[y][x].player== player:
            y = y - 1
            x = x - 1
        if map[y][x].player!= player:
            y = y + 1
            x = x + 1
        while y < len(map) and x < len(map[0]) and map[y][x].player== player:
            y = y + 1
            x = x + 1
            tmp = tmp + 1
        weight = weight + (tmp * tmp * tmp * tmp)

        x = save_x
        y = save_y
        tmp = 0

        # down / left
        while y > 0 and x < len(map[0]) - 1 and map[y][x].player== player:
            y = y - 1
            x = x + 1
        if map[y][x].player!= player:
            y = y + 1
            x = x - 1
        while y < len(map) and x > 0 and map[y][x].player== player:
            y = y + 1
            x = x - 1
            tmp = tmp + 1

        weight = weight + (tmp * tmp * tmp * tmp)

        return weight

    def eval_empty(self, map, player, x, y):

        save_x = x
        save_y = y
        weight = 0
        tmp = 0

        # left
        if x > 0:
            x = x - 1
        while x > 0 and map[y][x].player== player:
            x = x - 1
            tmp = tmp + 1
        weight = weight + (tmp * tmp * tmp * tmp)
        x = save_x
        tmp = 0

        # right
        if x < len(map[0]):
            x = x + 1
        while x < len(map[0]) and map[y][x].player== player:
            x = x + 1
            tmp = tmp + 1
        weight = weight + (tmp * tmp * tmp * tmp)
        x = save_x
        tmp = 0

        # up
        if y > 0:
            y = y - 1
        while y > 0 and map[y][x].player== player:
            y = y - 1
            tmp = tmp + 1
        weight = weight + (tmp * tmp * tmp * tmp)
        y = save_y
        tmp = 0

        # down
        if y < len(map):
            y = y + 1
        while y < len(map) and map[y][x].player== player:
            y = y + 1
            tmp = tmp + 1
        weight = weight + (tmp * tmp * tmp * tmp)
        y = save_y
        tmp = 0

        # up / right
        if y > 0 and x < len(map[0]):
            y = y - 1
            x = x + 1
        while y > 0 and x < len(map[0]) and map[y][x].player== player:
            y = y - 1
            x = x + 1
            tmp = tmp + 1
        weight = weight + (tmp * tmp * tmp * tmp)
        x = save_x
        y = save_y
        tmp = 0

        # up / left
        if y > 0 and x > 0:
            y = y - 1
            x = x - 1
        while y > 0 and x > 0 and map[y][x].player== player:
            y = y - 1
            x = x - 1
            tmp = tmp + 1
        weight = weight + (tmp * tmp * tmp * tmp)
        x = save_x
        y = save_y
        tmp = 0

        # down / left
        if y < len(map) and x > 0:
            y = y + 1
            x = x - 1
        while y < len(map) and x > 0 and map[y][x].player== player:
            y = y + 1
            x = x - 1
            tmp = tmp + 1
        weight = weight + (tmp * tmp * tmp * tmp)
        x = save_x
        y = save_y
        tmp = 0

        # down / left
        if y < len(map) and x < len(map[0]):
            y = y + 1
            x = x + 1
        while y < len(map) and x < len(map[0]) and map[y][x].player== player:
            y = y + 1
            x = x + 1
            tmp = tmp + 1
        weight = weight + (tmp * tmp * tmp * tmp)

        return weight

    # Fonction d'evaluation de gain potentiel si le coup x, y etait joue
    def eval(self, map, y, x, deep, Judge):
        if deep == 0:
            return pdn

        # TODO, rajouter regle double trois
        if map[y][x].player!= 0:
            return -1

        # On regarde le poids de l'ia et du joueur avant le coup
        weightIaNow = self.eval_empty(map, 2,x , y)
        weightPlayerNow = self.eval_empty(map, 1, x, y)

        # On execute le coup pour l'ia
        map[y][x].player= 2
        weightIa = self.eval_weight(map, 2, x, y, Judge)

        # On execute le coup si le joueur le placait
        map[y][x].player= 1
        weightPlayer = self.eval_weight(map, 1, x , y, Judge)

        # On remet la case a 0
        map[y][x].player= 0

        # On revoit le poids de la map si le coup avait ete joue
        # c'est a dire notre gain ajouter a la perte du joueur si le coup etait joue
        return (weightIa - weightIaNow) + (weightPlayer - weightPlayerNow)

    def is_first_token(self, token):
        x = 0
        y = 0
        while (y < len(token)):
            x = 0
            while (x < len(token)):
                if token[y][x].player== 2:
                    return 0
                x = x + 1
            y = y + 1
        return 1

    # Opti: definition d'une zone utilise de travail pour l'ia
    def zone_util(self, token):
        y = len(token) / 2
        x = len(token[0]) / 2
        maxX = 0
        maxY = 0

        i = 0
        j = 0
        while j < len(token):
            i = 0
            while i < len(token[0]):
                if token[i][j].player != 0:
                    if j < x:
                        x = j
                    if maxX < j:
                        maxX = j
                    if i < y:
                        y = i
                    if maxY < i:
                        maxY = i
                i = i + 1
            j = j + 1

        maxX = maxX + 1
        maxY = maxY + 1

        if maxX >= len(token[0]): maxX = len(token[0]) - 1
        if maxY >= len(token): maxY = len(token) - 1

        if x > 0: x = x - 1
        if y > 0: y = y - 1

        return (x, y, maxX, maxY)

    # Revoi 1 si la case selectionnee est a cote d'une case non vide
    def is_against_player(self, token, x, y):

        # up right
        if y > 0 and x < len(token[0]) - 1 and token[y - 1][x + 1].player!= 0: return 1

        # right
        if x < len(token[0]) - 1 and token[y][x + 1].player!= 0: return 1

        # down right
        if y < len(token) - 1 and x < len(token[0]) - 1 and token[y + 1][x + 1].player!= 0: return 1

        # down
        if y < len(token) - 1 and token[y + 1][x].player!= 0: return 1

        # up
        if y > 0 and token[y - 1][x].player!= 0: return 1

        # left 
        if x > 0 and token[y][x - 1].player!= 0: return 1

        # up left
        if x > 0 and y > 0 and token[y - 1][x - 1].player!= 0: return 1

        # down left
        if x > 0 and y < len(token) - 1 and token[y + 1][x - 1].player!= 0: return 1

        return 0

    def evaluation(self, map, deep, Judge):
        ret = self.evaluationRec(map, deep, Judge)
        return ret[0], ret[1], ret[2]

    def evaluationRec(self, map, deep, Judge):
        j = 0
        max = 0
        maxX = 0
        maxY = 0
        Len = len(map)
        LenW = len(map[0])

        if deep == 1:
          while j < Len:
             i = 0
             while i < LenW:
                    if map[j][i].player == 0 and self.is_against_player(map, i, j) == 1\
                    and Judge.double_trois(LenW, Len, map, i, j, 2):
                        tmp = self.eval(map, j, i, deep, Judge)
                        if tmp > max:
                            max = tmp
                            maxX = i
                            maxY = j
                    i = i + 1
             j = j + 1
        else:
          while j < Len:
             i = 0
             while i < LenW:
                    if map[j][i].player == 0 and self.is_against_player(map, i, j) == 1\
                    and Judge.double_trois(LenW, Len, map, i, j, deep % 2 + 1):

                        # Si le coup teste est un coup gagnant pour l'ia
                        if deep % 2 + 1 == 2 and Judge.is_win(LenW, Len, map, i, j, 2) == 1:
                            return i, j, 100000

                        ## Si le coup teste est un coup gagnant pour le joueur
                        elif deep % 2 + 1 == 1 and Judge.is_win(LenW, Len, map, i, j, 1) == 1:
                            return i, j, -100000

                        map[j][i].player = deep % 2 + 1 # joueur
                        ret = self.evaluationRec(map, deep - 1, Judge)
                        map[j][i].player = 0
                        if ret[2] > 99995:
                            return i, j, (ret[2] - 1)
                        if ret[2] < -99995:
                            return i, j, (ret[2] + 1)
                        if ret[2] > max:
                            max = ret[2]
                            maxX = ret[0]
                            maxY = ret[1]
                    i = i + 1
             j = j + 1
        return maxX, maxY, max
