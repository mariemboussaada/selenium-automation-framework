from datetime import datetime
import pytest
from selenium import webdriver
import os

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests")

@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")

    if browser.lower() == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")

        driver = webdriver.Chrome(options=options)

    elif browser.lower() == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")

        driver = webdriver.Firefox(options=options)
        driver.maximize_window()

    else:
        raise Exception(f"Browser {browser} not supported")

    driver.implicitly_wait(10)

    yield driver

    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:

        screenshots_dir = "screenshots"

        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        driver.save_screenshot(f"{screenshots_dir}/{request.node.name}_{timestamp}.png")

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)