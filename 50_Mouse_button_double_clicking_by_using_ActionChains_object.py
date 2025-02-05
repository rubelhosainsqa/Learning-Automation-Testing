import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
time.sleep(5)

# Mouse double time clicking by using ActionChains object
element = driver.find_element(By.ID,"testdoubleclick")
action = ActionChains(driver)
action.double_click(element).perform()
time.sleep(10)