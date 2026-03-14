from selenium.webdriver.common.by import By

class CartPage:

    def __init__(self,driver):
        self.driver = driver

    add_backpack = (By.ID,"add-to-cart-sauce-labs-backpack")
    remove_backpack = (By.ID,"remove-sauce-labs-backpack")
    cart_badge = (By.CLASS_NAME,"shopping_cart_badge")
    cart_icon = (By.CLASS_NAME,"shopping_cart_link")

    def add_product(self):
        self.driver.find_element(*self.add_backpack).click()

    def remove_product(self):
        self.driver.find_element(*self.remove_backpack).click()

    def open_cart(self):
        self.driver.find_element(*self.cart_icon).click()

    def get_cart_badge(self):
        return self.driver.find_element(*self.cart_badge)