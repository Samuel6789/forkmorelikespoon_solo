from __future__ import annotations
from typing import List, Dict, Any
from simple_types import RED, BLUE, YELLOW, GREEN, BLACK, Tile, Points
from interfaces import gameInterface
from board import Board
from patternLine import patternLine
from finalPointsCalculation import FinalPointsCalculation
from floor import Floor
from wallLine import WallLine
from gameFinished import GameFinished
from interfaces import FinishRoundResult
from usedTiles import usedTiles
from tableArea import TableArea
from bag import Bag
from wallLine import WallLine
import random 

class Game(gameInterface):
    def __init__(self, numOfPlayers: int) -> None:
        self.players: Dict[int, Board] = dict()
        self.used: usedTiles = usedTiles()
        self.bag: Bag = Bag(self.used)
        self.table: TableArea = TableArea(numOfPlayers, self.bag)
        for playedID in range(numOfPlayers):
            self.players[playedID] = Board(self.used)
        
        chooseFirst: int = random.randint(0,numOfPlayers - 1)
        self.players[chooseFirst]._is_first = True
        self.queue = self.generateQueue()
        self.table.startNewRound()
    
    def generateQueue(self) -> List[int]:
        playerQueue: List[int] = [x for x in range(len(self.players.values()))]
        for playerIndex in range(len(self.players.values())):
            if self.players[playerIndex]._is_first:
                playerQueue = playerQueue[playerIndex:] + playerQueue[0:playerIndex]
        return playerQueue
      

    def take(self, playerID: int, sourceID: int, colour: int, destinationID: int) -> bool:
        if playerID != self.queue[0]:
            return False
        if self.table.isEmpty(sourceID):
            return False
        if not self.table.isIn(sourceID, colour):
            return False
        
        currentPlayerNumber: int = self.queue.pop(0)
        self.queue.append(currentPlayerNumber)
        takenTiles: List[Tile] = self.table.take(sourceID, colour)
        currentPlayer: Board = self.players[playerID]
        currentPlayer.put(destinationID, takenTiles)

        if self.table.isRoundEnd():
            for player in self.players.values():
                endG = player.finishRound()
                if not endG == True:
                    print(player.state())
                    return True
            self.generateQueue()
        

        return True
    