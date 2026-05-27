class SignUpPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = self.driver.locator('input[data-testid="signup-firstname-input"]')
        self.last_name_input = self.driver.locator('input[data-testid="signup-lastname-input"]')
        self.email_input = self.driver.locator('input[data-testid="signup-email-input"]')
        self.password_input = self.driver.locator('input[data-testid="signup-password-input"]')
        self.create_account_button = self.driver.locator('button[data-testid="signup-submit-button"]')
        
    def fill_signup_first_name(self, first_name):
        self.first_name_input.fill(first_name)

    def fill_signup_last_name(self, last_name):
        self.last_name_input.fill(last_name)

    def fill_signup_password(self, password):
        self.password_input.fill(password) 
        
        
    def fill_email(self, email):
        self.email_input.fill(email)

    def fill_signup_password(self, password):
        self.password_input.fill(password) 
    
    def click_signup_button(self):
        self.create_account_button.click()