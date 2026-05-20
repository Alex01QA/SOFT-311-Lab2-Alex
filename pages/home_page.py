class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.search_input = driver.locator('#search_product')
        self.search_button = driver.locator('#submit_search')
        self.products = driver.locator('.productinfo')

    def search_product(self, product_name):
        self.search_input.fill(product_name)
        self.search_button.click()

    def get_products_count(self):
        return self.products.count()