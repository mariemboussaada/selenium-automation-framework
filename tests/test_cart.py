from pages.login_page import LoginPage
from pages.cart_page import CartPage

def test_add_to_cart(driver):

    driver.get("https://www.saucedemo.com")

    LoginPage(driver).login("standard_user","secret_sauce")

    cart = CartPage(driver)

    cart.add_product()

    assert cart.get_cart_badge().text == "1"