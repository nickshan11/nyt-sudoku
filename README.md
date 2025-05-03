# NYT Sudoku Auto-Solver

A command-line tool that:

- Retrieves today’s NYT Sudoku (easy, medium, or hard) via Playwright

- Solves the puzzle using a backtracking recursion algorithm

- Opens a browser and automatically fills in every cell

## Dependencies:

Python 3.8+

Playwright for Python

## Installation:

1. **Clone the repo**
```bash
git clone https://github.com/nickshan11/nyt-sudoku.git
cd nyt-sudoku
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
# macOS/Linux: source .venv/bin/activate
# Windows (PowerShell): .\.venv\Scripts\Activate.ps1
```

3. Install dependencies:
```bash
pip install playwright
```
4. Download browser binaries:
```bash
python -m playwright install
```

## Usage:

1. Run the solver:
```bash
python main.py
```
Select a difficulty: easy, medium, or hard

A browser window opens and the solver fills in the grid

Press ENTER to exit

