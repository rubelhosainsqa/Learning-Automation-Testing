import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
time.sleep(5)

text_area = driver.find_element(By.ID,"ta1")
text_area.send_keys(" I am an automation test engineer")
time.sleep(5)

driver.find_element(By.LINK_TEXT,"compendiumdev")
time.sleep(10)

driver.back()
time.sleep(10)

text_area.clear()
