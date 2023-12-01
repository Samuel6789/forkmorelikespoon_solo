from __future__ import annotations
from typing import List, Dict
from tileSources import tableCenter
from factory import Factory
from simple_types import Tile
from bag import Bag

class TableArea:
    def __init__(self, numOfPlayers: int, bag: Bag) -> None:
        self.tableCenter: tableCenter = tableCenter()
        self.factories: List[Factory] = list()
        for i in range (1 + numOfPlayers*2):
            self.factories.append(Factory(bag, self.tableCenter))

    def take(self, sourceIdx: int, colour: int) -> List[Tile]:
        if sourceIdx >= len(self.factories):
            raise ValueError("Invalid source index")
        
        source = self.factories[sourceIdx] if sourceIdx != -1 else self.tableCenter
        return source.take(colour)
    
    def isIn(self, index: int, colour: int) -> bool:
        mapColours: Dict[int, str] = {0 : "S", 1 : "R", 2 : "B", 3 : "Y", 4 : "G", 5 : "L"}
        colourSTR: str = mapColours[colour]
        if index >= len(self.factories) or index < -1:
            return False
        source = self.factories[index] if index != -1 else self.tableCenter
        return colourSTR in source.state()

    def isEmpty(self, index: int) -> bool:
        if index >= len(self.factories) or index < -1:
            return False
        source = self.factories[index] if index != -1 else self.tableCenter
        return source.isEmpty()
    
    def isRoundEnd(self) -> bool:
        return all(factory.isEmpty() for factory in self.factories) and self.tableCenter.isEmpty()

    def startNewRound(self) -> None:
        for factory in self.factories:
            factory.startNewRound()

    def state(self) -> str:
        factories_state: str = ' '.join([f.state() for f in self.factories])
        center_state: str = self.tableCenter.state()
        return f"Factories: {factories_state} | Center: {center_state}"