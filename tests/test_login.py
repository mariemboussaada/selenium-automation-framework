import allure
from pages.login_page import LoginPage

@allure.feature("Authentication")
@allure.story("Valid login")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_valid(driver):

    with allure.step("Open SauceDemo"):
        driver.get("https://www.saucedemo.com")

    with allure.step("Login with valid credentials"):
        login = LoginPage(driver)
        login.login("standard_user", "secret_sauce")

    with allure.step("Verify redirect to inventory page"):
        assert "inventory" in driver.current_url


@allure.feature("Authentication")
@allure.story("Invalid login")
@allure.severity(allure.severity_level.NORMAL)
def test_login_invalid(driver):

    with allure.step("Open SauceDemo"):
        driver.get("https://www.saucedemo.com")

    with allure.step("Login with wrong credentials"):
        login = LoginPage(driver)
        login.login("wrong", "wrong")

    with allure.step("Verify error message is displayed"):
        assert login.get_error().is_displayed()