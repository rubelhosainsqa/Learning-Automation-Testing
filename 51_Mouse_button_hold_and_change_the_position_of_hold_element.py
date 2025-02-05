import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
time.sleep(5)

# Located first element for hold
From_Oslo = driver.find_element(By.ID,"box1")

# Located the second element for
To_Italy = driver.find_element(By.ID,"box106")

action = ActionChains(driver)
action.click_and_hold(From_Oslo).move_to_element(To_Italy).release().perform()
time.sleep(10)