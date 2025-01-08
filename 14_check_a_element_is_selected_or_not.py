import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
time.sleep(5)

if driver.find_element(By.ID,"checkbox2").is_selected():
    print("This located field is selected")

else:
    print("This located field is not selected")