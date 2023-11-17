from __future__ import annotations
from typing import List
from azul.simple_types import Tile, RED
from azul.interfaces import FactoryBagInterface, TileSource


class Factory(TileSource):
    def __init__(self, bag: FactoryBagInterface, table_center: TileSource) -> None:
        self.bag = bag
        self.table_center = table_center

    def take(self, idx: Tile) -> List[Tile]:
        self._idx = idx
        return [RED]

    def is_empty(self) -> bool:
        return True

    def state(self) -> str:
        return ""

    def start_new_round(self) -> None:
        pass
