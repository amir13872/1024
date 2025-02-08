import json

class ConfigManager:
    def __init__(self, config_file):
        self.config_file = config_file
        self.settings = {}
        self.load_config()

    def load_config(self):
        """Load configuration settings from a JSON file."""
        try:
            with open(self.config_file, 'r') as file:
                self.settings = json.load(file)
        except FileNotFoundError:
            print(f"Config file {self.config_file} not found.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from {self.config_file}.")

    @property
    def window_width(self):
        return self.settings.get('window_width', 500)

    @property
    def window_height(self):
        return self.settings.get('window_height', 600)

    @property
    def frame_rate(self):
        return self.settings.get('frame_rate', 60)

    @property
    def background_color(self):
        return tuple(self.settings.get('background_color', [255, 255, 255]))

    def default_settings(self):
        """Return default configuration settings."""
        return {
            'window_size': (500, 600),
            'colors': {
                'background': (187, 173, 160),
                'tile': {
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
            },
            'fonts': {
                'main_font': 'assets/fonts/your_font.ttf',
                'font_size': 40
            },
            'sound_levels': {
                'effects': 0.5,
                'music': 0.5
            }
        }

    def get_setting(self, key):
        """Get a specific setting by key."""
        return self.settings.get(key)

    def set_setting(self, key, value):
        """Set a specific setting by key."""
        self.settings[key] = value

    def save_config(self):
        """Save the current settings to the configuration file."""
        with open(self.config_file, 'w') as file:
            json.dump(self.settings, file, indent=4)

# Example config.json file content:
# {
#     "window_width": 500,
#     "window_height": 600,
#     "frame_rate": 60,
#     "background_color": [255, 255, 255]
# }