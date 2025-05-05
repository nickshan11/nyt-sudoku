import solver
import load_nyt
import sudoku_fill

print("""What difficulty would you like to solve?
1. Easy
2. Medium
3. Hard\n""")

modes = ["easy", "medium", "hard"]
difficulty = input()
while difficulty not in ["1", "2", "3"]:
    print("Select a valid option: ")
    difficulty = input()
difficulty = modes[int(difficulty)-1]

sudoku = load_nyt.scrape_sudoku_cells(difficulty)
solver.solve_curses(sudoku)
sudoku_fill.launch(sudoku, difficulty)
