from __future__ import annotations
from azul.bag import Bag
import unittest
from typing import List
from azul.simple_types import RED, BLUE, YELLOW, GREEN, BLACK, Tile, Points
from azul.board import Board
from azul.patternLine import patternLine
from azul.finalPointsCalculation import FinalPointsCalculation
from azul.floor import Floor
from azul.wallLine import WallLine
from azul.gameFinished import GameFinished
from azul.interfaces import FinishRoundResult
from azul.usedTiles import usedTiles

class test(unittest.TestCase):
    def setUp(self) -> None:
        self.used: usedTiles = usedTiles()
        self.board: Board = Board(self.used)

    def test_integrationTest_RightSide(self) -> None:
        self.board.put(5,[RED,RED])
        self.board.finishRound()
        self.assertEqual(self.board._points._value, -2)
        self.board._points = Points(0)
        self.board.put(0,[RED])
        self.board.finishRound()
        self.assertTrue(self.board._points._value == 1)
        self.board.put(0,[YELLOW])
        self.board.put(1,[RED,RED])
        self.board.finishRound()
        self.board.put(0,[BLUE])
        self.board.finishRound()
        self.assertEqual(self.board._points._value, 8)
        self.board.put(1,[BLACK,BLACK])
        self.board.put(2,[GREEN, GREEN, GREEN])
        self.board.put(3,[YELLOW,YELLOW,YELLOW,YELLOW])
        self.board.put(4, [BLUE,BLUE,BLUE,BLUE,BLUE])
        self.board.finishRound()
        self.assertEqual(self.board._points._value, 24)
        self.board.put(0, [GREEN])
        self.board.finishRound()
        self.board.put(0, [BLACK])
        self.assertEqual(self.board.finishRound(), FinishRoundResult.GAME_FINISHED)
        self.assertEqual(self.board._points._value, 42)
        self.assertEqual(self.board.state(), ": has number of points 42")
        


if __name__ == '__main__':
    unittest.main()