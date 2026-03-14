from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoAlertPresentException

# fonction pour fermer une alerte éventuelle
def handle_alert(driver):
    try:
        WebDriverWait(driver, 5).until(lambda d: Alert(d))
        alert = driver.switch_to.alert
        print(f"Alerte détectée : {alert.text}")
        alert.accept()  # fermer l'alerte
    except NoAlertPresentException:
        pass  # aucune alerte, continuer

def test_checkout(driver):

    driver.get("https://www.saucedemo.com")

    # login
    LoginPage(driver).login("standard_user","secret_sauce")

    # gérer une alerte éventuelle
    handle_alert(driver)

    cart = CartPage(driver)
    cart.add_product()
    cart.open_cart()

    checkout = CheckoutPage(driver)
    checkout.checkout()
    checkout.fill_information("Test","User","1000")
    checkout.continue_checkout()
    checkout.finish_checkout()

    assert "thank you for your order" in checkout.get_confirmation_text().lower()

