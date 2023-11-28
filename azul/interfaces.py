from __future__ import annotations
from typing import List
from simple_types import Tile
from simple_types import Points

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