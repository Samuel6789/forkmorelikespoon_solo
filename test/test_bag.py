from __future__ import annotations
import unittest
from azul.bag import Bag
from azul.usedTiles import usedTiles
from azul.simple_types import RED

class testBag(unittest.TestCase):
    def setUp(self) -> None:
        self.used: usedTiles = usedTiles()
        self.used.tiles = [RED]
        self.bag: Bag = Bag(self.used)

    def test_bag(self) -> None:
        self.assertTrue(len(self.bag.state()) == 100)
        self.assertTrue(self.bag.state().count("B") == self.bag.state().count("L") == self.bag.state().count("Y") == self.bag.state().count("R")
                        == self.bag.state().count("G") == 20)
        ##Correct initialization 
        self.assertTrue(len(self.bag.take(4)) == 4)
        ##Can take from bag
        self.assertTrue(self.bag.tileCount == 96)
        ##Has updated counter
        self.assertTrue(len(self.bag.state()) == 96)
        ##State works
        self.assertEqual(self.bag.take(-1), [])
        ##Negative use of take
        self.assertEqual(self.bag.take(97), [])
        ##Out of bounds use of take
        self.bag.take(96)
        ##Take all from bag
        self.assertEqual(self.bag.state(), "")
        self.assertTrue(self.bag.tileCount == 0)
        ##Is the bag empty If we take all 
        self.assertEqual(self.bag.take(1), [RED])
        ##Take from a empty bag 
        

if __name__ == '__main__':
    unittest.main()
