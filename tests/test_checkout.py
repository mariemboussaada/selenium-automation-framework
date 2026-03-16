from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoAlertPresentException



def test_checkout(driver):

    driver.get("https://www.saucedemo.com")

    # login
    LoginPage(driver).login("standard_user","secret_sauce")



    cart = CartPage(driver)
    cart.add_product()
    cart.open_cart()

    checkout = CheckoutPage(driver)
    checkout.checkout()
    checkout.fill_information("Test","User","1000")
    checkout.continue_checkout()
    checkout.finish_checkout()

    assert "thank you for your order" in checkout.get_confirmation_text().lower()

