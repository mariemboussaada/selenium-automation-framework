from pages.login_page import LoginPage

def test_login_valid(driver):

    driver.get("https://www.saucedemo.com")

    login = LoginPage(driver)

    login.login("standard_user","secret_sauce")

    assert "inventory" in driver.current_url


def test_login_invalid(driver):

    driver.get("https://www.saucedemo.com")

    login = LoginPage(driver)

    login.login("wrong","wrong")

    assert login.get_error().is_displayed()