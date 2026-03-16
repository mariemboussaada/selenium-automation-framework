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
        self.wait = WebDriverWait(driver, 30)  # ← 30s

    def checkout(self):
        btn = self.wait.until(EC.presence_of_element_located(self.checkout_btn))
        self.driver.execute_script("arguments[0].click();", btn)
        self.wait.until(lambda d: "checkout-step-one" in d.current_url)

    def fill_information(self, fname, lname, zip):
        self.wait.until(EC.presence_of_element_located(self.first_name))
        self.driver.find_element(*self.first_name).send_keys(fname)
        self.driver.find_element(*self.last_name).send_keys(lname)
        self.driver.find_element(*self.postal_code).send_keys(zip)

    def continue_checkout(self):
        btn = self.wait.until(EC.presence_of_element_located(self.continue_btn))
        self.driver.execute_script("arguments[0].click();", btn)
        self.wait.until(lambda d: "checkout-step-two" in d.current_url)

    def finish_checkout(self):
        finish = self.wait.until(EC.presence_of_element_located(self.finish_btn))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", finish)
        self.driver.execute_script("arguments[0].click();", finish)
        self.wait.until(lambda d: "checkout-complete" in d.current_url)

    def get_confirmation_text(self):
        return self.wait.until(
            EC.presence_of_element_located(self.confirmation)
        ).text