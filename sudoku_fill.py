from playwright.sync_api import sync_playwright, Page


def dismiss_overlays(page):
    # list all the button‐selectors you want to try
    selectors = [
        "button.purr-blocker-card__button", 
        "button.index-module_closeX__NstKo"
    ]

    for sel in selectors:
        try:
            # wait a moment for it to appear
            page.wait_for_selector(sel, timeout=2000)
            page.click(sel)
        except:
            pass


def fill_cell(page: Page, cell_index: int, digit: str):
    """
    Clicks the sudoku cell with data-cell="{cell_index}"
    and then types `digit` on the keyboard.
    """
    selector = f'div[data-cell="{cell_index}"]'
    # wait for the grid to be ready
    page.wait_for_selector(selector)
    # click to focus the cell
    page.click(selector, force=True)
    # type the digit (or use page.keyboard.press if you prefer)
    page.keyboard.type(digit)


def launch(solution, difficulty):
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            channel="chrome",
            # optional: start maximized
            args=["--start-maximized"])

        context = browser.new_context(no_viewport=True)
        page = context.new_page()

        page.goto(f"https://www.nytimes.com/puzzles/sudoku/{difficulty}")

        dismiss_overlays(page)
        # wait until at least one cell shows up
        page.wait_for_selector('div[data-testid^="sudoku-cell-"]')

        # If you have a 9×9 solution matrix `solution[row][col]`,
        # you can map row,col → index = row*9 + col, then:
        #
        for row in range(9):
            for col in range(9):
                idx = row*9 + col
                if page.locator(f'div[data-cell="{idx}"]').get_attribute("aria-label") == "empty":
                    fill_cell(page, idx, str(solution[row][col]))

        # pause so you can see it
        input("Hit ENTER to quit…")
        browser.close()


if __name__ == "__main__":
    launch()
