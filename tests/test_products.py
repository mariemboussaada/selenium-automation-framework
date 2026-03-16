import allure
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

@allure.feature("Products")
@allure.story("Products page display")
@allure.severity(allure.severity_level.NORMAL)
def test_products_display(driver):

    with allure.step("Open SauceDemo"):
        driver.get("https://www.saucedemo.com")

    with allure.step("Login with valid credentials"):
        LoginPage(driver).login("standard_user", "secret_sauce")

    with allure.step("Verify products are displayed"):
        products = ProductsPage(driver)
        assert len(products.get_products()) > 0