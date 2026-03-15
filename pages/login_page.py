from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    username      = (By.ID, "user-name")
    password      = (By.ID, "password")
    login_button  = (By.ID, "login-button")
    error_message = (By.CSS_SELECTOR, "h3[data-test='error']")
    products_page = (By.CLASS_NAME, "inventory_list")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_username(self, username):
        self.wait.until(EC.visibility_of_element_located(self.username))
        self.driver.find_element(*self.username).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        # ← attendre succès OU erreur, pas uniquement succès
        self.wait.until(lambda d:
            d.find_elements(*self.products_page) or
            d.find_elements(*self.error_message)
        )

    def get_error(self):
        return self.wait.until(EC.visibility_of_element_located(self.error_message))