from __future__ import annotations
from typing import List
from azul.simple_types import Tile, compress_tile_list
from azul.interfaces import TileSource, FactoryBagInterface
from azul.table_center import TableCenter

class Factory(TileSource):
    def __init__(self, bag: FactoryBagInterface, table_center: TableCenter) -> None:
        self._tiles = []
        self.bag = bag
        self.table_center = table_center

    def take(self, _idx: Tile) -> List[Tile]:
        _tiles = [i for i in self._tiles if i == _idx]
        while _tiles[0] in self._tiles:
            self._tiles.remove(_tiles[0])
        self.table_center.add(self._tiles)
        self._tiles.clear()
        return _tiles        

    def is_empty(self) -> bool:
        if len(self.state()) == 0:
            return True
        return False

    def state(self) -> str:
        return compress_tile_list(self._tiles)    
    
    def start_new_round(self, _tiles: list[Tile] = []) -> None:
        #ability to add tiles for testing purposes fix later to just use bag
        if _tiles == []:
            self._tiles.extend(self.bag.take(4))
        else:
            self._tiles.extend(_tiles)
