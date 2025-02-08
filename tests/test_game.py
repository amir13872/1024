import unittest
from src.game import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_initialization(self):
        self.assertEqual(self.game.score, 0)
        self.assertEqual(len(self.game.board.tiles), 4)
        self.assertEqual(len(self.game.board.tiles[0]), 4)

    def test_move_tiles(self):
        self.game.board.tiles = [
            [2, 2, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.game.move('left')
        self.assertEqual(self.game.board.tiles, [
            [4, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ])
        self.assertEqual(self.game.score, 4)

    def test_merge_tiles(self):
        self.game.board.tiles = [
            [2, 2, 2, 2],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.game.move('left')
        self.assertEqual(self.game.board.tiles, [
            [4, 4, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ])
        self.assertEqual(self.game.score, 8)

    def test_win_condition(self):
        self.game.board.tiles = [
            [1024, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertTrue(self.game.check_win())

    def test_game_over_condition(self):
        self.game.board.tiles = [
            [2, 4, 2, 4],
            [4, 2, 4, 2],
            [2, 4, 2, 4],
            [4, 2, 4, 2]
        ]
        self.assertTrue(self.game.check_game_over())

if __name__ == '__main__':
    unittest.main()