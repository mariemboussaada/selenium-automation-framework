from pages.login_page import LoginPage
from pages.products_page import ProductsPage

def test_products_display(driver):

    driver.get("https://www.saucedemo.com")

    LoginPage(driver).login("standard_user","secret_sauce")

    products = ProductsPage(driver)

    assert len(products.get_products()) > 0