import allure
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@allure.feature("Checkout")
@allure.story("Complete checkout flow")
@allure.severity(allure.severity_level.CRITICAL)
def test_checkout(driver):

    with allure.step("Open SauceDemo"):
        driver.get("https://www.saucedemo.com")

    with allure.step("Login with valid credentials"):
        LoginPage(driver).login("standard_user", "secret_sauce")

    with allure.step("Add product to cart and open cart"):
        cart = CartPage(driver)
        cart.add_product()
        cart.open_cart()

    with allure.step("Proceed to checkout"):
        checkout = CheckoutPage(driver)
        checkout.checkout()

    with allure.step("Fill shipping information"):
        checkout.fill_information("Test", "User", "1000")
        checkout.continue_checkout()

    with allure.step("Finish order"):
        checkout.finish_checkout()

    with allure.step("Verify order confirmation message"):
        assert "thank you for your order" in checkout.get_confirmation_text().lower()