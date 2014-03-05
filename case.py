#!/usr/bin/env python2.7

class Case:

    def __init__(self, x = 0, y = 0, player = 0):
        self.x = x
        self.y = y
        self.player = player

    def __eq__(self, other):
        if self.player == other:
            return True
        return False

    def __ne__(self, other):
        if self.player == other:
            return False
        return True
