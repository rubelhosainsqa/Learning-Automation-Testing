import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
time.sleep(5)

button = driver.find_element(By.CLASS_NAME,"dropbtn")

driver.execute_script("arguments[0].scrollIntoView(true)", button)
button.click()
time.sleep(5)
