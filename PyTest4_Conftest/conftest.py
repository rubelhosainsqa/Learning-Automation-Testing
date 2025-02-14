import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(params=["chrome","firefox","edge"])
def setup_and_teardown(request):
    global driver
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        driver = webdriver.Chrome()

    elif browser == "firefox":
        driver = webdriver.Firefox()

    elif browser == "edge":
        driver = webdriver.Edge()

    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    request.cls.driver = driver
    yield
    driver.quit()
