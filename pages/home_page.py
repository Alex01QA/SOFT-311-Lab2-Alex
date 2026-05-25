class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.products = driver.locator('.slick-slide:not(.slick-cloned)')
        self.first_product = driver.locator('.slick-slide:not(.slick-cloned) a').first
        
    def get_products_count(self):
        return self.products.count()

    def click_first_product(self):
        self.first_product.click()