import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
time.sleep(5)

action = ActionChains(driver)  # ActionChains is a object and action is a reference of object
menu = driver.find_element(By.ID,"blogsmenu")
action.move_to_element(menu).perform()
time.sleep(10)