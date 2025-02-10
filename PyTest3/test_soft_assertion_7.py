from selenium import webdriver
from selenium.webdriver.common.by import By


def test_ninja_site():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")

    actual_title = driver.title
    expected_title = "Your Store Fake"
    assert actual_title.__eq__(expected_title)

    driver.find_element(By.XPATH,"//input[contains(@class,'form-control input-lg')]").send_keys("HP")
    driver.find_element(By.XPATH,"//button[contains(@class,'btn btn-default btn-lg')]").click()
    assert driver.find_element(By.XPATH,"//div[contains(@class,'product-layout product-grid col-lg-3 col-md-3 col-sm-6 col-xs-12')]").is_displayed()

