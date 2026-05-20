class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.password_input = self.driver.locator('input[data-testid="login-password-input"]')
        self.email_input = self.driver.locator('input[data-testid="login-email-input"]')
        self.signup_button = self.driver.locator('button[data-testid="login-submit-button"]')
        
    def fill_signup_password(self, password):
        self.password_input.fill(password) 
        
    def fill_email(self, email):
        self.email_input.fill(email)
    
    def click_signup_button(self):
        self.signup_button.click()