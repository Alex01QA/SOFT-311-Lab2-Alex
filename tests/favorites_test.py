import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from playwright.sync_api import sync_playwright
from pages.favorites_page import FavoritesPage


def run():

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        favorites = FavoritesPage(page)
        page.goto(
            "https://storedemo.testdino.com/products",
            wait_until="networkidle"
        )
        # Agregar favoritos
        favorites.add_product_to_favorites()
        page.wait_for_timeout(2000)

        # Abrir favoritos
        favorites.open_favorites()
        page.wait_for_timeout(3000)

        # Validar URL
        assert "wishlist" in page.url.lower(),f"Unexpected URL: {page.url}"
        print("TEST PASSED")
        browser.close()

if __name__ == "__main__":
    run()