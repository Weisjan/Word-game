# Word Game

An implementation of the popular word game "Wordle" using the Flask framework. Players have six attempts to guess a randomly selected 5-letter word. After each attempt, the player receives color-coded hints indicating whether the letters are correct and in the right position (green), correct but in the wrong position (yellow), or incorrect (red).

## Requirements

* Python 3.10  
* Flask 3.0.3

## File Structure

```
Words-game
├── templates
│   ├── index.html
│   ├── lose.html
│   └── win.html
├── wordle.py
├── words_eng.txt
└── Readme.md
```

| No | File Name     | Description                                                      |
|----|---------------|------------------------------------------------------------------|
| 1  | wordle.py     | Main application file containing Flask routes and game logic     |
| 2  | index.html    | Main HTML template for the game interface                        |
| 3  | win.html      | HTML template shown when the player wins                         |
| 4  | lose.html     | HTML template shown when the player loses                        |
| 5  | words_eng.txt | Text file containing the list of 5-letter words                  |
| 6  | Readme.md     | This README file                                                 |

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Weisjan/Word-game.git
   ```

2. Run the `wordle.py` file.

3. Open your web browser and navigate to `http://127.0.0.1:5000/` to start the game.

## How It Works

### Game Logic (`wordle.py`)

This file contains the main application code. Key components include:

- **Imports and Configuration**: Sets up Flask and imports necessary modules.
- **Routes**:
  - `/`: Main route handling game logic and rendering the game page.
  - `/gameover`: Triggered when the player wins the game.
  - `/gameover_lose`: Triggered when the player loses the game.
- **Game Logic**:
  - Initializes a new game with a random word from `words_eng.txt`.
  - Handles user guesses, provides feedback, and tracks remaining attempts.
  - Redirects to win or lose pages based on the outcome.

### Index (`index.html`)

The main game interface. Includes:

- A form for submitting guesses.
- Display of remaining attempts.
- Display of previous guesses with color-coded feedback.

### Win Page (`win.html`)

Shown when the player correctly guesses the word.

### Lose Page (`lose.html`)

Shown when the player fails to guess the word after all attempts.

## Notes

- **Word List**: You can update the `words_eng.txt` file to include your own list of 5-letter words.
- **Styling**: You can customize the appearance of the game by editing CSS styles in the HTML templates.

## Author

[Jan Weis](https://github.com/Weisjan)
