from __future__ import annotations
import unittest
from typing import List
from azul.tablearea import TableArea
from azul.interfaces import BagInterface
from azul.bag import Bag
from azul.interfaces import RngInterface, UsedTilesTakeAllInterface
from azul.simple_types import RED, BLACK, GREEN, Tile, BLUE, YELLOW, STARTING_PLAYER


class FakeUsedTilesTakeAllInterface(UsedTilesTakeAllInterface):
    def take_all(self) -> List[Tile]:
        return [RED] * 10 + [BLACK] * 12 + [GREEN] * 11

class FakeRngInterface(RngInterface):
    def permutation (self, count: int, length:int) -> List[int]:
        return list(range(count))

class TestTableArea(unittest.TestCase):
    _table_area : TableArea
    _bag: BagInterface
    _rng: RngInterface
    _used_tiles: UsedTilesTakeAllInterface

    def setUp(self) -> None:
        _rng = FakeRngInterface()
        _used_tiles = FakeUsedTilesTakeAllInterface()
        _bag = Bag(_used_tiles, _rng)
        self._table_area = TableArea(5, _bag)
    
    def test_table_area1(self) -> None:
        #take, state, is_round_end, start new_round test
        # only valid moves
        self.assertEqual(self._table_area.state(), "0-\n1-\n2-\n3-\n4-\n5-\n")
        self._table_area.start_new_round()
        self.assertEqual(self._table_area.state(), '0-S\n1-RGLB\n2-YRGL\n3-BYRG\n4-LBYR\n5-GLBY\n')
        self.assertFalse(self._table_area.is_round_end())

        self.assertEqual(self._table_area.take(1 ,RED), [RED])
        self.assertEqual(self._table_area.state(), '0-SGLB\n1-\n2-YRGL\n3-BYRG\n4-LBYR\n5-GLBY\n')
        self.assertEqual(self._table_area.take(2, RED), [RED])
        self.assertEqual(self._table_area.state(), '0-SGLBYGL\n1-\n2-\n3-BYRG\n4-LBYR\n5-GLBY\n')
        self.assertEqual(self._table_area.take(3, GREEN), [GREEN])
        self.assertEqual(self._table_area.state(), '0-SGLBYGLBYR\n1-\n2-\n3-\n4-LBYR\n5-GLBY\n')

        self._table_area.take(4, BLACK)
        self._table_area.take(5, BLACK)
        self.assertEqual(self._table_area.state(), '0-SGLBYGLBYRBYRGBY\n1-\n2-\n3-\n4-\n5-\n')
        self.assertFalse(self._table_area.is_round_end())

        self.assertEqual(self._table_area.take(0 ,RED), [RED, RED, STARTING_PLAYER])
        for i in [ BLACK,GREEN, BLUE, YELLOW]:
            self._table_area.take(0, i)
        
        self.assertTrue(self._table_area.is_round_end())
        self._table_area.start_new_round()
        self.assertEqual(self._table_area.state(), '0-S\n1-RGLB\n2-YRGL\n3-BYRG\n4-LBYR\n5-GLBY\n')

    def test_table_area2(self) -> None:
        #take, state, is_round_end, start new_round test
        # invalid/ tricky moves
        self.assertEqual(self._table_area.state(), "0-\n1-\n2-\n3-\n4-\n5-\n")
        self._table_area.start_new_round()
        try:
            self.assertEqual(self._table_area.take(1 ,YELLOW), [])
        except KeyError:
            answear: str
            answear = '0-S\n1-RGLB\n2-YRGL\n3-BYRG\n4-LBYR\n5-GLBY\n'
            self.assertEqual(self._table_area.state(), answear)
                            

        
        self.assertEqual(self._table_area.take(0, YELLOW), [STARTING_PLAYER])
        self.assertEqual(self._table_area.state(), '0-\n1-RGLB\n2-YRGL\n3-BYRG\n4-LBYR\n5-GLBY\n')

        self.assertEqual(self._table_area.take(1 ,RED), [RED])
        self.assertEqual(self._table_area.take(2 ,RED), [RED])
        self.assertEqual(self._table_area.take(3 ,RED), [RED])
        self.assertEqual(self._table_area.take(4 ,RED), [RED])
        self.assertEqual(self._table_area.take(5 ,GREEN), [GREEN])

        self.assertEqual(self._table_area.state(), '0-GLBYGLBYGLBYLBY\n1-\n2-\n3-\n4-\n5-\n')

        self._table_area.start_new_round()

        #starting round before everything is cleaned creates mess
        #however in game we only start round at the end of round so this is not a problem
        answear = '0-GLBYGLBYGLBYLBYS\n1-RGLB\n2-YRGL\n3-BYRG\n4-LBYR\n5-GLBY\n'
        self.assertEqual(self._table_area.state(), answear)
