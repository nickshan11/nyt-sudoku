import solver
import load_nyt


sudoku = load_nyt.scrape_sudoku_cells()
print(solver.solve(sudoku))
