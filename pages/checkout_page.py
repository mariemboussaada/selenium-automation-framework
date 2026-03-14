from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:

    def __init__(self,driver):
        self.driver = driver

    checkout_btn = (By.ID,"checkout")
    first_name = (By.ID,"first-name")
    last_name = (By.ID,"last-name")
    postal_code = (By.ID,"postal-code")
    continue_btn = (By.ID,"continue")
    finish_btn = (By.ID,"finish")
    confirmation = (By.CLASS_NAME,"complete-header")

    def checkout(self):
        self.driver.find_element(*self.checkout_btn).click()

    def fill_information(self,fname,lname,zip):
        self.driver.find_element(*self.first_name).send_keys(fname)
        self.driver.find_element(*self.last_name).send_keys(lname)
        self.driver.find_element(*self.postal_code).send_keys(zip)

    def continue_checkout(self):
        self.driver.find_element(*self.continue_btn).click()

    def finish_checkout(self):
        # attendre que le bouton soit visible
        finish_btn = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.finish_btn)
        )
        # scroller vers l'élément pour s'assurer qu'il est cliquable
        self.driver.execute_script("arguments[0].scrollIntoView(true);", finish_btn)
        # cliquer
        finish_btn.click()

    def get_confirmation_text(self):
        element = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".complete-header"))
        )
        return element.text


