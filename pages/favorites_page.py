class FavoritesPage:

    def __init__(self, driver):
        self.driver = driver

        # cards productos
        self.products = driver.locator('a[href^="/product/"]')

        # primer producto
        self.first_product = self.products.first

        # botón favoritos header
        self.fav_header_button = driver.get_by_test_id(
            "header-wishlist-button"
        )

    def add_product_to_favorites(self):

        # hover producto
        self.first_product.hover()

        # buscar botón SOLO dentro del producto
        fav_button = self.first_product.locator(
            '[data-testid="all-products-wishlist-button"]'
        )

        # click
        fav_button.click(force=True)

    def open_favorites(self):
        self.fav_header_button.click()