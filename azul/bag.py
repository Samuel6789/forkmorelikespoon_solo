from __future__ import annotations
from typing import List
from simple_types import Tile, compress_tile_list, Points, RED, BLUE, YELLOW, GREEN, BLACK
import random
from usedTiles import usedTiles

class Bag:
    def __init__(self, used: usedTiles) -> None:
        self.used = used
        self.tileCount: int = 100
        self.tiles: list[Tile] = []
        for i in range(20):
            self.tiles.append(RED)
            self.tiles.append(BLUE)
            self.tiles.append(YELLOW)
            self.tiles.append(GREEN)
            self.tiles.append(BLACK)
        self.shuffle()
    
    def state(self) -> str:
        return "".join([str(x) for x in self.tiles])
    
    def take(self, count: int) -> list[Tile]:
        if self.tiles == []:
            self.tiles = self.used.takeAll()
            self.tileCount = len(self.tiles)
        if count < 0 or count > self.tileCount:
            return []
        result: list[Tile] = []
        for i in range(count):
            self.tileCount -= 1
            result.append(self.tiles.pop(0))
        return result
    
    def shuffle(self) -> None:
        for i in range(2*len(self.tiles)):
            randomx: int = random.randint(0, len(self.tiles) - 1)
            randomy: int = random.randint(0, len(self.tiles) - 1)
            temp: Tile = self.tiles[randomx]
            self.tiles[randomx] = self.tiles[randomy]
            self.tiles[randomy] = temp
        



