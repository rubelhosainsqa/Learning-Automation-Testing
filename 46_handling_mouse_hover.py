import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
time.sleep(5)

menu = driver.find_element(By.ID,"blogsmenu")
action = ActionChains(driver)
action.move_to_element(menu).perform()
time.sleep(10)

submenu = driver.find_element(By.XPATH,"//a[@href='http://www.seleniumone-by-arun.blogspot.com']")
action.move_to_element(submenu).perform()
time.sleep(10)