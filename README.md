# 🕹️ Tic-Tac-Toe Game (Python CLI)

A simple command-line based Tic-Tac-Toe game for two players, developed in Python. This version tracks session statistics, supports multiple games per session, and saves stats in text files for future reference.

---

## 📂 Features

- Two-player game (Player 1 vs Player 2)
- Real-time input with input validation
- Board display after each turn
- Win/draw detection
- Session statistics tracking:
  - Player 1 wins
  - Player 2 wins
  - Draws
- Stats saved to `session_<number>_stats.txt`
- Auto-increment session tracking via `session_count.txt`
- Option to continue or exit after each game

---

## 🛠️ Technologies Used

- Python 3
- File I/O (for session stats)
- Command-line interface (CLI)

---

## ▶️ How to Run

### ✅ Prerequisites

- Python 3 installed

### 💻 Run the game

```bash
python tic_tac_toe.py

📌 Example Gameplay
Player 1's turn
- - -
- - -
- - -

Enter row and column numbers to fix spot for Player 1 (1-3): 1 1
Player 2's turn
O - -
- - -
- - -
...
Player 1 wins the game!
