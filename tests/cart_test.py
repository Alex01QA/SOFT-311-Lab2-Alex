import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from playwright.sync_api import sync_playwright
from pages.cart_page import CartPage


def test_cart():

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        cart = CartPage(page)
        page.goto(
            "https://storedemo.testdino.com/products",
            wait_until="networkidle"
        )

        # Abrir producto
        cart.click_first_product()
        page.wait_for_timeout(2000)

        # Agregar carrito
        cart.add_product_to_cart()
        page.wait_for_timeout(2000)

        # Abrir carrito
        cart.open_cart()
        page.wait_for_timeout(3000)

        # Validar URL
        assert "cart" in page.url.lower(),f"Unexpected URL: {page.url}"
        print("TEST PASSED")
        browser.close()