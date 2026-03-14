from selenium.webdriver.common.by import By

class ProductsPage:

    def __init__(self,driver):
        self.driver = driver

    products = (By.CLASS_NAME,"inventory_item")
    first_product = (By.CLASS_NAME,"inventory_item_name")

    def get_products(self):
        return self.driver.find_elements(*self.products)

    def open_first_product(self):
        self.driver.find_element(*self.first_product).click()