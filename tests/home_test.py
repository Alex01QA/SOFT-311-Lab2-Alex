import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from playwright.sync_api import sync_playwright
from pages.home_page import HomePage


def test_home():

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        home = HomePage(page)
        page.goto(
            "https://storedemo.testdino.com/",
            wait_until="domcontentloaded",
        )
        #page.pause()

        # Esperar productos
        page.wait_for_selector(
            '.slick-slide'
        )

        # Validar productos visibles
        products_count = home.get_products_count()
        assert products_count > 0, f"Expected products but found {products_count}"
        print(f"Products found: {products_count}")

        # Abrir primer producto
        home.click_first_product()
        page.wait_for_timeout(3000)

        # Validar navegación
        assert "product" in page.url.lower()
        print("TEST PASSED")
        browser.close()
