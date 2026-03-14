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
        options.add_argument("--headless")               # ← ajouté
        options.add_argument("--no-sandbox")             # ← ajouté
        options.add_argument("--disable-dev-shm-usage")  # ← ajouté
        options.add_argument("--disable-gpu")            # ← ajouté
        options.add_argument("--window-size=1920,1080")  # ← remplace --start-maximized
        driver = webdriver.Chrome(options=options)
    elif browser.lower() == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")               # ← ajouté pour Firefox aussi
        driver = webdriver.Firefox(options=options)
        driver.maximize_window()
    else:
        raise Exception(f"Browser {browser} not supported")

    yield driver

    # screenshot si test échoue
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        screenshots_dir = "screenshots"
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)
        driver.save_screenshot(f"{screenshots_dir}/{request.node.name}.png")

    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)