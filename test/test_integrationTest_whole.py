from __future__ import annotations
from azul.bag import Bag
import unittest
from azul.usedTiles import usedTiles
from azul.tableArea import TableArea
from typing import List
from azul.simple_types import RED, BLUE, YELLOW, GREEN, BLACK, Tile, Points
from azul.game import Game

class integrationTest(unittest.TestCase):
    def setUp(self) -> None:
        self.game: Game = Game(2)
        
    def test_integrationTest_Whole(self) -> None:
        self.game.bag.tiles = [BLUE, BLUE, BLUE, BLUE, #0
                               BLACK, RED, RED, RED, #1
                               BLUE, YELLOW, YELLOW, YELLOW, #2
                               RED, BLUE, YELLOW, GREEN, #3
                               BLUE, BLUE, BLUE, BLUE] #4
        self.game.bag.tileCount = 20
        self.game.queue = [0,1]
        for factory in self.game.table.factories:
            factory.tiles = []
        self.game.table.startNewRound()
        self.game.players[0]._wall[0]._tilesInLine = [RED, BLUE, YELLOW, GREEN, None]
        self.game.players[0]._wall[1]._tilesInLine = [BLACK,None,None,None,None]
        self.game.players[0]._wall[2]._tilesInLine = [GREEN,None,None,None,None]
        self.game.players[0]._wall[3]._tilesInLine = [YELLOW,None,None,None,None]
        self.game.players[0]._points = Points(19)
        #playerID: int, sourceID: int, colour: int, destinationID: int
        self.assertFalse(self.game.take(1, 0, 2, 4)) ##wrong player order
        self.assertFalse(self.game.take(0, -2, 2, 4))##wrong origin index negative
        self.assertFalse(self.game.take(0, 5, 2, 4))##wrong origin index positive
        self.assertFalse(self.game.take(0, 0, 1, 4))##non-present colour
        self.assertTrue(self.game.take(0, 0, 2, 4))#0
        self.assertTrue(self.game.take(1, 3, 2, 0))#3 RBG
        self.assertTrue(self.game.take(0, 2, 2, 4))#2 RBGYYY
        self.assertTrue(self.game.take(1, -1, 3, 2))#-1 RBG
        self.assertTrue(self.game.take(0, 1, 5, 0))#1 RRRRBG
        self.assertTrue(self.game.take(1, 4, 2, 3))#4 RRRRBG
        self.assertTrue(self.game.take(0, -1, 4, 0))#4 RRRRG
        self.assertTrue(self.game.take(1, -1, 1, 4))#4 
        self.assertEqual(self.game.players[0].state(), ": has number of points 37")


        
if __name__ == '__main__':
    unittest.main()