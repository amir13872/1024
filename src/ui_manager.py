import pygame

class UIManager:
    def __init__(self, screen, board):
        self.screen = screen
        self.board = board
        self.font = pygame.font.Font('src/assets/fonts/OpenSans-Regular.ttf', 24)
        self.large_font = pygame.font.Font('src/assets/fonts/OpenSans-Regular.ttf', 48)
        self.background_color = (187, 173, 160)  # Background color for the game
        self.grid_color = (205, 193, 180)  # Color for the grid lines

    def draw(self):
        self.draw_background()
        self.draw_board()
        self.draw_score()

    def draw_background(self):
        self.screen.fill(self.background_color)
        for row in range(4):
            for col in range(4):
                rect = pygame.Rect(col * 100 + 50, row * 100 + 150, 100, 100)
                pygame.draw.rect(self.screen, self.grid_color, rect, border_radius=5)

    def draw_board(self):
        for row in range(4):
            for col in range(4):
                value = self.board.get_tile_value(row, col)
                self.draw_tile(row, col, value)

    def draw_tile(self, row, col, value):
        rect = pygame.Rect(col * 100 + 50, row * 100 + 150, 100, 100)
        pygame.draw.rect(self.screen, self.get_tile_color(value), rect, border_radius=5)
        if value != 0:
            text_surface = self.font.render(str(value), True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=rect.center)
            self.screen.blit(text_surface, text_rect)

    def draw_score(self):
        score_text = self.large_font.render(f'Score: {self.board.score}', True, (0, 0, 0))
        self.screen.blit(score_text, (50, 50))

    def get_tile_color(self, value):
        colors = {
            0: (205, 193, 180),
            2: (238, 228, 218),
            4: (237, 224, 200),
            8: (242, 177, 121),
            16: (245, 149, 99),
            32: (246, 124, 95),
            64: (246, 94, 59),
            128: (237, 207, 114),
            256: (237, 204, 97),
            512: (237, 200, 80),
            1024: (237, 197, 63),
            2048: (237, 194, 46),
        }
        return colors.get(value, (60, 58, 50))

# Example usage in the main game loop
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((500, 600))
    board = Board()
    ui_manager = UIManager(screen, board)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))
        ui_manager.draw()
        pygame.display.flip()
    pygame.quit()