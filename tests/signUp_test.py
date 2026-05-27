import sys
from pathlib import Path

# Allow running this test file directly: `python tests/login_test.py`
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from playwright.sync_api import sync_playwright, expect
from pages.signUp_page import SignUpPage
import time


def test_sign_up() -> None:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        signup = SignUpPage(page)
        page.goto("https://storedemo.testdino.com/signup", wait_until="domcontentloaded")
        
        signup.fill_signup_first_name("Alex")
        time.sleep(2)

        signup.fill_signup_last_name("Arias")
        time.sleep(2)

        signup.fill_email("alex199149@hotmail.com")
        time.sleep(2)

        signup.fill_signup_password("123456")
        time.sleep(2)
        
        signup.click_signup_button()
        time.sleep(2)
        ## validar url
        try:
            assert page.url == "https://storedemo.testdino.com/signup", f"Expected URL to be 'https://storedemo.testdino.com/signup' but got '{page.url}'"
            print("URL TEST PASSED")
            
            expect(page.get_by_text("User already Exist")).to_be_visible(timeout=5000)
            print("MESSAGE TEST PASSED")

        except AssertionError:
            print("TEST FAILED")  

        time.sleep(5)
        browser.close()
