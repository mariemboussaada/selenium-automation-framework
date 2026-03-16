from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:

    add_backpack    = (By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']")
    remove_backpack = (By.CSS_SELECTOR, "[data-test='remove-sauce-labs-backpack']")
    cart_badge      = (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")
    cart_icon       = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)  # ← 30s

    def add_product(self):
        btn = self.wait.until(EC.presence_of_element_located(self.add_backpack))
        self.driver.execute_script("arguments[0].click();", btn)
        self.wait.until(EC.presence_of_element_located(self.cart_badge))

    def remove_product(self):
        btn = self.wait.until(EC.presence_of_element_located(self.remove_backpack))
        self.driver.execute_script("arguments[0].click();", btn)

    def open_cart(self):
        btn = self.wait.until(EC.presence_of_element_located(self.cart_icon))
        self.driver.execute_script("arguments[0].click();", btn)
        self.wait.until(lambda d: "cart" in d.current_url)

    def get_cart_badge(self):
        return self.wait.until(EC.presence_of_element_located(self.cart_badge))