import allure
from pages.login_page import LoginPage
from pages.cart_page import CartPage

@allure.feature("Shopping Cart")
@allure.story("Add product to cart")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_to_cart(driver):

    with allure.step("Open SauceDemo"):
        driver.get("https://www.saucedemo.com")

    with allure.step("Login with valid credentials"):
        LoginPage(driver).login("standard_user", "secret_sauce")

    with allure.step("Add backpack to cart"):
        cart = CartPage(driver)
        cart.add_product()

    with allure.step("Verify cart badge shows 1"):
        assert cart.get_cart_badge().text == "1"