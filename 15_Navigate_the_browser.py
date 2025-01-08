import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
time.sleep(5)
driver.find_element(By.LINK_TEXT,"compendiumdev").click()
time.sleep(5)
driver.back()  # back() is used for navigate the browser back
time.sleep(5)
driver.forward() # forward() used for navigate the browser back
time.sleep(5)

