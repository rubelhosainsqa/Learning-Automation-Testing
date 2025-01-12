import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
time.sleep(5)

radio_button = driver.find_element(By.ID, "radio1")
if radio_button.is_selected():
    pass
else:
    radio_button.click()

time.sleep(5)

check_box = driver.find_element(By.ID, "checkbox1")
if check_box.is_selected():
    check_box.click()
else:
    pass
