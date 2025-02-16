# Connect_Four_Game

A Python (Processing mode) implementation of the classic **Connect 4** board game. This repository contains the game logic, a computer AI player, and tests to ensure everything runs smoothly.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Game Logic](#game-logic)
- [AI Logic](#ai-logic)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Overview

**Connect 4** is a two-player strategy game where players take turns dropping colored discs into a vertically suspended grid. The goal is to be the first to form a line of four discs—horizontally, vertically, or diagonally.

In this version:
- The **human player** uses **red** discs (represented as `1`).
- The **computer player** uses **yellow** discs (represented as `-1`).
- The game is implemented using [Processing’s Python mode](https://py.processing.org/), featuring a graphical interface with mouse-based interaction.

## Features

- **Single-player mode:** Challenge the built-in AI.
- **Interactive GUI:** Graphical display and mouse-driven gameplay using Processing.
- **Robust Game Logic:** Handles token dropping, win condition checking (rows, columns, and diagonals), and board state updates.
- **Computer AI:** The computer can either block potential wins by the player or attempt to win when the opportunity arises.
- **Scoring System:** Saves high scores to a file after the game ends.
- **Unit Tests:** Multiple test files help ensure reliability across different modules.

## Project Structure

- **connect_4.pyde:** Main Processing (Python mode) file to run the game.
- **constant.py:** Constants used throughout the game (grid size, colors, spacing, etc.).
- **game_controller.py:** Core game logic and flow.
- **game_controller_test.py:** Unit tests for the game_controller module.
- **circle.py:** Module for drawing/representing the game tokens.
- **circle_test.py:** Tests for circle.py.
- **stack.py:** Data structure used for managing game tokens during drop animations.
- **stack_test.py:** Tests for stack.py.
- **message.py:** Module for displaying game messages (turns, win messages, etc.).
- **message_test.py:** Tests for message.py.
- **computer_player.py:** AI logic for deciding the computer's moves.
- **computer_player_test.py:** Tests for computer_player.py.
- **(Any additional files):** Other supporting modules or scripts.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/connect_4.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd connect_4
   ```
3. **Install dependencies (if any):**
   - If external libraries are required (e.g., `pytest`), install them using:
     ```bash
     pip install -r requirements.txt
     ```
4. **Install Processing:**
   - Download Processing from the [official website](https://processing.org/).
   - Install [Python mode](https://py.processing.org/) within Processing.

## Usage

1. **Open `connect_4.pyde` in Processing:**
   - Launch Processing.
   - Go to **File > Open** and select `connect_4.pyde`.
   - Ensure you are in **Python mode** (select `Python` from the mode dropdown).
2. **Run the Sketch:**
   - Click the “Run” button (or press `Ctrl+R`/`Command+R`).
   - A window will appear displaying the Connect 4 board.
3. **Gameplay:**
   - **Player Turn (Red):** Click near the top of a column to see a red token preview. Release the mouse button to drop the token.
   - **Computer Turn (Yellow):** The computer automatically takes its turn after a brief delay.
   - The game continues until one player connects four tokens or the board is full.
4. **Scoring:**
   - After a win, the game will prompt you to enter your name. Your score is then saved in `scores.txt`.

## Game Logic

The core game logic in `game_controller.py` covers:

- **Token Dropping:** Handles the animation of a token dropping from the top of the board to its designated slot.
- **Turn Management:** Alternates turns between the human player and the computer.
- **Win Condition Checking:** Evaluates if four tokens of the same color are connected vertically, horizontally, or diagonally.
- **Grid Management:** Maintains a 2D grid representing the game state where each column is a list.
- **Delayed Actions:** Implements delays for the computer’s move and scoring prompt to improve gameplay flow.

## AI Logic

The computer player (in `computer_player.py`) follows a three-step decision process:

1. **Check for a Winning Move:**  
   Uses `almost_win()` to determine if the computer has three in a row and can complete a four-token line.
2. **Block the Player:**  
   Uses `stop_win()` to check if the human player has three in a row and needs to be blocked.
3. **Random Valid Move:**  
   If neither of the above conditions is met, the computer randomly selects a column that isn’t full.
