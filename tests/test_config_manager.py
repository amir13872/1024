import unittest
from src.config_manager import ConfigManager

class TestConfigManager(unittest.TestCase):

    def setUp(self):
        self.config_manager = ConfigManager('config.json')

    def test_load_config(self):
        config = self.config_manager.load_config()
        self.assertIsInstance(config, dict)
        self.assertIn('window_size', config)
        self.assertIn('colors', config)
        self.assertIn('fonts', config)
        self.assertIn('sound_levels', config)

    def test_apply_settings(self):
        config = {
            'window_size': (500, 600),
            'colors': {
                'background': '#FFFFFF',
                'tile': '#CCCCCC',
                'font': '#000000'
            },
            'fonts': {
                'main_font': 'Arial',
                'title_font': 'Verdana'
            },
            'sound_levels': {
                'effects': 0.5,
                'music': 0.7
            }
        }
        self.config_manager.apply_settings(config)
        self.assertEqual(self.config_manager.window_size, (500, 600))
        self.assertEqual(self.config_manager.colors['background'], '#FFFFFF')
        self.assertEqual(self.config_manager.fonts['main_font'], 'Arial')
        self.assertEqual(self.config_manager.sound_levels['effects'], 0.5)

    def test_invalid_config(self):
        with self.assertRaises(FileNotFoundError):
            invalid_manager = ConfigManager('invalid_config.json')
            invalid_manager.load_config()

if __name__ == '__main__':
    unittest.main()