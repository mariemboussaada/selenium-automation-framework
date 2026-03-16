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
    summary      = (By.ID, "checkout_summary_container")
    complete     = (By.CSS_SELECTOR, ".checkout_complete_container")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def _fill_field(self, locator, value):
        """Remplit un champ React de façon fiable en headless."""
        field = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", field)
        self.driver.execute_script("arguments[0].value = '';", field)
        field.send_keys(value)
        actual = self.driver.execute_script("return arguments[0].value;", field)
        if actual != value:
            self.driver.execute_script(
                """
                var setter = Object.getOwnPropertyDescriptor(
                    window.HTMLInputElement.prototype, 'value').set;
                setter.call(arguments[0], arguments[1]);
                arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
                arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
                """,
                field, value
            )

    def checkout(self):
        btn = self.wait.until(EC.presence_of_element_located(self.checkout_btn))
        self.driver.execute_script("arguments[0].click();", btn)
        self.wait.until(EC.presence_of_element_located(self.first_name))

    def fill_information(self, fname, lname, zip_code):
        self._fill_field(self.first_name, fname)
        self._fill_field(self.last_name, lname)
        self._fill_field(self.postal_code, zip_code)

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