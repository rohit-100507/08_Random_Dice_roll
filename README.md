# 🎲 Dice Rolling Game

A simple Python Dice Rolling Game that uses the `random` module to simulate rolling a six-sided dice.

## Features

* Roll the dice by entering `1`
* Stop the game by entering `0`
* Generates a random number between 1 and 6
* Runs continuously until the user chooses to stop
* Handles invalid input

## Concepts Used

* `import random`
* `random.randint()`
* `while` loop
* `if`, `elif`, and `else`
* `break`
* User input
* Conditional statements

## How It Works

1. The program displays a welcome message.
2. The user enters `1` to roll the dice.
3. A random number from 1 to 6 is generated.
4. The result is displayed.
5. The user can continue rolling or enter `0` to stop.
6. If an invalid value is entered, the program displays an error message.

## Example

```text
WELCOME TO DICE ROLLING GAME

Enter 1 to roll the dice or 0 to stop: 1
You rolled: 4

Enter 1 to roll the dice or 0 to stop: 1
You rolled: 2

Enter 1 to roll the dice or 0 to stop: 0
Game stopped. Thanks for playing!
```

## How to Run

Make sure Python is installed, then run:

```bash
python dice_rolling_game.py
```

## Author

Created as a beginner Python practice project to learn loops, conditions, user input, and random numbers.
