from __future__ import annotations
import unittest
from azul.floor import Floor
from azul.simple_types import RED, BLUE, YELLOW, GREEN, BLACK
from azul.patternLine import patternLine
from azul.simple_types import Points
from azul.wallLine import WallLine 
from azul.usedTiles import usedTiles

class testpatterLine(unittest.TestCase):
    def setUp(self) -> None:
        self.used: usedTiles = usedTiles()
        self.wall: WallLine = WallLine()
        self.floor: Floor = Floor([Points(1), Points(2), Points(2)], self.used)

    def test_patternLine(self) -> None:
        pLine: patternLine = patternLine(1, self.floor, self.used, self.wall)
        self.assertEqual(pLine.capacity, 1)
        self.assertEqual(pLine.line, [])
        pLine.put([RED])
        self.assertEqual(pLine.line, [RED])
        ##Normal put
        pLine.put([BLUE])
        self.assertEqual(pLine.line, [RED])
        ##Put into full
        self.assertEqual(pLine.finishRound().__str__(), Points(1).__str__()) 
        ##Finish round 
        self.assertEqual(pLine.line, [])
        self.assertEqual(pLine.capacity, 1)
        ##Empty after finished round 
        ##Normal patternLine testing 
        pLine: patternLine = patternLine(-1, self.floor, self.used, self.wall)
        self.assertEqual(pLine.line, [])
        self.assertEqual(pLine.capacity, 0)
        ##Incorrect patternLine testing
        pLine: patternLine = patternLine(1, self.floor, self.used, self.wall)
        pLine.put([RED,RED])
        self.assertEqual(pLine.state(), "R")
        self.assertEqual(pLine.floor.state(), "R")
        ##Overflow of patterLine using floor
        


if __name__ == '__main__':
    unittest.main()
