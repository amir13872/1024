// Load sound effects
const tileMergeSound = new Audio('assets/sounds/tile-merge.mp3');
const moveSound = new Audio('assets/sounds/move.mp3');
const gameOverSound = new Audio('assets/sounds/game-over.mp3');
const victorySound = new Audio('assets/sounds/victory.mp3');

// Function to play sound effect
function playSound(sound) {
    sound.play();
}

// Example usage
function onTileMerge() {
    playSound(tileMergeSound);
}

function onMove() {
    playSound(moveSound);
}

function onGameOver() {
    playSound(gameOverSound);
}

function onVictory() {
    playSound(victorySound);
}
