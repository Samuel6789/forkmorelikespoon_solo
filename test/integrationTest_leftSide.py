from __future__ import annotations
from azul.bag import Bag
import unittest
from azul.usedTiles import usedTiles
from azul.tableArea import TableArea
from typing import List
from azul.simple_types import RED, GREEN, BLUE, Tile

class integrationTest(unittest.TestCase):
    def setUp(self) -> None:
        self.used: usedTiles = usedTiles()
        self.bag: Bag = Bag(self.used)
        self.table: TableArea = TableArea(2, self.bag)
        
    def integrationTest_LeftSide(self) -> None:
        self.assertTrue(len(self.table.factories) == 5)
        self.assertTrue(len(self.bag.state()) == 100)
        self.bag.tiles = [RED, GREEN, BLUE, GREEN, RED, RED, BLUE, GREEN] #R1B2Y3G4L5
        self.bag.used.tiles = [GREEN, GREEN, GREEN, GREEN, GREEN]
        self.table.factories[3].startNewRound()
        self.assertEqual(self.table.factories[3].state(), "RGBG")
        self.table.factories[4].startNewRound()
        self.assertEqual(self.table.factories[4].state(), "RRBG")
        self.assertEqual(self.bag.state(),"") 
        self.table.take(3, 4)
        self.assertEqual(self.table.table_Center.state(), "SRB")
        self.assertEqual(self.table.factories[3].state(), "")

        take_result: List[Tile] = self.bag.take(3) 
        self.assertEqual(self.usedTiles.state(),"") 
        self.assertEqual(take_result, [GREEN, GREEN, GREEN])

        self.table.take(4, 4)
        self.assertEqual(self.table.table_Center.state(), "SRBRRB")
        self.table.take(-1, 1)
        self.assertFalse(self.table.isRoundEnd())
        self.table.take(-1, 2)
        self.assertEqual(self.table.table_Center.state(), "")
        self.assertTrue(self.table.isRoundEnd())
        self.bag.tiles = [RED, GREEN, BLUE, GREEN, RED, RED, BLUE, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN]
        self.table.startNewRound()
        self.assertEqual(self.bag.state(), "")


if __name__ == '__main__':
    unittest.main()