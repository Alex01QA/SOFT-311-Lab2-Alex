import sys
from pathlib import Path

# Allow running this test file directly: `python tests/login_test.py`
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
import time


def run() -> None:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        login = LoginPage(page)
        page.goto("https://storedemo.testdino.com/login", wait_until="domcontentloaded")
        
        login.fill_email("alex199149@hotmail.com")
        time.sleep(5)

        login.fill_signup_password("123456")
        time.sleep(5)
        
        login.click_signup_button()
        time.sleep(5)
        
        ## validar url
        try:
            assert page.url == "https://storedemo.testdino.com/login", f"Expected URL to be 'https://storedemo.testdino.com/login' but got '{page.url}'"
            print("TEST PASSED")

        except AssertionError:
            print("TEST FAILED")  

        time.sleep(5)
        browser.close()


if __name__ == "__main__":
    run()