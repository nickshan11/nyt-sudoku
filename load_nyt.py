from playwright.sync_api import sync_playwright


def scrape_sudoku_cells(difficulty):
    with sync_playwright() as p:
        # Launch a headless Chromium browser
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()


        page.goto(f"https://www.nytimes.com/puzzles/sudoku/{difficulty}")

        # Wait until at least one cell has been injected
        page.wait_for_selector('div[data-testid^="sudoku-cell-"]')

        # Query all the cell divs
        cells = page.query_selector_all('div[data-testid^="sudoku-cell-"]')
        
        # Sort cells
        grid = []
        for row in range(9):
            temp = []
            for col in range(9):
                value = cells[row*9+col].get_attribute("aria-label")
                if value == "empty":
                    value = 0
                temp.append(int(value))
            grid.append(temp)

        browser.close()
        return grid


if __name__ == "__main__":
    print(scrape_sudoku_cells())
