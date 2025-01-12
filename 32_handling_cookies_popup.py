import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.kaspersky.com/resource-center/definitions/cookies")
time.sleep(5)

driver.find_element(By.XPATH,"//button[contains(text(),'Accept and Close')]").click()

driver.quit()