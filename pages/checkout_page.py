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
    summary      = (By.ID, "checkout_summary_container")   # ← page step-two
    complete     = (By.CSS_SELECTOR, ".checkout_complete_container")  # ← page complete

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def checkout(self):
        btn = self.wait.until(EC.presence_of_element_located(self.checkout_btn))
        self.driver.execute_script("arguments[0].click();", btn)
        self.wait.until(EC.presence_of_element_located(self.first_name))

    def fill_information(self, fname, lname, zip_code):
        fn = self.wait.until(EC.presence_of_element_located(self.first_name))
        fn.click()
        fn.clear()
        fn.send_keys(fname)

        ln = self.driver.find_element(*self.last_name)
        ln.click()
        ln.clear()
        ln.send_keys(lname)

        pc = self.driver.find_element(*self.postal_code)
        pc.click()
        pc.clear()
        pc.send_keys(zip_code)

    def continue_checkout(self):
        btn = self.wait.until(EC.presence_of_element_located(self.continue_btn))
        self.driver.execute_script("arguments[0].click();", btn)

        self.wait.until(EC.presence_of_element_located(self.summary))

    def finish_checkout(self):
        finish = self.wait.until(EC.presence_of_element_located(self.finish_btn))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", finish)
        self.driver.execute_script("arguments[0].click();", finish)

        self.wait.until(EC.presence_of_element_located(self.complete))

    def get_confirmation_text(self):
        return self.wait.until(
            EC.presence_of_element_located(self.confirmation)
        ).text