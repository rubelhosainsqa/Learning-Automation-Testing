import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://jqueryui.com/resizable/")
time.sleep(5)

frame = driver.find_element(By.CLASS_NAME,"demo-frame")
driver.switch_to.frame(frame)

resize_pointer = driver.find_element(By.XPATH,"//div[@class='ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']")

action = ActionChains(driver)
action.drag_and_drop_by_offset(resize_pointer,50,100).perform()
time.sleep(5)
