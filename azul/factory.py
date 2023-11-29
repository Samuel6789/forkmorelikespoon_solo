from __future__ import annotations
from typing import List
from simple_types import Tile, compress_tile_list, Points, RED, BLUE, YELLOW, GREEN, BLACK
from bag import Bag
from azul.tileSources import TileSource
from azul.tileSources import tableCenter


class Factory(TileSource):
    def __init__(self, bag: Bag, center: tableCenter) -> None:
        super().__init__()
        self.bag: Bag = bag 
        self.center: tableCenter = center
    
    def startNewRound(self) -> None:
        self.tiles += self.bag.take(4)
    
    def take(self, colour: int) -> list[Tile]:
        result: List[Tile] = super().take(colour)
        if result == []:
            return result
        self.center.add(self.tiles)
        self.tiles.clear()
        return result