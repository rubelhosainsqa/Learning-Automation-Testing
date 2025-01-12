import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
time.sleep(5)

driver.find_element(By.ID, "justAnInputBox").click()
time.sleep(5)

driver.find_element(By.XPATH, "(//span[contains(text(),'choice 1')])[1]").click()
time.sleep(5)

driver.find_element(By.XPATH, "(//span[contains(text(),'choice 2 1')])[1]").click()
time.sleep(5)

driver.find_element(By.XPATH, "//div[@id='jquery-script-menu']/following-sibling::div/h1").click()
time.sleep(5)