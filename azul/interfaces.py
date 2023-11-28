from __future__ import annotations
from typing import List, Set
from azul.simple_types import Tile


class UsedTilesGiveInterface:
    def give(self, tiles: List[Tile]) -> None:
        pass
class GameInterface:
    ''''''

    def __init__(self) -> None:
        pass

class ObserverInterface:
    '''perposiela observerom state z board-u'''
    def __init__(self) -> None:
        '''prepares GUI in a GUI implementation'''
        self._observers: Set[str] = []
        pass

    def notify(self, newState:str):
        '''in a GUI implementation this would pop up a window with a message'''
        print(f"new state is: {newState}")

    def registerObserver(self, name: str) -> None:
        self._observers.add(name)

    def cancelObserver(self, name: str) -> None:
        self._observers -= name