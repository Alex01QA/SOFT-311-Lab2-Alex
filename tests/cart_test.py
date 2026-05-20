import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from playwright.sync_api import sync_playwright
from pages.cart_page import CartPage


def run() -> None:

    with sync_playwright() as playwright:

        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        cart = CartPage(page)
        page.goto(
            "https://www.automationexercise.com/products",
            wait_until="domcontentloaded"
        )
        cart.add_product_to_cart()
        page.wait_for_timeout(3000)
        cart.open_cart()
        page.wait_for_url(
            "https://www.automationexercise.com/view_cart"
        )

        try:
            assert "view_cart" in page.url
            print("TEST PASSED")

        except AssertionError:
            print("TEST FAILED") 

        browser.close()

if __name__ == "__main__":
    run()