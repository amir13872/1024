import pygame
from board import Board
from ui_manager import UIManager
from animation_manager import AnimationManager
from sound_manager import SoundManager
from config_manager import ConfigManager

class Game:
    def __init__(self):
        pygame.init()
        self.config = ConfigManager('config.json')
        self.screen = pygame.display.set_mode((self.config.window_width, self.config.window_height))
        pygame.display.set_caption('1024 Game')
        self.clock = pygame.time.Clock()
        self.board = Board()
        self.ui_manager = UIManager(self.screen, self.board)
        self.animation_manager = AnimationManager(self.screen)
        self.sound_manager = SoundManager()
        self.running = True

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(self.config.frame_rate)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                    self.board.move(event.key)
                    self.sound_manager.play_sound('move')
                    self.animation_manager.animate_move()
                elif event.key == pygame.K_ESCAPE:
                    self.running = False

    def update(self):
        self.board.update()
        if self.board.check_win():
            self.ui_manager.show_win_screen()
            self.running = False
        elif self.board.check_game_over():
            self.ui_manager.show_game_over_screen()
            self.running = False

    def render(self):
        self.screen.fill(self.config.background_color)
        self.ui_manager.draw()
        pygame.display.flip()

if __name__ == '__main__':
    game = Game()
    game.run()