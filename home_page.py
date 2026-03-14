from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SidebarMenu:
    def __init__(self, driver):
        self.driver = driver
        self.menu_btn = (By.ID, "react-burger-menu-btn")
        self.logout_link = (By.ID, "logout_sidebar_link")

    def open_menu(self):
        self.driver.find_element(*self.menu_btn).click()

    def logout(self):
        # ouvrir le menu si nécessaire
        self.open_menu()

        # attendre que le bouton Logout soit cliquable
        logout_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.logout_link)
        )
        # cliquer dessus
        logout_btn.click()
