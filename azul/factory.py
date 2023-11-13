from __future__ import annotations
from typing import List
from azul.simple_types import Tile, compress_tile_list
from azul.interfaces import TileSource
from azul.table_center import TableCenter
from azul.bag import Bag

class Factory(TileSource):
    def __init__(self, _tiles: list[Tile], table_center: TableCenter) -> None:
        self._tiles = _tiles
        self._table_center = table_center
        

    def take(self, _idx: Tile) -> List[Tile]:
        _tiles = [i for i in self._tiles if i == _idx]
        self._table_center.add(self._tiles)
        self._tiles.clear()
        return _tiles


    def is_empty(self) -> bool:
        if len(self.state) == 0:
            return True
        return False
    

    def state(self) -> str:
        return compress_tile_list(self._tiles)    
        
    
    def start_new_round(self) -> None:
        self._tiles.extend(Bag.take(4))