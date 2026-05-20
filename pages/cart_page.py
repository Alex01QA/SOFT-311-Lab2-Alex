class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.first_product = driver.locator('.product-image-wrapper').first
        self.add_to_cart_button = driver.locator('.add-to-cart').first
        self.continue_shopping_button = driver.locator('.btn-success')
        self.cart_button = driver.locator('a[href="/view_cart"]').first

    def add_product_to_cart(self):
        self.first_product.hover()
        self.add_to_cart_button.click()

    def open_cart(self):
        self.cart_button.click()