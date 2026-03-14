from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    username = (By.ID,"user-name")
    password = (By.ID,"password")
    login_button = (By.ID,"login-button")
    error_message = (By.CSS_SELECTOR,"h3[data-test='error']")

    def enter_username(self,username):
        self.driver.find_element(*self.username).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(*self.password).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def login(self,username,password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error(self):
        return self.driver.find_element(*self.error_message)
