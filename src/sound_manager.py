import pygame
class SoundManager:
    def __init__(self):
        self.sounds = {}
        self.volume = 1.0  # Default volume level

    def load_sound(self, name, file_path):
        """Load a sound file and store it in the sounds dictionary."""
        try:
            sound = pygame.mixer.Sound(file_path)
            self.sounds[name] = sound
        except pygame.error as e:
            print(f"Error loading sound {name}: {e}")

    def play_sound(self, name):
        """Play a sound effect if it has been loaded."""
        if name in self.sounds:
            self.sounds[name].set_volume(self.volume)
            self.sounds[name].play()
        else:
            print(f"Sound {name} not found.")

    def set_volume(self, volume):
        """Set the volume for all sounds."""
        self.volume = max(0.0, min(volume, 1.0))  # Ensure volume is between 0.0 and 1.0

    def mute(self):
        """Mute all sounds."""
        self.set_volume(0.0)

    def unmute(self):
        """Unmute all sounds."""
        self.set_volume(1.0)