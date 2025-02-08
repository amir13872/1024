import pygame
import random

class Board:
    def __init__(self):
        self.grid = [[0] * 4 for _ in range(4)]
        self.score = 0
        self.add_random_tile()
        self.add_random_tile()

    def add_random_tile(self):
        empty_tiles = [(r, c) for r in range(4) for c in range(4) if self.grid[r][c] == 0]
        if empty_tiles:
            row, col = random.choice(empty_tiles)
            self.grid[row][col] = random.choice([2, 4])

    def move(self, direction):
        if direction == pygame.K_UP:
            self.move_up()
        elif direction == pygame.K_DOWN:
            self.move_down()
        elif direction == pygame.K_LEFT:
            self.move_left()
        elif direction == pygame.K_RIGHT:
            self.move_right()
        self.add_random_tile()

    def move_up(self):
        self.grid = self.transpose(self.grid)
        self.grid = self.merge(self.grid)
        self.grid = self.transpose(self.grid)

    def move_down(self):
        self.grid = self.transpose(self.grid)
        self.grid = self.reverse(self.grid)
        self.grid = self.merge(self.grid)
        self.grid = self.reverse(self.grid)
        self.grid = self.transpose(self.grid)

    def move_left(self):
        self.grid = self.merge(self.grid)

    def move_right(self):
        self.grid = self.reverse(self.grid)
        self.grid = self.merge(self.grid)
        self.grid = self.reverse(self.grid)

    def merge(self, grid):
        new_grid = [[0] * 4 for _ in range(4)]
        for r in range(4):
            position = 0
            for c in range(4):
                if grid[r][c] != 0:
                    new_grid[r][position] = grid[r][c]
                    position += 1
            for c in range(3):
                if new_grid[r][c] == new_grid[r][c + 1] and new_grid[r][c] != 0:
                    new_grid[r][c] *= 2
                    self.score += new_grid[r][c]
                    new_grid[r][c + 1] = 0
            position = 0
            for c in range(4):
                if new_grid[r][c] != 0:
                    new_grid[r][position] = new_grid[r][c]
                    position += 1
        return new_grid

    def reverse(self, grid):
        new_grid = []
        for r in grid:
            new_grid.append(list(reversed(r)))
        return new_grid

    def transpose(self, grid):
        new_grid = [[0] * 4 for _ in range(4)]
        for r in range(4):
            for c in range(4):
                new_grid[r][c] = grid[c][r]
        return new_grid

    def update(self):
        pass

    def get_tile_value(self, row, col):
        return self.grid[row][col]

    def check_win(self):
        for row in self.grid:
            if 1024 in row:
                return True
        return False

    def check_game_over(self):
        for row in self.grid:
            if 0 in row:
                return False
        for row in range(4):
            for col in range(4):
                if col < 3 and self.grid[row][col] == self.grid[row][col + 1]:
                    return False
                if row < 3 and self.grid[row][col] == self.grid[row + 1][col]:
                    return False
        return True

    def get_score(self):
        return self.score

    def reset(self):
        self.grid = [[0] * 4 for _ in range(4)]
        self.score = 0
        self.add_random_tile()
        self.add_random_tile()