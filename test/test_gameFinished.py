from __future__ import annotations
import unittest
from typing import List, Any
from azul.gameFinished import GameFinished
from azul.interfaces import FinishRoundResult
from azul.simple_types import Tile, RED, BLUE, YELLOW, GREEN, BLACK

class testpatterLine(unittest.TestCase):
    def test_patternLine(self) -> None:
        wl: List[List[Any]] = [
            [RED, BLUE, None, None, None],
            [None, None, None, None, None],
            [None, None, None, None, None],
            [None, None, None, None, None],
            [None, None, None, None, None]
        ]
        self.assertFalse(GameFinished().verify(wl))
        wl = [
            [None, None, None, None, None],
            [None, None, None, None, None],
            [None, None, None, None, None],
            [None, None, None, None, None],
            [None, None, None, None, None]
        ]
        self.assertFalse(GameFinished().verify(wl))
        wl = [
            [RED, BLUE, YELLOW, GREEN, BLACK],
            [None, None, None, None, None],
            [None, None, None, None, None],
            [None, None, None, None, None],
            [None, None, None, None, None]
        ]
        self.assertTrue(GameFinished().verify(wl))

if __name__ == '__main__':
    unittest.main()
