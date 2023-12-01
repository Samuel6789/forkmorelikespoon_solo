from __future__ import annotations
from typing import List, Set, Any
from simple_types import Tile, Points
from enum import Enum


class GameInterface:
    ''''''

    def __init__(self) -> None:
        pass

class ObserverInterface:
    '''perposiela observerom state z board-u'''
    def __init__(self) -> None:
        '''prepares GUI in a GUI implementation'''
        self._observers: Set[str] = set()
        pass

    def notify(self, newState:str) -> None:
        '''in a GUI implementation this would pop up a window with a message'''
        print(f"new state is: {newState}")

    def registerObserver(self, name: str) -> None:
        self._observers.add(name)

    def cancelObserver(self, name: str) -> None:
        self._observers.remove(name)


class FinishRoundResult(Enum):
    NORMAL = True
    GAME_FINISHED = False
    
class gameInterface:
    def __init__(self) -> None:
        pass

    def take(self, playerID: int, sourceID: int, colour: int, destinationID: int):
        pass