from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:

    checkout_btn = (By.ID, "checkout")
    first_name   = (By.ID, "first-name")
    last_name    = (By.ID, "last-name")
    postal_code  = (By.ID, "postal-code")
    continue_btn = (By.ID, "continue")
    finish_btn   = (By.ID, "finish")
    confirmation = (By.CSS_SELECTOR, ".complete-header")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # ← wait partagé pour toute la classe

    def checkout(self):
        self.wait.until(EC.element_to_be_clickable(self.checkout_btn))  # ← ajouté
        self.driver.find_element(*self.checkout_btn).click()

    def fill_information(self, fname, lname, zip):
        self.wait.until(EC.visibility_of_element_located(self.first_name))  # ← ajouté
        self.driver.find_element(*self.first_name).send_keys(fname)
        self.driver.find_element(*self.last_name).send_keys(lname)
        self.driver.find_element(*self.postal_code).send_keys(zip)

    def continue_checkout(self):
        self.wait.until(EC.element_to_be_clickable(self.continue_btn))  # ← ajouté
        self.driver.find_element(*self.continue_btn).click()

    def finish_checkout(self):
        finish_btn = self.wait.until(
            EC.visibility_of_element_located(self.finish_btn)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", finish_btn)
        finish_btn.click()

    def get_confirmation_text(self):
        element = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.confirmation)
        )
        return element.text