from __future__ import annotations
from typing import List
from tileSources import tableCenter
from factory import Factory
from simple_types import Tile

class TableArea:
    def __init__(self, factories: List[Factory], tableCenter: tableCenter) -> None:
        self.factories = factories
        self.tableCenter = tableCenter
        self.roundEnded = False

    def take(self, sourceIdx: int, colour: int) -> List[Tile]:
        if sourceIdx >= len(self.factories):
            raise ValueError("Invalid source index")
        
        source = self.factories[sourceIdx] if sourceIdx != -1 else self.tableCenter
        return source.take(colour)

    def isRoundEnd(self) -> bool:
        return all(factory.isEmpty() for factory in self.factories) and self.tableCenter.isEmpty()

    def startNewRound(self):
        if not self.isRoundEnd():
            raise Exception("Cannot start a new round before the current one has ended")
        
        for factory in self.factories:
            factory.startNewRound()
        self.roundEnded = False

    def state(self) -> str:
        factories_state = ' '.join([f.state() for f in self.factories])
        center_state = self.tableCenter.state()
        return f"Factories: {factories_state} | Center: {center_state}"