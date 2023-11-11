from __future__ import annotations
from typing import List
from azul.simple_types import Tile
from abc import ABC, abstractmethod


class UsedTilesGiveInterface:
    def give(self, tiles: List[Tile]) -> None:
        pass

class UsedTilesTakeAllInterface(ABC):
    @abstractmethod
    def take_all(self) -> List[Tile]:
        pass
