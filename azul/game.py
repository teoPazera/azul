from __future__ import annotations
from typing import List
from interfaces.game_interface import GameInterface
from azul.bag import Bag
from azul.used_tiles import UsedTiles


class Game(GameInterface):
    
    _bag = Bag(UsedTiles, )