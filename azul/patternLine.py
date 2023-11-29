from __future__ import annotations
from typing import List
from simple_types import Tile, compress_tile_list, Points, RED, BLUE, YELLOW, GREEN, BLACK
from floor import Floor
from usedTiles import usedTiles
from wallLine import WallLine

class patternLine():
    def __init__(self, capacity: int, floorLine: Floor, usedTiles: usedTiles, wall : WallLine) -> None:
        self.floor: Floor = floorLine
        self.wall: WallLine = wall
        self.used: usedTiles = usedTiles
        self.capacity: int = capacity

        if self.capacity < 0:
            self.capacity = 0
        self.line: List[Tile] = []
    
    def put(self, tiles: List[Tile]) -> None:
        currentCapacity: int = self.capacity - len(self.line)
        if currentCapacity == 0:
            self.floor.put(tiles)
            return
        while currentCapacity > 0:
            self.line.append(tiles.pop())
            currentCapacity -= 1
        self.floor.put(tiles)

    def state(self) -> str:
        return "".join([str(x) for x in self.line])
    
    def finishRound(self) -> Points:
        if len(self.line) < self.capacity:
            return Points(0)
        
        resultingPoints: Points = self.wall.putTile(self.line.pop())
        self.used.give(self.line)
        self.line = []
        return resultingPoints