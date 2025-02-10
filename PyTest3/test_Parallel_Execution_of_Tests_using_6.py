from selenium import webdriver

def test_open_facebook():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.facebook.com")
    driver.quit()


def test_open_youtube():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.youtube.com")
    driver.quit()


def test_open_google():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.google.com")
    driver.quit()