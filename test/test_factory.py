from __future__ import annotations
import unittest
from azul.factory import Factory
from azul.bag import Bag
from typing import List
from azul.tileSources import tableCenter
from azul.simple_types import RED, BLUE, YELLOW, GREEN, BLACK, Tile

class testFactory(unittest.TestCase):
    def setUp(self) -> None:
        self.bag: Bag = Bag()
        self.center: tableCenter = tableCenter()
        self.factory: Factory = Factory(self.bag, self.center)


    def test_factory(self) -> None:
        self.assertTrue(self.factory.isEmpty)
        self.assertTrue(self.factory.state() == "")
        ##Empty at the begining 
        self.factory.startNewRound()
        self.assertTrue(len(self.factory.state()) == 4)
        self.factory.tiles: List[Tile] = [RED, RED, BLUE, BLUE]
        ##Start of round
        self.assertEqual(self.factory.take(5), [])
        ##Take non-existent
        self.assertEqual(self.factory.take(1), [RED, RED])
        ##Take existing
        self.assertEqual(self.factory.state(), "")
        ##Check state after succesful take
        self.assertEqual(self.factory.take(1), [])
        ##Take from empty 


if __name__ == '__main__':
    unittest.main()