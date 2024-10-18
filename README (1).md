
# Tic-Tac-Toe Game (Terminal Version)

This is a Python-based implementation of the classic Tic-Tac-Toe game. The game is designed to be played in the terminal with enhanced text styling, offering a visually engaging experience.

## Features

- **Colored Text & Styled Output:**
  - Players' markers (X and O) are displayed in color using ANSI escape codes.
  - 'X' is shown in blue, and 'O' is shown in green.
  - The game includes bright and decorated text to make the game board easy to read.
  
- **Game Board Design:**
  - The game dynamically updates and displays the game board after each player's turn.
  
- **Winner Detection:**
  - After each turn, the game checks rows, columns, and diagonals to detect a winner.
  - If a player wins or the game results in a draw, a message is displayed.

## Screenshots

Here are some screenshots from the game:

### Winning Scenario:

![Winner Screenshot](./mnt/data/XOX_winner_screenshot.png)

### Game in Progress:

![Game Progress Screenshot](./mnt/data/image.png)

## Planned Features

- **Scoreboard:** Future versions will include a scoreboard to track multiple rounds.
- **Two-Player Network Mode or AI:** In the future, the game might support playing over a network or with an AI opponent.
- **GUI:** There is a plan to add a graphical interface for easier interaction.

## How to Run

Make sure you have Python installed on your system. You can run the game by executing the script in your terminal:
```bash
python3 XOX.py
```

## Requirements

- Python 3.x

## Notes

- The game is currently designed for local play between two players.
- ANSI escape codes used for styling may not work as expected in some terminal emulators.
- There are placeholders (TODOs) in the code for future features like AI, network play, and a GUI.
  
## License

This project is open-source and free to use.
