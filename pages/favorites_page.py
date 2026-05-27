class FavoritesPage:

    def __init__(self, driver):
        self.driver = driver

        # Productos
        self.products = driver.locator('a[href^="/product/"]')

        # Primer producto
        self.first_product = self.products.first

        # Botón favoritos header
        self.fav_header_button = driver.locator('[data-testid="header-wishlist-button"]')

        # Botón favoritos
        self.fav_button = driver.locator('[data-testid="all-products-wishlist-button"]')

        # Mostrar boton
        self.show_fav_button = driver.locator('[data-testid="show-wishlist-button"]')

   # def click_first_product(self):
       # self.first_product.click()

    def add_product_to_favorites(self):
        self.first_product.hover()
        self.fav_button.click()

    def open_favorites(self):
        self.fav_header_button.click()