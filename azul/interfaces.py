from __future__ import annotations
from typing import List, Optional
from abc import ABC, abstractmethod
from azul.simple_types import Tile

class UsedTilesGiveInterface:
    def give(self, tiles: List[Tile]) -> None:
        pass

class WallLineGetTilesInterface(ABC):
    @abstractmethod
    def get_tiles(self) -> Optional[List[Tile]]:
        pass
