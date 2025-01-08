import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
time.sleep(5)


driver.find_element(By.LINK_TEXT,"Open a popup window").click()
time.sleep(5)

driver.close() # Close() function is used for close the current window