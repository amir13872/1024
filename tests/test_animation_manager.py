import unittest
from src.animation_manager import AnimationManager

class TestAnimationManager(unittest.TestCase):
    def setUp(self):
        self.animation_manager = AnimationManager()

    def test_tile_movement_animation(self):
        # Test the tile movement animation logic
        start_position = (0, 0)
        end_position = (0, 1)
        animation = self.animation_manager.animate_tile_movement(start_position, end_position)
        self.assertIsNotNone(animation)
        self.assertEqual(animation.start, start_position)
        self.assertEqual(animation.end, end_position)

    def test_tile_merge_animation(self):
        # Test the tile merge animation logic
        position = (1, 1)
        animation = self.animation_manager.animate_tile_merge(position)
        self.assertIsNotNone(animation)
        self.assertEqual(animation.position, position)

    def test_fade_in_animation(self):
        # Test the fade-in animation for new tiles
        position = (2, 2)
        animation = self.animation_manager.animate_fade_in(position)
        self.assertIsNotNone(animation)
        self.assertEqual(animation.position, position)

    def test_zoom_in_animation(self):
        # Test the zoom-in animation for new tiles
        position = (3, 3)
        animation = self.animation_manager.animate_zoom_in(position)
        self.assertIsNotNone(animation)
        self.assertEqual(animation.position, position)

if __name__ == '__main__':
    unittest.main()