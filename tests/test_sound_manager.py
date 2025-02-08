import unittest
from src.sound_manager import SoundManager

class TestSoundManager(unittest.TestCase):

    def setUp(self):
        self.sound_manager = SoundManager()

    def test_load_sound(self):
        sound_file = 'assets/sounds/tile_merge.wav'
        self.sound_manager.load_sound(sound_file)
        self.assertIn(sound_file, self.sound_manager.sounds)

    def test_play_sound(self):
        sound_file = 'assets/sounds/tile_merge.wav'
        self.sound_manager.load_sound(sound_file)
        self.sound_manager.play_sound(sound_file)
        # Assuming play_sound method has a way to verify if sound is played
        self.assertTrue(self.sound_manager.is_sound_playing(sound_file))

    def test_adjust_volume(self):
        initial_volume = self.sound_manager.volume
        self.sound_manager.set_volume(0.5)
        self.assertEqual(self.sound_manager.volume, 0.5)
        self.sound_manager.set_volume(initial_volume)  # Reset to initial volume

    def test_mute_sound(self):
        self.sound_manager.set_volume(0.0)
        self.assertEqual(self.sound_manager.volume, 0.0)

    def test_unmute_sound(self):
        self.sound_manager.set_volume(1.0)
        self.assertEqual(self.sound_manager.volume, 1.0)

if __name__ == '__main__':
    unittest.main()