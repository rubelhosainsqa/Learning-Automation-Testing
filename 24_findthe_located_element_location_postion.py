import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(3)
driver.get("https://omayo.blogspot.com/")

location_position = driver.find_element(By.ID,"ta1").location # location is used find the located element location position
print(location_position)

location_size = driver.find_element(By.ID,"ta1").rect # rect is used for want to know the located element location position and also size
print(location_size)