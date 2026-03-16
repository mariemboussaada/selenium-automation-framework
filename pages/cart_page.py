from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:

    add_backpack    = (By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']")
    remove_backpack = (By.CSS_SELECTOR, "[data-test='remove-sauce-labs-backpack']")
    cart_badge      = (By.CLASS_NAME, "shopping_cart_badge")
    cart_icon       = (By.CLASS_NAME, "shopping_cart_link")
    cart_page_ready = (By.CLASS_NAME, "cart_list")  # ← ajouté

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_product(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.add_backpack))
        btn.click()

    def remove_product(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.remove_backpack))
        btn.click()

    def open_cart(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.cart_icon))
        btn.click()
        self.wait.until(EC.visibility_of_element_located(self.cart_page_ready))  # ← ajouté

    def get_cart_badge(self):
        return self.wait.until(EC.visibility_of_element_located(self.cart_badge))