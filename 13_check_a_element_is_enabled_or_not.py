import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
time.sleep(5)

if driver.find_element(By.ID,"but2").is_enabled():
    print("This located field is enabled")

else:
    print("This located field is disabled")
