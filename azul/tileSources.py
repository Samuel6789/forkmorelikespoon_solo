from __future__ import annotations
from typing import List
from interfaces import UsedTilesGiveInterface
from simple_types import Tile, compress_tile_list, Points, RED, BLUE, YELLOW, GREEN, BLACK
from bag import Bag

class TileSource:
    def __init__(self) -> None:
        self.tiles: list[Tile] = []
    
    def isEmpty(self) -> bool:
        return (self.tiles == [])
    
    def take(self, colour: str) -> list[Tile]:
        result: list[Tile] = []
        i: int = 0
        while i < len(self.tiles):
            if colour == self.tiles[i].__str__():
                result.append(self.tiles.pop(i))
            else:
                i += 1
        return result
    
    def state(self) -> str:
        return "".join([str(x) for x in self.tiles])

class Factory(TileSource):
    def __init__(self, bag: Bag, center: TableCenter) -> None:
        super().__init__()
        self.bag: Bag = bag 
        self.center: TableCenter = center
    
    def startNewRound(self) -> None:
        if not super().isEmpty():
            raise Exception("Factory not empty at the end of round")
        self.tiles += self.bag.take(4)
    
    def take(self, colour: str) -> list[Tile]:
        result: list[Tile] = super().take(colour)
        self.center.add(self.tiles)
        self.tiles.clear()
        return result

class TableCenter(TileSource):
    def __init__(self) -> None:
        super().__init__()

    def add(self, tiles: list[Tile]) -> None:
        self.tiles += tiles