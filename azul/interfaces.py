from __future__ import annotations
from typing import List
from simple_types import Tile
from simple_types import Points
from enum import Enum

class UsedTilesGiveInterface:
    def give(self, tiles: List[Tile]) -> None:
        pass

class wallLinePutTileInterface:
    def putTile(self, tile: Tile) -> Points:
        pointInterface: Points = Points(1)
        return pointInterface

class tableCenterAddInterface:
    def add(self, tiles: list[Tile]):
        pass

class bagState:
    def __init__(self) -> None:
        self.tiles = []
    
    def fakeAdd(self, tiles: list[Tile]) -> None:
        self.tiles += tiles
    
    def state(self):
        return "".join([str(x) for x in self.tiles])
    
class FinishRoundResult(Enum):
    NORMAL = True
    GAME_FINISHED = False