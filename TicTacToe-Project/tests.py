from msilib.schema import SelfReg
from typing import Self
import unittest
import logic


class TestLogic(unittest.TestCase):

    def test_get_winner(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')

    # TODO: Test all functions from logic.py!

    def test_get_winner(self):
        board = [
            ['X', 'O', 'X'],
            ['X', 'O', 'O'],
            ['O', 'X', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'Draw')

    def test_other_player(self):
        self.assertEqual(logic.other_player('X'), 'O')
        self.assertEqual(logic.other_player('O'), 'X')
    
    def test_make_empty_board(self):
        board = logic.make_empty_board()
        self.assertEqual(board, [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ])


if __name__ == '__main__':
    unittest.main()