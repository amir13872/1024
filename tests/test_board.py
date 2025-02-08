import unittest
from src.board import Board

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_initial_board(self):
        self.assertEqual(len(self.board.grid), 4)
        self.assertEqual(len(self.board.grid[0]), 4)
        self.assertEqual(sum(sum(row) for row in self.board.grid), 0)

    def test_insert_random_tile(self):
        self.board.insert_random_tile()
        self.assertIn(2, [tile for row in self.board.grid for tile in row])
        self.assertEqual(sum(sum(row) for row in self.board.grid), 2)

    def test_move_tiles_left(self):
        self.board.grid = [
            [2, 2, 0, 0],
            [4, 4, 4, 4],
            [0, 0, 2, 2],
            [0, 0, 0, 0]
        ]
        self.board.move_tiles('left')
        expected_grid = [
            [4, 0, 0, 0],
            [8, 0, 0, 0],
            [4, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(self.board.grid, expected_grid)

    def test_merge_tiles(self):
        self.board.grid = [
            [2, 2, 0, 0],
            [4, 4, 4, 4],
            [0, 0, 2, 2],
            [0, 0, 0, 0]
        ]
        self.board.merge_tiles('left')
        expected_grid = [
            [4, 0, 0, 0],
            [8, 0, 0, 0],
            [4, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(self.board.grid, expected_grid)

    def test_score_update(self):
        self.board.grid = [
            [2, 2, 0, 0],
            [4, 4, 4, 4],
            [0, 0, 2, 2],
            [0, 0, 0, 0]
        ]
        self.board.merge_tiles('left')
        self.assertEqual(self.board.score, 12)

    def test_game_over_condition(self):
        self.board.grid = [
            [2, 4, 2, 4],
            [4, 2, 4, 2],
            [2, 4, 2, 4],
            [4, 2, 4, 2]
        ]
        self.assertTrue(self.board.is_game_over())

if __name__ == '__main__':
    unittest.main()