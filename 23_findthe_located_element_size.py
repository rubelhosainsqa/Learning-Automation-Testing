import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(3)
driver.get("https://omayo.blogspot.com/")

size = driver.find_element(By.ID,"ta1").size # size is used find the located element size
print(size)