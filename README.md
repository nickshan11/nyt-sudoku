NYT Sudoku Auto-Solver

A command-line tool that:

Retrieves today’s NYT Sudoku (easy, medium, or hard) via Playwright

Solves the puzzle using a backtracking recursion algorithm

Opens a browser and automatically fills in every cell

Dependencies:

Python 3.8+

Playwright for Python

Installation:

Clone the repo:

git clone https://github.com/<your-username>/nyt-sudoku-solver.git
cd nyt-sudoku-solver

Create and activate a virtual environment:

python -m venv .venv
# macOS/Linux: source .venv/bin/activate
# Windows (PowerShell): .\.venv\Scripts\Activate.ps1

Install dependencies:

pip install playwright

Download browser binaries:

python -m playwright install

Usage:

Run the solver:

python main.py

Select a difficulty: easy, medium, or hard

A browser window opens and the solver fills in the grid

Press ENTER to exit

