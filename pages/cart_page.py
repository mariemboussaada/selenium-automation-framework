from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:

    add_backpack    = (By.ID, "add-to-cart-sauce-labs-backpack")
    remove_backpack = (By.ID, "remove-sauce-labs-backpack")
    cart_badge      = (By.CLASS_NAME, "shopping_cart_badge")
    cart_icon       = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_product(self):
        self.wait.until(EC.element_to_be_clickable(self.add_backpack))  # ← ajouté
        self.driver.find_element(*self.add_backpack).click()

    def remove_product(self):
        self.wait.until(EC.element_to_be_clickable(self.remove_backpack))  # ← ajouté
        self.driver.find_element(*self.remove_backpack).click()

    def open_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.cart_icon))  # ← ajouté
        self.driver.find_element(*self.cart_icon).click()

    def get_cart_badge(self):
        return self.wait.until(EC.visibility_of_element_located(self.cart_badge))  # ← ajouté