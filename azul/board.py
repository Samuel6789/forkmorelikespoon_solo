from typing import List
from azul.simple_types import Points, Tile, STARTING_PLAYER
import pattern_line
import floor
from interfaces import UsedTilesGiveInterface

class Board:
    _points: Points = Points(0)
    _is_first: bool = False        # indicates 
    _wall = None        # instancia wall line
    _floor = floor.Floor([], UsedTilesGiveInterface)
    _player_name: str = ""
    _pattern_line: pattern_line.PatternLine = pattern_line.PatternLine

    def __init__(self, player_name: str = "") -> None:
        self._player_name = player_name
    
    def finishRound(self):
        '''zavola finish round z patternline a zapocita vratene body'''
        pass

    def put(self, destinationIdx: int, tiles: List[Tile]):
        if tiles == []:     #uz nie je co vybrat => koncim kolo
            self.finishRound()
        elif tiles == [STARTING_PLAYER]:
            self._is_first = True;
            floor.put([STARTING_PLAYER])
        else:
            self._is_first = False
            tile_placement_points = pattern_line.put(destinationIdx, tiles)
            self._points = Points.sum([self._points, tile_placement_points])        #nastavi nove body

    def state(self) -> str:
        """vypise kolko bodov ma dany hrac"""
        out = f"{self._player_name}: has number of points {str(self._points)}"
    
    
