import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
time.sleep(5)

attribute_value = driver.find_element(By.XPATH,"//input[@value='Search']").get_attribute("value")
print(attribute_value)