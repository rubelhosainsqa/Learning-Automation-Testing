import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://getbootstrap.com/docs/4.0/components/dropdowns/")
time.sleep(5)

driver.find_element(By.ID, "dropdownMenuButton").click()
time.sleep(5)

driver.find_element(By.XPATH, "//button[@id='dropdownMenuButton']/following-sibling::div/a[2]").click()
time.sleep(5)