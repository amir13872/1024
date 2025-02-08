# 1024 Game

Welcome to the 1024 Game! This project is an advanced version of the classic 2048 game, where the objective is to combine tiles with the same value to reach the target tile of 1024. This README provides comprehensive documentation on the project, including setup instructions, project structure, and guidelines for running and extending the game.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Features

- Object-oriented design with distinct classes for game logic, board management, UI rendering, animations, sound management, and configuration.
- Modern and visually appealing user interface with smooth animations for tile movements and merges.
- Support for keyboard controls (arrow keys and WASD) for tile movement.
- Sound effects for various game events (optional).
- Configurable settings for window size, colors, fonts, and sound levels.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/1024-game.git
   cd 1024-game
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the game, execute the following command in your terminal:
```
python src/game.py
```

## Project Structure

```
1024-game
├── src
│   ├── game.py               # Core game logic and event loop
│   ├── board.py              # Board management and tile logic
│   ├── ui_manager.py         # UI rendering and menu management
│   ├── animation_manager.py   # Animation effects for tiles
│   ├── sound_manager.py       # Sound effects management (optional)
│   ├── config_manager.py      # Configuration settings management (optional)
│   └── assets
│       ├── fonts             # Font files for rendering text
│       ├── sounds            # Sound files for game events
│       └── images            # Image files for graphical elements
├── tests
│   ├── test_game.py          # Unit tests for Game class
│   ├── test_board.py         # Unit tests for Board class
│   ├── test_ui_manager.py    # Unit tests for UIManager class
│   ├── test_animation_manager.py # Unit tests for AnimationManager class
│   ├── test_sound_manager.py  # Unit tests for SoundManager class
│   └── test_config_manager.py # Unit tests for ConfigManager class
├── requirements.txt           # Project dependencies
├── README.md                  # Project documentation
└── config.json                # Configuration settings
```

## Configuration

Configuration settings such as window size, colors, fonts, and sound levels can be managed in the `config.json` file. Modify this file to customize your game experience.

## Testing

Unit tests are provided for key functionalities of the game. To run the tests, navigate to the `tests` directory and execute:
```
python -m unittest discover
```

## Contributing

Contributions are welcome! If you would like to contribute to the project, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.