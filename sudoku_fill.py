from playwright.sync_api import sync_playwright, Page


def dismiss_overlays(page):
    # list all the button‐selectors you want to try
    selectors = [
        "button.purr-blocker-card__button", 
        "button.index-module_closeX__NstKo"
    ]

    for sel in selectors:
        try:
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
    page.wait_for_selector(selector)
    page.click(selector, force=True)
    page.keyboard.type(digit)


def launch(solution, difficulty):
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            channel="chrome",
            args=["--start-maximized"])

        context = browser.new_context(no_viewport=True)
        page = context.new_page()

        page.goto(f"https://www.nytimes.com/puzzles/sudoku/{difficulty}")

        dismiss_overlays(page)
        # wait until at least one cell shows up
        page.wait_for_selector('div[data-testid^="sudoku-cell-"]')

        for row in range(9):
            for col in range(9):
                idx = row*9 + col
                if page.locator(f'div[data-cell="{idx}"]').get_attribute("aria-label") == "empty":
                    fill_cell(page, idx, str(solution[row][col]))

        input("Hit ENTER to quit…")
        browser.close()


if __name__ == "__main__":
    launch()
