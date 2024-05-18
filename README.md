# Pong Game

This is the classic Pong game using Python and the Pygame library.

## Description

Pong is a two-player game where each player controls a paddle and tries to score points by hitting a ball past the opponent's paddle. The game continues until one player scores 10 points.

## Features

- Two-player gameplay
- Basic collision detection
- Score tracking
- Enhanced visuals with background color/image
- Rounded paddles and ball
- Sound effects for ball collisions and scoring
- Start screen and game over screen

## Controls

- Player 1 (Left Paddle): Use `W` to move up and `S` to move down
- Player 2 (Right Paddle): Use `UP` arrow to move up and `DOWN` arrow to move down

## Installation

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).
2. Install Pygame using pip:

    ```bash
    pip install pygame
    ```

3. Clone this repository or download the `pongGame.py` file and sound files (`hit.wav`, `score.mp3`).

## Running the Game

1. Open a terminal or command prompt.
2. Navigate to the directory where `pongGame.py` is located.
3. Run the game using Python:

    ```bash
    python pongGame.py
    ```

## Code Overview

The main parts of the code are:

- **Initialization**: Set up the game window, colors, and initial positions of paddles and ball.
- **Game Loop**: Handle events, update game state, and render graphics.
- **Collision Detection**: Detect and handle collisions between the ball and paddles or screen boundaries.
- **Scoring**: Update and display scores when the ball goes out of bounds.
- **Visual Enhancements**: Improved paddles and ball graphics, background color/image, and animated scoring.
- **Sound Effects**: Added sounds for ball collisions and scoring.
- **Screens**: Start screen and game over screen for better user experience.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- This game was built using the Pygame library. You can find more about Pygame [here](https://www.pygame.org/).
- Sound effects were sourced from [Freesound](https://freesound.org/).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Contact

If you have any questions or feedback, feel free to contact me.

Enjoy the game!
