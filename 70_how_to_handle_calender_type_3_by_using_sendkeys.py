import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.demo.guru99.com/test/")
time.sleep(5)

# Select Future Date
driver.find_element(By.NAME,"bdaytime").send_keys("0612")
driver.find_element(By.NAME,"bdaytime").send_keys(Keys.TAB)
driver.find_element(By.NAME,"bdaytime").send_keys("2028")
driver.find_element(By.NAME,"bdaytime").send_keys(Keys.TAB)
driver.find_element(By.NAME,"bdaytime").send_keys(1230)
driver.find_element(By.NAME,"bdaytime").send_keys(Keys.ARROW_DOWN)
time.sleep(5)