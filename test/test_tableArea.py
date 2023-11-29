from __future__ import annotations
import unittest
from typing import List
from azul.simple_types import Tile, STARTING_PLAYER, RED, GREEN, Points
from azul.tileSources import TileSource, tableCenter

class TestTileSources(unittest.TestCase):
    def setUp(self) -> None:
        self.tileSources: TileSource = TileSource()
        self.center: tableCenter = tableCenter()

    def test_tileSources(self) -> None:
        ...