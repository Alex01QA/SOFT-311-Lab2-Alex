import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from playwright.sync_api import sync_playwright
from pages.home_page import HomePage


def run() -> None:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        home = HomePage(page)
        page.goto(
            "https://www.automationexercise.com/products",
            wait_until="domcontentloaded"
        )
        home.search_product("Tshirt")

        try:
            assert home.get_products_count() > 0
            print("TEST PASSED")

        except AssertionError:
            print("TEST FAILED") 

        browser.close()

if __name__ == "__main__":
    run()