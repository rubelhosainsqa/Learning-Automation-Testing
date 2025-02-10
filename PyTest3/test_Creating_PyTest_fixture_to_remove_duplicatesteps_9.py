import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture()
def setup_and_teardown():
   global driver
   driver = webdriver.Chrome()
   driver.maximize_window()
   driver.get("https://tutorialsninja.com/demo/")
   yield
   driver.quit()

# Test Case 1 (Positive Test Case)
def test_search_with_valid_product(setup_and_teardown):
   driver.find_element(By.XPATH,"//input[contains(@class,'form-control input-lg')]").send_keys("HP")
   driver.find_element(By.XPATH,"//button[contains(@class,'btn btn-default btn-lg')]").click()
   assert driver.find_element(By.XPATH,"//div[contains(@class,'product-layout product-grid col-lg-3 col-md-3 col-sm-6 col-xs-12')]").is_displayed()


# Test Case 2 (Negative Test Case)
def test_search_with_invalid_product(setup_and_teardown):
   driver.find_element(By.XPATH,"//input[contains(@class,'form-control input-lg')]").send_keys("Tiger")
   driver.find_element(By.XPATH,"//button[contains(@class,'btn btn-default btn-lg')]").click()
   expected_result = "There is no product that matches the search criteria."
   assert driver.find_element(By.XPATH,"//input[@id='button-search']/following-sibling::p").text.__eq__(expected_result)


# Test Case 3 (Negative Test Case)
def test_search_with_blank_product(setup_and_teardown):
   driver.find_element(By.XPATH,"//input[contains(@class,'form-control input-lg')]").send_keys()
   driver.find_element(By.XPATH,"//button[contains(@class,'btn btn-default btn-lg')]").click()
   expected_result = "There is no product that matches the search criteria."
   assert driver.find_element(By.XPATH,"//input[@id='button-search']/following-sibling::p").text.__eq__(expected_result)
